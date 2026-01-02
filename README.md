# Console Todo Application

A simple command-line todo application built in Python for Phase I of the "Evolution of Todo" project.

## Features

- Add new todo tasks with title and description
- View all existing tasks with status indicators
- Update task title and description
- Delete tasks by ID
- Mark tasks as complete or incomplete
- Continuous command-line interface
- In-memory storage (tasks reset on application exit)

## Prerequisites

- Python 3.13 or higher

## Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is installed

## Usage

Run the application:
```bash
python src/main.py
```

### Available Commands

- `add "title" "description"` - Add a new task (description is optional)
- `list` or `ls` - List all tasks
- `update id "title" "description"` - Update a task
- `delete id` - Delete a task by ID
- `complete id` - Mark task as complete
- `incomplete id` - Mark task as incomplete
- `help` - Show help information
- `exit` or `quit` - Exit the application

### Example Workflow

1. Add a task: `add "Buy groceries" "Milk, bread, eggs"`
2. List tasks: `list`
3. Mark task as complete: `complete 1`
4. Update a task: `update 1 "Groceries purchased" "Bought milk, bread, and eggs"`
5. Exit: `exit`

## Architecture

The application follows a clean architecture pattern:

- **Models**: Task data structure with validation
- **Services**: TaskManager with business logic
- **Interfaces**: CLI controller for user interaction
- **Main**: Application entry point with execution loop

## File Structure

```
todo-app/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py
│   ├── interfaces/
│   │   ├── __init__.py
│   │   └── cli_controller.py
│   └── main.py
├── specs/
│   └── 001-console-todo-app/
└── README.md
```

## Phase Information

This is Phase I of the "Evolution of Todo" project, focusing on a console-based application with in-memory storage. Future phases will include web interfaces, persistence, and AI features.