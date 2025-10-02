from __future__ import annotations

import html
from typing import Dict

import streamlit as st

from src.services.llm_client import LLMResponse
from src.services.judge_service import JudgeResult


VERSION_STYLES: Dict[str, Dict[str, str]] = {
    "version_1": {"bg": "#e0f2f7", "border": "#007bff"},
    "version_2": {"bg": "#e6ffe6", "border": "#28a745"},
    "version_3": {"bg": "#fff3cd", "border": "#ffc107"},
    "reasoning": {"bg": "#f0f2f6", "border": "#6c757d"},
    "judge_best": {"bg": "#d4edda", "border": "#28a745"},
    "judge_reasoning": {"bg": "#f0f8ff", "border": "#007bff"},
}


def _format_html(text: str) -> str:
    return html.escape(text).replace("\n", "<br>") if text else ""


def _render_scroll_box(content: str, style_key: str, height: int) -> None:
    styles = VERSION_STYLES[style_key]
    html_block = f"""
    <div style="background-color: {styles['bg']}; padding: 15px; border-radius: 10px; border-left: 4px solid {styles['border']}; height: {height}px; overflow-y: auto;">
        {content}
    </div>
    """
    st.markdown(html_block, unsafe_allow_html=True)


def render_optimization_panel(
    model_name: str,
    response: LLMResponse,
    analysis: Dict[str, object],
    prompt: str,
    debug_key_prefix: str,
) -> None:
    st.write("**✨ Optimierte Versionen**")

    if response.version_1:
        st.write("**Version 1: Emotionaler Hook**")
        _render_scroll_box(_format_html(response.version_1), "version_1", height=300)

    if response.version_2:
        st.write("**Version 2: Storytelling/Konkretes**")
        _render_scroll_box(_format_html(response.version_2), "version_2", height=300)

    if response.version_3:
        st.write("**Version 3: Geografischer/Lokaler Bezug**")
        _render_scroll_box(_format_html(response.version_3), "version_3", height=300)

    if response.reasoning:
        st.write("**💡 Begründung der Optimierung**")
        _render_scroll_box(_format_html(response.reasoning), "reasoning", height=350)

    _render_analysis_summary(analysis)

    if st.checkbox(
        f"🔧 Debug-Informationen für {model_name} anzeigen",
        key=f"{debug_key_prefix}_debug_{model_name}",
    ):
        with st.expander("Raw LLM Response"):
            st.text_area(
                label="Raw LLM Response",
                value=response.raw_response or "Keine Rohdaten vom LLM erhalten oder API-Aufruf fehlgeschlagen.",
                height=200,
                disabled=True,
                label_visibility="collapsed",
                key=f"{debug_key_prefix}_raw_response_{model_name}",
            )
        with st.expander("Verwendeter Prompt"):
            st.text_area(
                label="Verwendeter Prompt",
                value=prompt,
                height=200,
                disabled=True,
                label_visibility="collapsed",
                key=f"{debug_key_prefix}_prompt_{model_name}",
            )


def _render_analysis_summary(analysis: Dict[str, object]) -> None:
    positive_patterns = analysis.get("positive_patterns", [])
    anti_patterns = analysis.get("anti_patterns", [])

    filtered_positive = [
        pattern
        for pattern in positive_patterns
        if pattern != "Länge: Optimal (150-600 Zeichen)" and "Flughafen Zürich" not in pattern
    ]

    if not filtered_positive and not anti_patterns:
        return

    with st.expander("🔍 Detaillierte Analyse"):
        if filtered_positive:
            st.success("**Erkannte Stärken:**")
            for pattern in filtered_positive:
                st.write(f"✅ {pattern}")

        if anti_patterns:
            st.error("**Identifizierte Schwächen:**")
            for pattern in anti_patterns:
                st.write(f"❌ {pattern}")


def render_judge_result(judge_result: JudgeResult, debug_key: str) -> None:
    st.success(
        f"**Der Gewinner ist Version {judge_result.version_number} von {judge_result.model_used}!**"
    )

    st.write("**Beste Version:**")
    _render_scroll_box(
        _format_html(judge_result.best_version_text),
        "judge_best",
        height=350,
    )

    st.write("**Begründung des Judges:**")
    _render_scroll_box(
        _format_html(judge_result.judge_reasoning),
        "judge_reasoning",
        height=250,
    )

    if st.checkbox("🔧 Debug-Informationen für o3 Judge anzeigen", key=f"{debug_key}_debug_o3"):
        with st.expander("Raw o3 Judge Response"):
            st.text_area(
                label="Raw o3 Judge Response",
                value=judge_result.raw_judge_response,
                height=200,
                disabled=True,
                label_visibility="collapsed",
                key=f"{debug_key}_raw_judge_response",
            )

