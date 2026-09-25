# Demo 1: AI Customer Support Chatbot

This demo shows a customer support chatbot built with Python and FastAPI. It answers from an approved FAQ knowledge base first, then can optionally use an AI fallback if an `OPENAI_API_KEY` is configured.

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

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
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

## What would change for a real client

- Replace sample FAQs with the client's real knowledge base
- Add authentication if private account data is used
- Integrate order, ticket, CRM, or helpdesk APIs
- Add logging and analytics
- Add deployment scripts for the client's server

