# Data Model: Enhanced Console Todo Application

## Entities

### Task
Represents a single todo item with the following attributes:

- **id**: UUID/string (unique identifier, automatically assigned)
- **title**: string (required, non-empty)
- **description**: string (optional, can be empty)
- **completed**: boolean (default: false)
- **created_at**: datetime (automatically assigned when created)

### TaskList
In-memory collection of Task objects:

- **tasks**: List[Task] (collection of Task objects)
- **next_id**: integer (auto-incrementing ID counter for new tasks)

## Validation Rules

### Task Validation
- Title must be non-empty string (min 1 character)
- ID must be unique within the TaskList
- Completed status must be a boolean value
- Created timestamp must be a valid datetime

### TaskList Validation
- No duplicate IDs allowed
- Maximum of 1000 tasks in memory (enforced limit)
- Task operations must reference existing task IDs

## State Transitions

### Task State Transitions
- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete

## Relationships

### TaskList contains Tasks
- One TaskList contains many Tasks
- Tasks exist only within the context of a TaskList
- When TaskList is cleared (app exit), all Tasks are destroyed

## Constraints

- Task IDs must be unique within the application session
- TaskList maintains insertion order by default
- In-memory only - no persistence between sessions
- Tasks are immutable except for completion status and updates to title/description