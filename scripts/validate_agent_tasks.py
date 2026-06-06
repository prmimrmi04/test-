import json
import sys
import os

def validate_tasks(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return False

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print(f"Error: The root of the JSON file must be an array (list). Got {type(data).__name__} instead.")
            return False

        return True

    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON: {e}")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    filepath = "agent_tasks.json"
    if len(sys.argv) > 1:
        filepath = sys.argv[1]

    if validate_tasks(filepath):
        print(f"Success: '{filepath}' is a valid JSON array.")
        sys.exit(0)
    else:
        sys.exit(1)
