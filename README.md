# Python AI Automation Portfolio

Practical demo projects for freelance work in AI chatbots, workflow automation, API integration, and data reporting.

This repository is built as a client-facing portfolio. Each demo is small enough to understand quickly, but structured like real client work: clear inputs, predictable outputs, tests or checks, and documentation.

## What I Build

I build Python and AI automation tools for small businesses, agencies, and internal teams:

- Customer support chatbots and FAQ assistants
- OpenAI API integrations with safe fallback behavior
- CRM and lead workflow automation
- API data extraction and CSV or Excel-ready reports
- Production-style MVPs with documentation and handoff notes

## Portfolio Demos

| Demo | Best for | What it proves |
| --- | --- | --- |
| [AI Customer Support Chatbot](demo-1-ai-chatbot) | Chatbot, FAQ bot, support automation, OpenAI integration | FastAPI backend, knowledge base matching, structured API responses, safe fallback |
| [Automation Workflow Assistant](demo-2-automation-workflow) | CRM automation, lead review, workflow MVPs | Lead scoring, human review queue, CRM-ready JSON, follow-up drafts |
| [Data Extraction and Reporting Toolkit](demo-3-data-extraction) | API extraction, CSV reporting, data cleanup | Adapter-based data ingestion, normalization, validation, report export |

## Quick Verification

Run the no-dependency checks:

```bash
python run_checks.py
```

Expected result:

```text
All portfolio checks passed.
```

Run the workflow demos:

```bash
cd demo-2-automation-workflow
python workflow_cli.py --input app/data/sample_leads.csv --output out
```

```bash
cd demo-3-data-extraction
python extractor.py --sources sources.json --output out/report.csv
```

## Chatbot Demo

The chatbot demo uses FastAPI. To run it locally:

```bash
cd demo-1-ai-chatbot
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Docker is also available:

```bash
cd demo-1-ai-chatbot
docker build -t support-chatbot-demo .
docker run --rm -p 8000:8000 support-chatbot-demo
```

## Proposal Assets

- [Proposal templates](proposal_templates.md)
- [Client questionnaire](client_questionnaire.md)
- [Delivery notes](DELIVERY_NOTES.md)
- [Portfolio landing page](index.html)
- [How to use this portfolio for proposals](docs/how-to-use-for-proposals.md)
- [Milestone playbook](docs/milestone-playbook.md)
- [Profile bio drafts](docs/profile-bio.md)

## Safe Automation Policy

These demos avoid:

- Paywall bypass
- Login bypass
- Unauthorized scraping
- Credential harvesting
- Fake account creation
- Mass unsolicited messaging
- Platform rule evasion

For real client work, I use official APIs, client-owned data, approved exports, or public data where collection is allowed.

## Client-Facing Summary

> I build practical Python and AI automation systems: customer support chatbots, API integrations, workflow automation, and data reporting tools. I focus on scoped MVPs that are easy to test, document, and hand off.

## Suggested First Milestone

For most projects, the safest first milestone is:

1. Confirm source data, API access, and acceptance criteria.
2. Build a working MVP around one end-to-end workflow.
3. Add tests or verification scripts.
4. Deliver setup instructions and handoff notes.
5. Expand only after the first workflow is approved.

## Repository Quality

This repository includes:

- No-dependency smoke checks in `run_checks.py`
- GitHub Actions workflow in `.github/workflows/portfolio-checks.yml`
- Docker support for the chatbot demo
- PowerShell and shell helper scripts in `scripts/`
- Clear safety boundaries for automation work
