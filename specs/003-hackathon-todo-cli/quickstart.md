# Quickstart: Hackathon Todo CLI Application

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Setup

1. **Install UV** (if not already installed):
   ```bash
   # Installation method depends on your OS
   # For most systems:
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone or create the project**:
   ```bash
   # If starting fresh, create a new directory
   mkdir todo-app && cd todo-app
   ```

3. **Initialize the project with UV**:
   ```bash
   uv init
   ```

4. **Add required dependencies**:
   ```bash
   uv add typer rich
   ```

## Project Structure

```
todo-app/
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Dependency lock file
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── task.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── task_manager.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── main.py
│       └── utils/
│           ├── __init__.py
│           └── table_formatter.py
└── tests/
    ├── __init__.py
    ├── unit/
    └── integration/
```

## Running the Application

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Run the application**:
   ```bash
   uv run python -m src.todo_app.cli.main
   # Or if the project is configured as a package:
   uv run todo-app
   ```

## Available Commands

- `add` - Add a new task with title and optional description
- `list` - Display all tasks in a formatted Rich table
- `update` - Update an existing task's title or description
- `complete` - Mark a task as complete/incomplete
- `delete` - Remove a task by ID
- `help` - Show available commands

## Development

1. **Install with development dependencies**:
   ```bash
   uv sync --dev
   ```

2. **Run tests**:
   ```bash
   uv run pytest
   ```

3. **Format code** (if using formatters):
   ```bash
   uv run ruff format .
   ```

## Configuration

The application uses Typer's built-in configuration for command-line arguments and Rich for all console formatting. No additional configuration files are needed for basic operation.