from pathlib import Path

from extractor import extract_records, load_sources, validate_record


def test_extracts_all_fixture_records():
    sources = load_sources(Path("sources.json"))
    records, errors = extract_records(sources)
    assert len(records) == 4
    assert errors == []


def test_validation_catches_missing_fields():
    errors = validate_record({
        "source": "products",
        "record_id": "",
        "title": "Example",
        "category": "demo",
        "value": "12",
        "updated_at": "2026-09-25",
    })
    assert "missing record_id" in errors


def test_validation_requires_numeric_value():
    errors = validate_record({
        "source": "products",
        "record_id": "A",
        "title": "Example",
        "category": "demo",
        "value": "not-a-number",
        "updated_at": "2026-09-25",
    })
    assert "value must be numeric" in errors

