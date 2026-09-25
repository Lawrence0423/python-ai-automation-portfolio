import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path


HIGH_VALUE_INTERESTS = {"chatbot", "crm_sync", "voice_agent", "automation"}


@dataclass(frozen=True)
class Lead:
    company: str
    contact_name: str
    email: str
    source: str
    employees: int
    interest: str
    notes: str


@dataclass(frozen=True)
class ReviewItem:
    lead: Lead
    score: int
    priority: str
    reason: str
    recommended_next_step: str


def read_leads(path: Path) -> list[Lead]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            Lead(
                company=row["company"],
                contact_name=row["contact_name"],
                email=row["email"],
                source=row["source"],
                employees=int(row["employees"]),
                interest=row["interest"],
                notes=row["notes"],
            )
            for row in reader
        ]


def score_lead(lead: Lead) -> ReviewItem:
    score = 0
    reasons = []

    if lead.source in {"website", "referral"}:
        score += 25
        reasons.append("strong source")

    if lead.employees >= 20:
        score += 25
        reasons.append("team size suggests budget")

    if lead.interest in HIGH_VALUE_INTERESTS:
        score += 35
        reasons.append("high-value automation need")

    if any(word in lead.notes.lower() for word in ["booking", "crm", "front desk", "order"]):
        score += 15
        reasons.append("specific workflow mentioned")

    if score >= 75:
        priority = "high"
        next_step = "Send tailored discovery questions and request API or workflow details."
    elif score >= 45:
        priority = "medium"
        next_step = "Ask clarifying questions before estimating."
    else:
        priority = "low"
        next_step = "Send a short qualification reply before spending time on a proposal."

    return ReviewItem(
        lead=lead,
        score=score,
        priority=priority,
        reason=", ".join(reasons) if reasons else "limited fit signals",
        recommended_next_step=next_step,
    )


def build_crm_payload(item: ReviewItem) -> dict:
    lead = item.lead
    return {
        "company": lead.company,
        "contact": {
            "name": lead.contact_name,
            "email": lead.email,
        },
        "source": lead.source,
        "interest": lead.interest,
        "score": item.score,
        "priority": item.priority,
        "notes": lead.notes,
        "status": "needs_human_review",
    }


def build_followup(item: ReviewItem) -> str:
    lead = item.lead
    return (
        f"Subject: Re: {lead.interest.replace('_', ' ').title()} request\n\n"
        f"Hi {lead.contact_name},\n\n"
        f"Thanks for reaching out about {lead.interest.replace('_', ' ')}. "
        "Before I estimate the work, I would like to understand your current workflow, "
        "the systems that need to connect, and what a successful first demo should show.\n\n"
        "Best,\n"
    )


def run_workflow(input_path: Path, output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    review_items = [score_lead(lead) for lead in read_leads(input_path)]
    crm_payloads = [build_crm_payload(item) for item in review_items]
    followups = [build_followup(item) for item in review_items if item.priority != "low"]

    review_path = output_dir / "review_queue.json"
    crm_path = output_dir / "crm_payloads.json"
    followup_path = output_dir / "followups.md"

    review_path.write_text(
        json.dumps([asdict(item) for item in review_items], indent=2),
        encoding="utf-8",
    )
    crm_path.write_text(json.dumps(crm_payloads, indent=2), encoding="utf-8")
    followup_path.write_text("\n---\n".join(followups), encoding="utf-8")

    return {
        "review_queue": review_path,
        "crm_payloads": crm_path,
        "followups": followup_path,
    }

