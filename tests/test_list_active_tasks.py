import pytest
import json
from pathlib import Path
from scripts.list_active_tasks import list_active_tasks

def test_list_active_tasks(tmp_path, capsys):
    # Create a temporary JSON file
    tasks_file = tmp_path / "agent_tasks.json"
    tasks_data = [
        {"id": "t1", "title": "Task 1", "status": "done"},
        {"id": "t2", "title": "Task 2", "status": "todo"},
        {"id": "t3", "title": "Task 3", "status": "in-progress"},
        {"id": "t4", "title": "Task 4", "status": "todo"},
    ]
    tasks_file.write_text(json.dumps(tasks_data))

    # Run the function
    list_active_tasks(str(tasks_file))

    # Check output
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    assert output == ["Task 2", "Task 4"]

def test_list_active_tasks_file_not_found(capsys):
    list_active_tasks("nonexistent.json")
    captured = capsys.readouterr()
    assert "Error: File 'nonexistent.json' does not exist." in captured.err

def test_list_active_tasks_invalid_json(tmp_path, capsys):
    tasks_file = tmp_path / "invalid.json"
    tasks_file.write_text("{invalid json}")
    list_active_tasks(str(tasks_file))
    captured = capsys.readouterr()
    assert "Error: Failed to parse JSON" in captured.err

def test_list_active_tasks_not_array(tmp_path, capsys):
    tasks_file = tmp_path / "not_array.json"
    tasks_file.write_text("{\"key\": \"value\"}")
    list_active_tasks(str(tasks_file))
    captured = capsys.readouterr()
    assert "Error: The root of the JSON file must be an array. Got dict." in captured.err
