# Demo 3: Data Extraction and Reporting Toolkit

This demo shows a safe data extraction pipeline. It reads approved JSON sources, normalizes records into a consistent schema, validates required fields, and exports a CSV report.

## Client problems this demo supports

- API data extraction
- Multi-source data collection
- CSV or Excel-ready reporting
- Data cleanup and normalization
- Scheduled reporting MVP

## Features

- Adapter-based source configuration
- Local fixture mode for repeatable demos
- Field normalization
- Required field validation
- CSV export
- Summary report

## Run locally

```bash
python extractor.py --sources sources.json --output out/report.csv
```

The demo uses local JSON fixtures so it runs without network access. In a real project, each fixture adapter can be replaced with an approved API request.

## Proposal snippet

I can build this as a reliable data extraction pipeline: connect to approved APIs or client-provided exports, normalize the fields, validate missing values, and deliver CSV or Excel-ready reports. I avoid paywall bypassing or unauthorized scraping; if a source requires login, I would use an approved API, export, or client-authorized access method.

## What would change for a real client

- Replace local fixtures with approved API calls
- Add pagination and retry behavior
- Add scheduled runs
- Export to Excel, Google Sheets, database, or API
- Add logging and alerts for failed sources

