import json
import sys
from pathlib import Path


def list_completed_tasks(filepath: str) -> None:
    path = Path(filepath)

    if not path.exists():
        print(f"Error: File '{filepath}' does not exist.", file=sys.stderr)
        return

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"Error: Failed to parse JSON: {error}", file=sys.stderr)
        return

    if not isinstance(data, list):
        print(f"Error: The root of the JSON file must be an array. Got {type(data).__name__}.", file=sys.stderr)
        return

    for task in data:
        if task.get("status") == "done" and "title" in task:
            print(task["title"])


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "agent_tasks.json"
    list_completed_tasks(target)
