# CLI Contract: Hackathon Todo CLI Application

## Command Interface

### Add Command
```
todo add --title <title> [--description <description>]
```

- **Purpose**: Add a new task
- **Parameters**:
  - `title` (required): Task title (string, min 1 char)
  - `description` (optional): Task description (string)
- **Returns**: Success message with assigned task ID
- **Errors**: Validation error if title is empty

### List Command
```
todo list [--all | --completed | --pending]
```

- **Purpose**: Display tasks in formatted Rich table
- **Parameters**:
  - `--all` (default): Show all tasks
  - `--completed`: Show only completed tasks
  - `--pending`: Show only pending tasks
- **Returns**: Rich-formatted table with ID, Title, Description, Status
- **Errors**: None (shows empty state if no tasks)

### Update Command
```
todo update --id <id> [--title <title>] [--description <description>]
```

- **Purpose**: Update an existing task
- **Parameters**:
  - `id` (required): Task ID to update
  - `title` (optional): New title
  - `description` (optional): New description
- **Returns**: Success message
- **Errors**: Task not found error if ID doesn't exist

### Complete Command
```
todo complete --id <id> [--status <true|false>]
```

- **Purpose**: Mark task as complete/incomplete
- **Parameters**:
  - `id` (required): Task ID to update
  - `status` (optional, default: true): Completion status
- **Returns**: Success message
- **Errors**: Task not found error if ID doesn't exist

### Delete Command
```
todo delete --id <id>
```

- **Purpose**: Remove a task
- **Parameters**:
  - `id` (required): Task ID to delete
- **Returns**: Success message
- **Errors**: Task not found error if ID doesn't exist

## Output Format

All commands return structured output using Rich formatting:
- Success messages in green
- Error messages in red
- Task lists as formatted tables with Rich
- Status indicators using Rich's color and text formatting

## Error Handling

- Invalid command: Shows help text
- Missing required parameter: Shows error and usage
- Invalid task ID: Shows "Task not found" error
- Validation errors: Shows specific validation message