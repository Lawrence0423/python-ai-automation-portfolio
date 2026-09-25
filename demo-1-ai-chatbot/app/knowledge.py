import json
import re
from dataclasses import dataclass
from pathlib import Path


STOP_WORDS = {
    "a", "an", "and", "are", "can", "do", "does", "for", "how", "i", "is",
    "it", "my", "of", "the", "to", "what", "where", "with", "you",
}


@dataclass(frozen=True)
class KnowledgeItem:
    id: str
    question: str
    answer: str
    tags: tuple[str, ...]


@dataclass(frozen=True)
class MatchResult:
    item: KnowledgeItem | None
    confidence: float
    source: str


def tokenize(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {word for word in words if word not in STOP_WORDS and len(word) > 1}


def load_knowledge(path: Path) -> list[KnowledgeItem]:
    raw_items = json.loads(path.read_text(encoding="utf-8"))
    return [
        KnowledgeItem(
            id=item["id"],
            question=item["question"],
            answer=item["answer"],
            tags=tuple(item.get("tags", [])),
        )
        for item in raw_items
    ]


def score_item(message_tokens: set[str], item: KnowledgeItem) -> float:
    item_tokens = tokenize(" ".join([item.question, item.answer, " ".join(item.tags)]))
    if not message_tokens or not item_tokens:
        return 0.0
    overlap = message_tokens & item_tokens
    return len(overlap) / max(len(message_tokens), 1)


def find_best_answer(message: str, items: list[KnowledgeItem], threshold: float = 0.24) -> MatchResult:
    message_tokens = tokenize(message)
    best_item = None
    best_score = 0.0

    for item in items:
        score = score_item(message_tokens, item)
        if score > best_score:
            best_item = item
            best_score = score

    if best_item and best_score >= threshold:
        return MatchResult(item=best_item, confidence=round(best_score, 2), source="knowledge_base")

    return MatchResult(item=None, confidence=round(best_score, 2), source="fallback")

