from pathlib import Path

from app.knowledge import find_best_answer, load_knowledge, tokenize


def test_tokenize_removes_common_words():
    assert "return" in tokenize("How do I return an order?")
    assert "how" not in tokenize("How do I return an order?")


def test_returns_best_faq_answer():
    items = load_knowledge(Path("app/data/faqs.json"))
    result = find_best_answer("I need to return my order", items)
    assert result.item is not None
    assert result.item.id == "return-policy"
    assert result.source == "knowledge_base"


def test_low_confidence_uses_fallback():
    items = load_knowledge(Path("app/data/faqs.json"))
    result = find_best_answer("Do you sell wholesale office furniture?", items)
    assert result.item is None
    assert result.source == "fallback"

