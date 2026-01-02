# Quickstart Guide: Console Todo Application

**Feature**: 001-console-todo-app
**Created**: 2026-01-02
**Author**: Main System Architect

## Getting Started

### Prerequisites
- Python 3.13 or higher
- No additional packages required (uses only standard library)

### Setup
1. Clone or download the repository
2. Navigate to the project root directory
3. Ensure Python 3.13+ is installed and accessible from command line

### Running the Application
```bash
python src/main.py
```

## Application Commands

Once the application starts, you'll see a menu with the following options:

### Adding a Task
```
add "Your task title" "Optional task description"
```
- Example: `add "Buy groceries" "Milk, bread, eggs"`
- The title is required and cannot be empty
- The description is optional

### Listing All Tasks
```
list
```
or
```
ls
```
- Shows all tasks with their ID, title, description, and completion status

### Updating a Task
```
update ID "New title" "New description"
```
- Example: `update 1 "Updated task title" "Updated description"`
- All parameters are required
- Use the task's ID as shown in the list command

### Deleting a Task
```
delete ID
```
- Example: `delete 1`
- Permanently removes the task from the system

### Marking a Task as Complete
```
complete ID
```
- Example: `complete 1`
- Changes the task status to completed

### Marking a Task as Incomplete
```
incomplete ID
```
- Example: `incomplete 1`
- Changes the task status to incomplete

### Getting Help
```
help
```
- Displays the list of available commands

### Exiting the Application
```
exit
```
or
```
quit
```
- Terminates the application
- All tasks will be lost when the application exits (in-memory storage)

## Example Workflow

1. Start the application: `python src/main.py`
2. Add a task: `add "Complete project" "Finish the todo app implementation"`
3. List tasks: `list`
4. Mark task as complete: `complete 1`
5. Update the task: `update 1 "Project completed" "Successfully finished the todo app"`
6. View updated list: `list`
7. Exit: `exit`

## Error Handling

The application provides clear error messages for invalid operations:
- Invalid command: "Unknown command. Type 'help' for available commands."
- Invalid task ID: "Task with ID X does not exist."
- Empty title: "Task title cannot be empty."
- Invalid command format: "Invalid command format. See 'help' for usage."

## Architecture Overview

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
├── tests/
├── specs/
│   └── 001-console-todo-app/
└── README.md
```