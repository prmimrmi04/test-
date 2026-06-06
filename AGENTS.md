# Agent Instructions

This repository contains tools and tasks for AI agents.

## Files and Directories

- `agent_tasks.json`: A JSON file containing a list of tasks for agents to perform. The structure must be a JSON array.
- `scripts/validate_agent_tasks.py`: A Python script used to validate the structure of `agent_tasks.json`.
- `requirements.txt`: Python dependencies for the project.
- `tests/`: Directory containing tests for the project's scripts.

## Guidelines

- All new scripts should have corresponding tests added in the `tests/` directory.
- Before committing, ensure all tests pass.
- Modifications to `agent_tasks.json` must leave it as a valid JSON array.
