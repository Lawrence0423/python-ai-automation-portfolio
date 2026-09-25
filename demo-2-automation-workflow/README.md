# Demo 2: Automation Workflow Assistant

This demo shows a safe lead-to-CRM automation workflow. It scores incoming leads, creates a human review queue, prepares CRM payloads, and generates follow-up drafts without sending messages automatically.

## Best-fit freelance projects

- "Automate our lead qualification workflow"
- "Connect web form leads to CRM"
- "Replace a manual spreadsheet process"
- "Build a Make.com or Zapier-style MVP in Python"

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

## Deliverables this pattern supports

- CSV, webhook, or API intake
- Scoring rules and priority classification
- Review queue for human approval
- CRM payload generation
- Draft follow-up messages
- Workflow logs and handoff notes

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

## Acceptance criteria for a client version

- Each incoming record receives a clear priority and reason.
- CRM payloads match the client's API schema.
- Follow-up drafts stay in human review until approved.
- Errors are logged instead of silently dropped.
- The first milestone covers one complete workflow before expansion.

## What would change for a real client

- Replace sample CSV intake with a webhook, form export, CRM API, or database.
- Add authentication and secret management.
- Add retries and alerting for failed API calls.
- Add a small dashboard if the client needs manual review.
- Add scheduled runs if the workflow is batch-based.
