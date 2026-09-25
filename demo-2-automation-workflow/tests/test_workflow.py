from pathlib import Path

from app.workflow import Lead, build_crm_payload, score_lead


def test_high_value_lead_gets_high_priority():
    lead = Lead(
        company="Urban Medspa",
        contact_name="Noah Smith",
        email="noah@example.com",
        source="website",
        employees=32,
        interest="voice_agent",
        notes="Wants front desk automation and booking follow-up",
    )
    item = score_lead(lead)
    assert item.priority == "high"
    assert item.score >= 75


def test_low_signal_lead_stays_low_priority():
    lead = Lead(
        company="Tiny Shop",
        contact_name="Sam",
        email="sam@example.com",
        source="newsletter",
        employees=2,
        interest="unknown",
        notes="Asked a general pricing question",
    )
    item = score_lead(lead)
    assert item.priority == "low"


def test_crm_payload_requires_human_review():
    lead = Lead(
        company="Northwind Parts",
        contact_name="Liam Carter",
        email="liam@example.com",
        source="referral",
        employees=85,
        interest="crm_sync",
        notes="Wants order status synced into CRM",
    )
    payload = build_crm_payload(score_lead(lead))
    assert payload["status"] == "needs_human_review"
    assert payload["contact"]["email"] == "liam@example.com"

