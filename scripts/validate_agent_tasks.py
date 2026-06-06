import json
import sys
from pathlib import Path


def validate_tasks(filepath: str) -> bool:
    path = Path(filepath)

    if not path.exists():
        print(f"Error: File '{filepath}' does not exist.")
        return False

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"Error: Failed to parse JSON: {error}")
        return False

    if not isinstance(data, list):
        print(f"Error: The root of the JSON file must be an array. Got {type(data).__name__}.")
        return False

    for index, task in enumerate(data):
        if not isinstance(task, dict):
            print(f"Error: Task #{index} must be an object.")
            return False

        required_fields = ["id", "title", "status"]
        for field in required_fields:
            if field not in task:
                print(f"Error: Task #{index} is missing required field: {field}")
                return False

    print(f"Success: '{filepath}' is valid.")
    return True


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "agent_tasks.json"
    sys.exit(0 if validate_tasks(target) else 1)
