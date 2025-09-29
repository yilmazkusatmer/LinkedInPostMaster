from __future__ import annotations

import re
from typing import Dict

from src.domain.performance_rules import PERFORMANCE_RULES


def analyze_post_with_rules(post_text: str) -> Dict[str, object]:
    """Analyse post content based on curated performance rules."""

    analysis: Dict[str, object] = {
        "positive_patterns": [],
        "anti_patterns": [],
        "total_score": 0,
    }

    lower_post_text = post_text.lower()

    def prepare_pattern(pattern_data: Dict[str, object]) -> str:
        raw_pattern = pattern_data.get("pattern") or pattern_data.get("term")
        if not isinstance(raw_pattern, str):  # defensive fallback
            return ""
        pattern_string = raw_pattern.lower()
        return pattern_string if pattern_data.get("regex") else pattern_string.replace(" + ", ".*?")

    def add_positive(entry: str, boost: int | None = None) -> None:
        if entry:
            analysis["positive_patterns"].append(entry)
        if isinstance(boost, int):
            analysis["total_score"] += boost

    def add_negative(entry: str, penalty: int | None = None) -> None:
        if entry:
            analysis["anti_patterns"].append(entry)
        if isinstance(penalty, int):
            analysis["total_score"] += penalty

    for pattern_data in PERFORMANCE_RULES["geographic_patterns"]["high_performance"]:
        if prepare_pattern(pattern_data) and re.search(prepare_pattern(pattern_data), lower_post_text):
            add_positive(
                f"Geografischer Bezug: {pattern_data['pattern']} (+{pattern_data['boost']}%) (z.B. {pattern_data['examples'][0]})",
                boost=pattern_data.get("boost"),
            )

    for pattern_data in PERFORMANCE_RULES["geographic_patterns"]["avoid"]:
        if prepare_pattern(pattern_data) and re.search(prepare_pattern(pattern_data), lower_post_text):
            add_negative(
                f"Generischer Ort: {pattern_data['pattern']} ({pattern_data['impact']}%) (z.B. {pattern_data['examples'][0]})",
                penalty=pattern_data.get("impact"),
            )

    for trigger_data in PERFORMANCE_RULES["innovation_language"]["triggers"]:
        if prepare_pattern(trigger_data) and re.search(prepare_pattern(trigger_data), lower_post_text):
            add_positive(
                f"Exklusivität/Innovation: {trigger_data['term']} (+{trigger_data['boost']}%) (z.B. {trigger_data['examples'][0]})",
                boost=trigger_data.get("boost"),
            )

    for anti_data in PERFORMANCE_RULES["innovation_language"]["avoid"]:
        if prepare_pattern(anti_data) and re.search(prepare_pattern(anti_data), lower_post_text):
            add_negative(
                f"Administrative Sprache: {anti_data['term']} ({anti_data['impact']}%) (z.B. {anti_data['examples'][0]})",
                penalty=anti_data.get("impact"),
            )

    for pattern_data in PERFORMANCE_RULES["content_structure"]["successful_openings"]:
        if prepare_pattern(pattern_data) and re.search(prepare_pattern(pattern_data), lower_post_text):
            add_positive(
                f"Starker Einstieg: {pattern_data['pattern']} (Performance: {pattern_data['performance']}) (z.B. {pattern_data['examples'][0]})",
            )
            performance = pattern_data.get("performance")
            if performance == "Sehr stark":
                analysis["total_score"] += 20
            elif performance == "Stark":
                analysis["total_score"] += 10

    for pattern_data in PERFORMANCE_RULES["content_structure"]["emotional_triggers"]:
        if prepare_pattern(pattern_data) and re.search(prepare_pattern(pattern_data), lower_post_text):
            add_positive(
                f"Emotionale Verbindung: {pattern_data['pattern']} (Performance: {pattern_data['performance']}) (z.B. {pattern_data['examples'][0]})",
            )
            performance = pattern_data.get("performance")
            if performance == "Top":
                analysis["total_score"] += 25
            elif performance == "Stark":
                analysis["total_score"] += 15

    for anti_data in PERFORMANCE_RULES["content_structure"]["anti_patterns"]:
        if prepare_pattern(anti_data) and re.search(prepare_pattern(anti_data), lower_post_text):
            add_negative(
                f"Struktur/Anti-Pattern: {anti_data['pattern']} ({anti_data['impact']}%) (z.B. {anti_data['examples'][0]})",
                penalty=anti_data.get("impact"),
            )

    post_length = len(post_text)
    if 150 <= post_length <= 600:
        add_positive("Länge: Optimal (150-600 Zeichen)", boost=10)
    elif post_length > 600:
        add_negative("Länge: Zu lang (über 600 Zeichen)", penalty=-5)
    else:
        add_negative("Länge: Zu kurz (unter 150 Zeichen)", penalty=-5)

    analysis["total_score"] = max(0, min(100, analysis["total_score"]))
    return analysis


