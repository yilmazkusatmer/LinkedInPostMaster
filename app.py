from __future__ import annotations

import concurrent.futures
import os
from typing import Dict, Optional

import streamlit as st
from dotenv import load_dotenv

from src.analysis.post_analysis import analyze_post_with_rules
from src.config import APP_CONFIG
from src.prompts.optimizer_prompt import create_optimizer_prompt
from src.services.judge_service import JudgeService
from src.services.llm_client import LLMResponse, OpenAIClient
from src.ui.components import render_judge_result, render_optimization_panel

load_dotenv()


client_cache: Dict[str, OpenAIClient] = {}


def get_openai_client(api_key: str) -> OpenAIClient:
    if api_key not in client_cache:
        client_cache[api_key] = OpenAIClient(api_key=api_key)
    return client_cache[api_key]


def run_parallel_optimizations(
    client: OpenAIClient,
    prompt: str,
    baseline_score: Optional[int],
    temperature: float,
) -> Dict[str, LLMResponse]:
    results: Dict[str, LLMResponse] = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_model = {
            executor.submit(
                client.optimize_post,
                prompt=prompt,
                model=model,
                baseline_score=baseline_score,
                temperature=temperature,
            ): model
            for model in APP_CONFIG.openai_models
        }

        for future in concurrent.futures.as_completed(future_to_model):
            model_name = future_to_model[future]
            try:
                results[model_name] = future.result()
            except Exception as exc:  # noqa: BLE001
                results[model_name] = LLMResponse(
                    model=model_name,
                    reasoning=f"Fehler bei der Optimierung mit {model_name}: {exc}",
                    raw_response=str(exc),
                    error=str(exc),
                )

    return results


EXAMPLE_POSTS: Dict[str, str] = {
    "ABB AdWalks (Original)": (
        "Animation, die Maßstäbe setzt: ABB bespielt die AdWalks am Flughafen Zürich AG mit einer"
        " eindrucksvollen animierten Kampagne über mehrere Screens hinweg. Eine"
        " aufmerksamkeitsstarke Kampagne in einem hochwertigen Werbeumfeld.\n\nDigitales"
        " Werbeangebot am Flughafen Zürich entdecken: https://lnkd.in/dt9k3AXG"
    ),
    "Neue Werbeflächen Basel": (
        "Neue digitale Werbeflächen in Basel verfügbar. Interessante Möglichkeiten für lokale"
        " Unternehmen.\n\nMehr Informationen: [Link]"
    ),
    "Schweizer Kampagne": (
        "Innovative Werbelösungen für Schweizer Städte. Modernste Technologie für maximale"
        " Aufmerksamkeit.\n\nJetzt entdecken: [Link]"
    ),
}


