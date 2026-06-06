import os
import json
import pytest
import sys

# Add scripts directory to path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.validate_agent_tasks import validate_tasks

def create_temp_json(tmp_path, data, is_raw=False):
    filepath = tmp_path / "temp.json"
    with open(filepath, "w") as f:
        if is_raw:
            f.write(data)
        else:
            json.dump(data, f)
    return str(filepath)

def test_valid_json_array(tmp_path):
    filepath = create_temp_json(tmp_path, [])
    assert validate_tasks(filepath) == True

def test_valid_json_array_with_data(tmp_path):
    filepath = create_temp_json(tmp_path, [{"id": 1, "task": "test"}])
    assert validate_tasks(filepath) == True

def test_invalid_json_object(tmp_path):
    filepath = create_temp_json(tmp_path, {})
    assert validate_tasks(filepath) == False

def test_invalid_json_string(tmp_path):
    filepath = create_temp_json(tmp_path, "not an array")
    assert validate_tasks(filepath) == False

def test_invalid_json_syntax(tmp_path):
    filepath = create_temp_json(tmp_path, "[invalid json}", is_raw=True)
    assert validate_tasks(filepath) == False

def test_file_not_found():
    assert validate_tasks("non_existent_file.json") == False
