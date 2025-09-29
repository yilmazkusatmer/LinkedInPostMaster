from src.analysis.post_analysis import analyze_post_with_rules


def test_analyze_post_with_rules_positive_patterns():
    post = "Neu steht das Matterhorn mitten in Zürich: UBS inszeniert ein bemerkenswertes Mural."
    analysis = analyze_post_with_rules(post)

    assert analysis["total_score"] > 0
    assert analysis["positive_patterns"]
    assert any(
        "Neu steht" in pattern or "Starker Einstieg" in pattern
        for pattern in analysis["positive_patterns"]
    )


def test_analyze_post_with_rules_negative_patterns():
    post = "Administrative Phase: Call for Entries geöffnet."
    analysis = analyze_post_with_rules(post)

    assert analysis["total_score"] <= 0
    assert any("Administrative Sprache" in pattern for pattern in analysis["anti_patterns"])


