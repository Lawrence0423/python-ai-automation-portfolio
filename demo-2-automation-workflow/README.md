# Demo 2: Automation Workflow Assistant

This demo shows a safe lead-to-CRM automation workflow. It scores incoming leads, creates a human review queue, prepares CRM payloads, and generates follow-up drafts without sending messages automatically.

## Client problems this demo supports

- CRM automation
- Lead qualification
- Internal review queues
- Make/Zapier replacement MVP
- Human-approved AI workflow
- API integration planning

## Features

- CSV lead intake
- Deterministic scoring rules
- Review queue for human approval
- CRM-ready JSON payloads
- Follow-up draft generation
- Audit-friendly workflow output

## Run locally

```bash
python workflow_cli.py --input app/data/sample_leads.csv --output out
```

The command writes:

- `out/review_queue.json`
- `out/crm_payloads.json`
- `out/followups.md`

## Why this is safe

The demo does not scrape social platforms, send unsolicited messages, or bypass platform controls. It shows a realistic pattern for approved business data and human-in-the-loop review.

## Proposal snippet

I can build this as a reliable workflow automation MVP: intake approved lead data, score and classify each record, prepare CRM-ready payloads, generate draft follow-ups, and keep a human approval step before anything is sent. I have a small demo of this pattern that can be adapted to your CRM and API documentation.

