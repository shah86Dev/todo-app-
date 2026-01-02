# Data Model: Console Todo Application

**Feature**: 001-console-todo-app
**Created**: 2026-01-02
**Author**: Main System Architect

## 1. Task Entity

### Fields
- **id** (int)
  - Type: Integer
  - Constraints: Unique, Auto-generated
  - Description: Unique identifier for the task
  - Required: Yes

- **title** (str)
  - Type: String
  - Constraints: Not empty, Max length 200 characters
  - Description: Brief title of the task
  - Required: Yes

- **description** (str)
  - Type: String
  - Constraints: Optional, Max length 1000 characters
  - Description: Detailed description of the task
  - Required: No

- **completed** (bool)
  - Type: Boolean
  - Default: False
  - Description: Completion status of the task
  - Required: Yes

- **created_at** (datetime)
  - Type: DateTime
  - Constraints: Auto-generated on creation
  - Description: Timestamp when task was created
  - Required: Yes

### Validation Rules
1. **Title Validation**:
   - Must not be empty or contain only whitespace
   - Must be between 1 and 200 characters
   - Should not contain only special characters without any alphanumeric content

2. **ID Validation**:
   - Must be unique within the system
   - Auto-generated using incrementing integer sequence

3. **Description Validation**:
   - Optional field
   - If provided, must be between 1 and 1000 characters

4. **Status Validation**:
   - Must be either True (completed) or False (incomplete)

### State Transitions
- **Incomplete → Complete**: When user marks task as complete
- **Complete → Incomplete**: When user marks task as incomplete

## 2. Task Collection Structure

### In-Memory Storage
- **Structure**: Dictionary with integer keys and Task objects as values
- **Type**: `dict[int, Task]`
- **Access Pattern**: O(1) lookup by ID

### ID Generation
- **Strategy**: Auto-incrementing integer starting from 1
- **Implementation**: Track next available ID using a counter
- **Collision Handling**: Check if ID exists before assignment

## 3. Relationships

### Task to TaskManager
- **Relationship**: One TaskManager manages multiple Tasks
- **Cardinality**: One-to-Many (1:M)
- **Implementation**: TaskManager contains the dictionary of Task objects

## 4. Data Integrity Constraints

### Uniqueness
- Each Task must have a unique ID within the system
- No two tasks can share the same ID

### Referential Integrity
- All operations on tasks must reference valid task IDs
- Operations on non-existent tasks must raise appropriate errors

### Domain Constraints
- Completed field must be a boolean value
- Title and description must conform to character limits
- Created timestamp must be set at task creation time

## 5. Data Access Patterns

### Read Operations
- **Get Single Task**: Retrieve task by ID (O(1) complexity)
- **List All Tasks**: Retrieve all tasks in the system (O(n) complexity)

### Write Operations
- **Create Task**: Add new task with auto-generated ID
- **Update Task**: Modify existing task properties
- **Delete Task**: Remove task from the system

## 6. Validation Implementation

### At Model Level
```python
class Task:
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        self.id = self._validate_id(id)
        self.title = self._validate_title(title)
        self.description = self._validate_description(description)
        self.completed = completed
        self.created_at = datetime.now()

    def _validate_id(self, id: int) -> int:
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be a positive integer")
        return id

    def _validate_title(self, title: str) -> str:
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")
        if len(title.strip()) > 200:
            raise ValueError("Title cannot exceed 200 characters")
        return title.strip()

    def _validate_description(self, description: str) -> str:
        if description and len(description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")
        return description
```

### At Service Level
- Validate that task IDs exist before operations
- Validate operation parameters before execution
- Handle edge cases appropriately

## 7. Serialization Considerations

### Current Phase (Phase I)
- No serialization required (in-memory only)
- Objects exist only during application runtime

### Future Phases
- JSON serialization may be needed for persistence
- Format: Standard JSON with field names matching model attributes