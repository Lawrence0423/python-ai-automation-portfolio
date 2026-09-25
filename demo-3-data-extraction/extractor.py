import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = ["source", "record_id", "title", "category", "value", "updated_at"]


@dataclass(frozen=True)
class SourceConfig:
    name: str
    type: str
    path: Path
    mapping: dict[str, str]


def load_sources(path: Path) -> list[SourceConfig]:
    raw_sources = json.loads(path.read_text(encoding="utf-8"))
    base_dir = path.parent
    return [
        SourceConfig(
            name=item["name"],
            type=item["type"],
            path=(base_dir / item["path"]).resolve(),
            mapping=item["mapping"],
        )
        for item in raw_sources
    ]


def load_fixture(path: Path) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_record(source: SourceConfig, raw: dict[str, Any]) -> dict[str, Any]:
    normalized = {"source": source.name}
    for output_field, input_field in source.mapping.items():
        normalized[output_field] = raw.get(input_field)
    return normalized


def validate_record(record: dict[str, Any]) -> list[str]:
    errors = []
    for field in REQUIRED_FIELDS:
        if record.get(field) in (None, ""):
            errors.append(f"missing {field}")
    try:
        float(record.get("value"))
    except (TypeError, ValueError):
        errors.append("value must be numeric")
    return errors


def extract_records(sources: list[SourceConfig]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    valid_records = []
    error_records = []

    for source in sources:
        if source.type != "fixture":
            raise ValueError(f"Unsupported source type: {source.type}")
        for raw in load_fixture(source.path):
            record = normalize_record(source, raw)
            errors = validate_record(record)
            if errors:
                error_records.append({"source": source.name, "record": record, "errors": errors})
            else:
                valid_records.append(record)

    return valid_records, error_records


def write_csv(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REQUIRED_FIELDS)
        writer.writeheader()
        writer.writerows(records)


def write_summary(records: list[dict[str, Any]], errors: list[dict[str, Any]], path: Path) -> None:
    total_value = sum(float(record["value"]) for record in records)
    lines = [
        "# Extraction Summary",
        "",
        f"Valid records: {len(records)}",
        f"Error records: {len(errors)}",
        f"Total value: {total_value:.2f}",
    ]
    if errors:
        lines.append("")
        lines.append("## Errors")
        for error in errors:
            lines.append(f"- {error['source']}: {', '.join(error['errors'])}")
    path.write_text("\n".join(lines), encoding="utf-8")


def run(sources_path: Path, output_path: Path) -> dict[str, Path]:
    records, errors = extract_records(load_sources(sources_path))
    write_csv(records, output_path)
    summary_path = output_path.with_suffix(".summary.md")
    write_summary(records, errors, summary_path)
    return {"csv": output_path, "summary": summary_path}


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the data extraction demo.")
    parser.add_argument("--sources", required=True, help="Path to source configuration JSON.")
    parser.add_argument("--output", required=True, help="Path to output CSV.")
    args = parser.parse_args()

    outputs = run(Path(args.sources), Path(args.output))
    for name, path in outputs.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()

