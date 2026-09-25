import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module at {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_chatbot() -> None:
    demo = ROOT / "demo-1-ai-chatbot"
    knowledge = load_module("knowledge_demo", demo / "app" / "knowledge.py")
    items = knowledge.load_knowledge(demo / "app" / "data" / "faqs.json")
    result = knowledge.find_best_answer("I need to return my order", items)
    assert result.item is not None
    assert result.item.id == "return-policy"


def check_workflow() -> None:
    demo = ROOT / "demo-2-automation-workflow"
    workflow = load_module("workflow_demo", demo / "app" / "workflow.py")
    lead = workflow.Lead(
        company="Urban Medspa",
        contact_name="Noah Smith",
        email="noah@example.com",
        source="website",
        employees=32,
        interest="voice_agent",
        notes="Wants front desk automation and booking follow-up",
    )
    item = workflow.score_lead(lead)
    assert item.priority == "high"
    payload = workflow.build_crm_payload(item)
    assert payload["status"] == "needs_human_review"


def check_extractor() -> None:
    demo = ROOT / "demo-3-data-extraction"
    extractor = load_module("extractor_demo", demo / "extractor.py")
    records, errors = extractor.extract_records(extractor.load_sources(demo / "sources.json"))
    assert len(records) == 4
    assert errors == []


def main() -> None:
    check_chatbot()
    check_workflow()
    check_extractor()
    print("All portfolio checks passed.")


if __name__ == "__main__":
    main()