def main() -> None:
    st.set_page_config(
        page_title="LinkedInPostMaster - AI Post Optimizer",
        page_icon="",
        layout="wide",
    )

    st.title("LinkedInPostMaster")
    st.markdown("**KI-gestützte LinkedIn Post-Optimierung mit Model-Evaluation**")

    with st.sidebar:
        st.subheader("OpenAI API Konfiguration")

        env_api_key = os.getenv("OPENAI_API_KEY", "")
        manual_key_default = st.session_state.get("manual_api_key", "")
        api_key_input = st.text_input(
            "OpenAI API Key",
            value="" if env_api_key else manual_key_default,
            type="password",
            help="Falls in .env vorhanden, wird dieser Key automatisch genutzt.",
        )

        if env_api_key:
            st.success("✅ OPENAI_API_KEY aus .env geladen")
            active_api_key = env_api_key
        elif api_key_input:
            st.session_state["manual_api_key"] = api_key_input
            st.success("✅ OpenAI API Key manuell gesetzt")
            active_api_key = api_key_input
        else:
            st.error("❌ Kein OpenAI API Key gefunden. Bitte manuell eingeben.")
            active_api_key = ""

        available_models = APP_CONFIG.openai_models
        selected_model = st.selectbox(
            "GPT Model:",
            options=available_models,
            index=available_models.index(APP_CONFIG.default_model),
        )

        temperature_value = st.slider(
            "Temperatur (Kreativität)",
            min_value=0.0,
            max_value=1.0,
            value=APP_CONFIG.default_temperature,
            step=0.1,
            help="Für gpt-5 wird die Temperatureinstellung nicht angewandt.",
        )

        st.info(
            f"Verwendet: {selected_model} (Temp: {temperature_value}, Max Tokens: {APP_CONFIG.max_tokens})"
        )

        run_all_models = st.checkbox("Alle Modelle parallel ausführen")

    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.subheader("📝 Post-Eingabe")

        selected_example = st.selectbox(
            "Beispiel wählen:",
            options=["Eigener Post"] + list(EXAMPLE_POSTS.keys()),
        )

        default_text = EXAMPLE_POSTS.get(selected_example, "")
        user_input = st.text_area(
            "Post-Text:",
            height=200,
            value=default_text,
            placeholder="Geben Sie hier Ihren LinkedIn Post-Entwurf ein...",
        )

        optimize_triggered = st.button(
            "🚀 Post optimieren",
            type="primary",
            use_container_width=True,
            disabled=not bool(active_api_key),
        )

    if optimize_triggered:
        if not user_input.strip():
            st.warning("⚠️ Bitte geben Sie einen Post-Text ein")
        elif not active_api_key:
            st.error("❌ Bitte geben Sie einen gültigen OpenAI API Key ein")
        else:
            with st.spinner("Analysiere und optimiere..."):
                analysis = analyze_post_with_rules(user_input)
                prompt = create_optimizer_prompt(user_input, analysis)

                st.session_state["analysis"] = analysis
                st.session_state["prompt"] = prompt
                st.session_state["user_input"] = user_input

                client = get_openai_client(active_api_key)

                if run_all_models:
                    st.session_state["all_optimizations"] = run_parallel_optimizations(
                        client=client,
                        prompt=prompt,
                        baseline_score=analysis["total_score"],
                        temperature=temperature_value,
                    )
                    st.session_state.pop("optimization", None)
                else:
                    result = client.optimize_post(
                        prompt=prompt,
                        model=selected_model,
                        baseline_score=analysis["total_score"],
                        temperature=temperature_value,
                    )
                    st.session_state["optimization"] = result
                    st.session_state.pop("all_optimizations", None)

                st.session_state.pop("judge_result", None)

    if "analysis" not in st.session_state:
        return

    analysis_state = st.session_state["analysis"]
    prompt_state = st.session_state.get("prompt", "")
    user_input_state = st.session_state.get("user_input", "")

    st.divider()
    st.subheader("📊 Ergebnisse")

    all_results = st.session_state.get("all_optimizations")
    single_result = st.session_state.get("optimization")

    if all_results:
        st.write("**✨ Ergebnisse im Vergleich**")

        columns = st.columns(len(all_results))
        for column, (model_name, result) in zip(columns, all_results.items(), strict=True):
            with column:
                st.subheader(f"**{model_name}**")
                render_optimization_panel(
                    model_name=model_name,
                    response=result,
                    analysis=analysis_state,
                    prompt=prompt_state,
                    debug_key_prefix=model_name,
                )

        st.divider()
        st.subheader("🏆 Richter-Urteil (o3)")

        if st.button("🏆 Gewinner ermitteln", type="secondary", use_container_width=True):
            if not active_api_key:
                st.error("❌ Kein OpenAI API Key verfügbar. Bitte API Key angeben.")
            else:
                judge_service = JudgeService(api_key=active_api_key)
                with st.spinner("o3 bewertet die Posts..."):
                    judge_result = judge_service.judge(
                        original_post=user_input_state,
                        all_optimizations={
                            model: response.as_dict() for model, response in all_results.items()
                        },
                    )
                    st.session_state["judge_result"] = judge_result

        if st.session_state.get("judge_result"):
            render_judge_result(
                st.session_state["judge_result"],
                debug_key="judge",
            )

    elif single_result:
        _, center_col, _ = st.columns([1, 2, 1])
        with center_col:
            render_optimization_panel(
                model_name=single_result.model or selected_model,
                response=single_result,
                analysis=analysis_state,
                prompt=prompt_state,
                debug_key_prefix="single",
            )


if __name__ == "__main__":
    main()