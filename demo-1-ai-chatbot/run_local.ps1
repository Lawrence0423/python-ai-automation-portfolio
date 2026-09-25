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

if (-not (Test-Path ".venv")) {
  & $Python -m venv .venv
}

.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m uvicorn app.main:app --reload
