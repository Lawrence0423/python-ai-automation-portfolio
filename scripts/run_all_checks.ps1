$ErrorActionPreference = "Stop"

function Get-PythonCommand {
  if (Get-Command python -ErrorAction SilentlyContinue) {
    return "python"
  }
  if (Get-Command py -ErrorAction SilentlyContinue) {
    return "py"
  }
  throw "Python was not found. Install Python 3.12+ or add python to PATH."
}

$Python = Get-PythonCommand

Write-Host "Running portfolio checks..."
& $Python run_checks.py

Write-Host "Running workflow demo..."
Push-Location demo-2-automation-workflow
& $Python workflow_cli.py --input app/data/sample_leads.csv --output out
Pop-Location

Write-Host "Running data extraction demo..."
Push-Location demo-3-data-extraction
& $Python extractor.py --sources sources.json --output out/report.csv
Pop-Location

Write-Host "All checks completed."
