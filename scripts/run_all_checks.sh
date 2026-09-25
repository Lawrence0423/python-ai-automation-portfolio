#!/usr/bin/env bash
set -euo pipefail

echo "Running portfolio checks..."
python run_checks.py

echo "Running workflow demo..."
(
  cd demo-2-automation-workflow
  python workflow_cli.py --input app/data/sample_leads.csv --output out
)

echo "Running data extraction demo..."
(
  cd demo-3-data-extraction
  python extractor.py --sources sources.json --output out/report.csv
)

echo "All checks completed."

