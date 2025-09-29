from __future__ import annotations

from textwrap import dedent

from src.data.post_examples import POST_EXAMPLES


def create_optimizer_prompt(user_post: str, analysis: dict[str, object]) -> str:
    positive_patterns = analysis.get("positive_patterns", [])
    negative_patterns = analysis.get("anti_patterns", [])

    positive_patterns_str = "\n".join(f"- {pattern}" for pattern in positive_patterns)
    negative_patterns_str = "\n".join(f"- {pattern}" for pattern in negative_patterns)

    if not positive_patterns_str:
        positive_patterns_str = "- Keine spezifischen Stärken erkannt."
    if not negative_patterns_str:
        negative_patterns_str = "- Keine spezifischen Schwächen erkannt."

    def summarize_examples(bucket: str) -> str:
        return "\n".join(
            f"• '{example.text[:100]}...' ({example.reactions} Reactions) → {example.analysis}"
            for example in POST_EXAMPLES[bucket]
        )

    prompt_body = dedent(
        """
        Du optimierst LinkedIn-Posts für APG|SGA basierend auf Erfolgsmustern aus 74 historischen Posts
        und einer detaillierten Voranalyse des aktuellen Posts.

        LERNE AUS DIESEN BEISPIELEN:

        === HIGH PERFORMERS (100+ Reactions) ===
        {high_performers}

        === MEDIUM PERFORMERS (50-99 Reactions) ===
        {medium_performers}

        === LOW PERFORMERS (<50 Reactions) ===
        {low_performers}

        ERKENNTNISSE:
        High Performers nutzen: Emotionale Hooks, konkrete Geschichten, geografische Bezüge mit Überraschung,
        Kreativität, echte Innovation
        Low Performers haben: Administrative Sprache, generische Beschreibungen, schwache Hooks, keine Emotionen

        DETAILS ZUM ZU OPTIMIERENDEN POST (aus Voranalyse):
        --- Erkannte Stärken ---
        {positive_patterns}

        --- Identifizierte Schwächen ---
        {negative_patterns}

        OPTIMIERE DIESEN POST:
        "[{user_post}]"

        WICHTIG:
        - Lerne aus den High Performer Patterns und der Voranalyse, aber BEHALTE die Kernbotschaft
        - Vermeide Low Performer Fallen (Administration, Generisches, Langweiliges)
        - Nutze APG|SGA-typische Sprache und Tonalität
        - KEINE EMOJIS verwenden - nur Text
        - BEHALTE alle Links und Call-to-Actions aus dem Original-Post
        - Erstelle DREI verschiedene Versionen mit unterschiedlichen Ansätzen
        - Jede Version soll vollständig sein (inklusive Links/CTAs)

        AUSGABEFORMAT:
        VERSION_1: [Erste optimierte Version - fokussiert auf emotionalen Hook + alle Original-Links]
        VERSION_2: [Zweite optimierte Version - fokussiert auf Storytelling/Konkretes + alle Original-Links]
        VERSION_3: [Dritte optimierte Version - fokussiert auf geografischen/lokalen Bezug + alle Original-Links]

        BEGRÜNDUNG: [Erkläre konkret, welche Änderungen du vorgenommen hast, warum diese basierend auf den
        Erfolgsmustern und der VORANALYSE funktionieren werden. Beziehe dich explizit auf die erkannten Stärken
        und Schwächen des Original-Posts.]

        BEISPIEL für vollständige Version:
        "Emotionaler Hook-Text hier...

        Original Call-to-Action und Link hier: https://lnkd.in/example"

        Antworte NUR in diesem Format.
        """
    ).strip()

    prompt = prompt_body.format(
        high_performers=summarize_examples("high_performers"),
        medium_performers=summarize_examples("medium_performers"),
        low_performers=summarize_examples("low_performers"),
        positive_patterns=positive_patterns_str,
        negative_patterns=negative_patterns_str,
        user_post=user_post.replace("{", "{{").replace("}", "}}"),
    )

    return prompt


