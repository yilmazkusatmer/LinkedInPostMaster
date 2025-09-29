from src.prompts.optimizer_prompt import create_optimizer_prompt


def test_create_optimizer_prompt_contains_versions_headers():
    prompt = create_optimizer_prompt(
        user_post="Testpost mit Call-to-Action: https://example.com",
        analysis={
            "positive_patterns": ["Geografischer Bezug: Zürich"],
            "anti_patterns": ["Administrative Sprache"],
            "total_score": 42,
        },
    )

    assert "VERSION_1" in prompt
    assert "VERSION_2" in prompt
    assert "VERSION_3" in prompt
    assert "Geografischer Bezug" in prompt
    assert "Administrative Sprache" in prompt



