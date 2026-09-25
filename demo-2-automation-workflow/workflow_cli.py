import argparse
from pathlib import Path

from app.workflow import run_workflow


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the automation workflow demo.")
    parser.add_argument("--input", required=True, help="Path to input CSV.")
    parser.add_argument("--output", required=True, help="Directory for generated outputs.")
    args = parser.parse_args()

    outputs = run_workflow(Path(args.input), Path(args.output))
    for name, path in outputs.items():
        print(f"{name}: {path}")


if __name__ == "__main__":
    main()

