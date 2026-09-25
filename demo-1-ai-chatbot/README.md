# Demo 1: AI Customer Support Chatbot

This demo shows a customer support chatbot built with Python and FastAPI. It answers from an approved FAQ knowledge base first, then can optionally use an AI fallback if an `OPENAI_API_KEY` is configured.

## Best-fit freelance projects

- "Upgrade our existing Python chatbot"
- "Add an AI FAQ assistant to our website"
- "Connect a chatbot to order or ticket APIs"
- "Build a support bot MVP with OpenAI"

## Client problems this demo supports

- FAQ chatbot for a website
- Customer support assistant
- Knowledge base chatbot
- Order or ticket routing assistant
- OpenAI API integration with guardrails

## Features

- FastAPI backend
- Simple browser chat interface
- Knowledge base matching
- Structured response payloads
- Safe fallback message when confidence is low
- Optional OpenAI fallback placeholder
- Unit tests for matching behavior

## Deliverables this pattern supports

- Backend API for chat requests
- Website chat widget or embeddable frontend
- Knowledge base ingestion
- Admin-approved FAQ answers
- Fallback routing to human support
- Setup guide and handoff documentation

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Or use the Windows helper:

```powershell
.\run_local.ps1
```

Or use Docker:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000
```

## API example

```bash
curl -X POST http://127.0.0.1:8000/chat ^
  -H "Content-Type: application/json" ^
  -d "{\"message\":\"How do I return an order?\"}"
```

## Proposal snippet

I have a small Python support chatbot demo that shows the same delivery pattern I would use for your project: approved knowledge base answers first, structured API responses, fallback handling, and a simple web interface. For your codebase, I would connect this pattern to your real order, ticket, or account APIs.

## Acceptance criteria for a client version

- The bot answers approved FAQ questions with consistent wording.
- Low-confidence questions route to a safe fallback or human review.
- API responses include source and confidence metadata.
- Setup instructions allow the client to run the project locally.
- Sensitive customer data is not sent to an AI provider without approval.

## What would change for a real client

- Replace sample FAQs with the client's real knowledge base
- Add authentication if private account data is used
- Integrate order, ticket, CRM, or helpdesk APIs
- Add logging and analytics
- Add deployment scripts for the client's server
