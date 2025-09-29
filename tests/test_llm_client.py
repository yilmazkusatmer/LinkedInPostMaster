from src.services.llm_client import OpenAIClient


def test_parse_llm_response_structure():
    raw_response = (
        "VERSION_1: Erster Vorschlag\n"
        "VERSION_2: Zweiter Vorschlag\n"
        "VERSION_3: Dritter Vorschlag\n"
        "BEGRÜNDUNG: Änderungen auf Basis der Analyse"
    )

    parsed = OpenAIClient.parse_llm_response(
        response=raw_response,
        model="gpt-4o",
        baseline_score=40,
    )

    assert parsed.version_1 == "Erster Vorschlag"
    assert parsed.version_2 == "Zweiter Vorschlag"
    assert parsed.version_3 == "Dritter Vorschlag"
    assert parsed.reasoning.startswith("Änderungen")
    assert parsed.new_score == 65
    assert parsed.improvement == 25



