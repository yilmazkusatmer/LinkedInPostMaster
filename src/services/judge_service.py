from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Dict, Optional

import openai

from src.data.post_examples import POST_EXAMPLES


@dataclass
class JudgeResult:
    best_version_text: str
    model_used: str
    version_number: str
    judge_reasoning: str
    raw_judge_response: str


class JudgeService:
    """Encapsulates interaction with the o3 judge model."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client: Optional[openai.OpenAI] = None

    @property
    def client(self) -> openai.OpenAI:
        if not self._client:
            if not self.api_key:
                raise ValueError("OPENAI_API_KEY is missing for JudgeService.")
            self._client = openai.OpenAI(api_key=self.api_key)
        return self._client

    def judge(self, original_post: str, all_optimizations: Dict[str, Dict[str, str]]) -> JudgeResult:
        assistant_prompt = (
            "Du bist ein LinkedIn Post Judge, spezialisiert auf APG|SGA Performance."
            " Deine Aufgabe ist es, verschiedene optimierte Versionen eines Original-Posts"
            " zu bewerten, den besten auszuwählen und deine Entscheidung klar und präzise"
            " zu begründen. Fokus liegt auf der Maximierung der Performance (Reaktionen,"
            " Sichtbarkeit, Engagement) gemäss den APG|SGA Erfolgsmustern und den"
            " bereitgestellten historischen Post-Beispielen.\n\n###AUSGABEFORMAT###\n"
            "BESTE_VERSION_TEXT: [Der vollständige Text der besten Version, inklusive Links/CTAs]"
            "\nMODELL: [Name des Modells, das diese Version generiert hat, z.B. 'gpt-4o']"
            "\nVERSION_NUMMER: [Die Nummer der Version, z.B. '1', '2' oder '3']"
            "\nJUDGE_BEGRÜNDUNG: [Deine detaillierte Begründung für die Auswahl dieser Version]"
        )

        user_prompt_parts = [f"Original Post:\n\"\"\"{original_post}\"\"\"\n\n"]

        user_prompt_parts.append("LERNE AUS DIESEN BEISPIELEN:\n\n")
        user_prompt_parts.append("=== HIGH PERFORMERS (100+ Reactions) ===\n")
        user_prompt_parts.append(
            "\n".join(
                f"• '{hp.text[:100]}...' ({hp.reactions} Reactions) → {hp.analysis}"
                for hp in POST_EXAMPLES["high_performers"]
            )
        )
        user_prompt_parts.append("\n\n=== MEDIUM PERFORMERS (50-99 Reactions) ===\n")
        user_prompt_parts.append(
            "\n".join(
                f"• '{mp.text[:100]}...' ({mp.reactions} Reactions) → {mp.analysis}"
                for mp in POST_EXAMPLES["medium_performers"]
            )
        )
        user_prompt_parts.append("\n\n=== LOW PERFORMERS (<50 Reactions) ===\n")
        user_prompt_parts.append(
            "\n".join(
                f"• '{lp.text[:100]}...' ({lp.reactions} Reactions) → {lp.analysis}"
                for lp in POST_EXAMPLES["low_performers"]
            )
        )
        user_prompt_parts.append(
            "\n\nERKENNTNISSE:\nHigh Performers nutzen: Emotionale Hooks, konkrete Geschichten, geografische"
            " Bezüge mit Überraschung, Kreativität, echte Innovation\nLow Performers haben:"
            " Administrative Sprache, generische Beschreibungen, schwache Hooks, keine Emotionen\n\n"
        )

        for model_name, optimization in all_optimizations.items():
            user_prompt_parts.append(f"=== Optimierung von {model_name} ===\n")
            user_prompt_parts.append(f"Version 1:\n\"\"\"{optimization.get('version_1', 'N/A')}\"\"\"\n")
            user_prompt_parts.append(f"Version 2:\n\"\"\"{optimization.get('version_2', 'N/A')}\"\"\"\n")
            user_prompt_parts.append(f"Version 3:\n\"\"\"{optimization.get('version_3', 'N/A')}\"\"\"\n")
            user_prompt_parts.append(f"Begründung von {model_name}:\n\"\"\"{optimization.get('reasoning', 'N/A')}\"\"\"\n\n")

        user_prompt_parts.append(
            "WICHTIG:\n"
            "- Bewerte jede Version objektiv basierend auf APG|SGA Erfolgsmustern.\n"
            "- Wähle die beste optimierte Version aus ALLEN Modellen (Version 1, 2 oder 3 von"
            " GPT-4o, GPT-4.1, GPT-5 oder O3).\n"
            "- Begründe ausführlich, WARUM diese Version die beste ist und welche Kriterien sie"
            " am besten erfüllt, indem du dich auf die bereitgestellten historischen Beispiel-Posts"
            " und deren Erkenntnisse beziehst.\n"
            "- Gib NUR die beste Version und deine detaillierte Begründung zurück.\n\n"
            "###AUSGABEFORMAT###\n"
            "BESTE_VERSION_TEXT: [Der vollständige Text der besten Version, inklusive Links/CTAs]\n"
            "MODELL: [Name des Modells, das diese Version generiert hat, z.B. 'gpt-4o']\n"
            "VERSION_NUMMER: [Die Nummer der Version, z.B. '1', '2' oder '3']\n"
            "JUDGE_BEGRÜNDUNG: [Deine detaillierte Begründung für die Auswahl dieser Version]"
        )

        judge_user_prompt = "".join(user_prompt_parts)

        response = self.client.chat.completions.create(
            model="o3",
            messages=[{"role": "system", "content": assistant_prompt}, {"role": "user", "content": judge_user_prompt}],
            reasoning_effort="low",
        )

        raw_text = response.choices[0].message.content or ""

        best_version_match = re.search(r"BESTE_VERSION_TEXT:\s*(.*?)(?=\nMODELL:|###|$)", raw_text, re.DOTALL)
        model_match = re.search(r"MODELL:\s*(.*?)(?=\nVERSION_NUMMER:|###|$)", raw_text)
        version_match = re.search(r"VERSION_NUMMER:\s*(.*?)(?=\nJUDGE_BEGRÜNDUNG:|###|$)", raw_text)
        reasoning_match = re.search(r"JUDGE_BEGRÜNDUNG:\s*(.*?)$", raw_text, re.DOTALL)

        return JudgeResult(
            best_version_text=(best_version_match.group(1).strip() if best_version_match else f"Parsing Error: BESTE_VERSION_TEXT nicht gefunden. Rohantwort: {raw_text}"),
            model_used=model_match.group(1).strip() if model_match else "N/A (Modell nicht gefunden)",
            version_number=version_match.group(1).strip() if version_match else "N/A (Version nicht gefunden)",
            judge_reasoning=reasoning_match.group(1).strip() if reasoning_match else "N/A (Begründung nicht gefunden)",
            raw_judge_response=raw_text,
        )


