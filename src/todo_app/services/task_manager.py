"""
TaskManager service for the console todo application.
Handles all business logic for task operations with file-based persistence.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

from src.todo_app.models.task import Task


class TaskManager:
    """
    Manages all task operations including adding, updating, deleting, and marking tasks.
    Uses file-based storage for tasks to persist between sessions.
    """
    def __init__(self, storage_file="tasks.json"):
        """Initialize the TaskManager with file-based storage."""
        self.storage_file = storage_file
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1
        self._load_tasks()

    def _load_tasks(self):
        """Load tasks from the storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for task_data in data.get('tasks', []):
                        # Convert dict back to Task object
                        task = Task(
                            id=task_data['id'],
                            title=task_data['title'],
                            description=task_data['description'],
                            completed=task_data['completed']
                        )
                        # Convert created_at string back to datetime
                        if task_data.get('created_at'):
                            task.created_at = datetime.fromisoformat(task_data['created_at'])
                        self._tasks[task.id] = task
                    self._next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError, ValueError):
                # If there's an error loading, start fresh
                self._tasks = {}
                self._next_id = 1

    def _save_tasks(self):
        """Save tasks to the storage file."""
        tasks_data = []
        for task in self._tasks.values():
            task_dict = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'created_at': task.created_at.isoformat() if task.created_at else None
            }
            tasks_data.append(task_dict)

        data = {
            'tasks': tasks_data,
            'next_id': self._next_id
        }

        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def _get_next_id(self) -> int:
        """Get the next available task ID."""
        while self._next_id in self._tasks:
            self._next_id += 1
        return self._next_id

    def add_task(self, title: str, description: str = "") -> int:
        """
        Create a new task with unique ID.

        Args:
            title: The task title
            description: The task description (optional)

        Returns:
            The ID of the created task

        Raises:
            ValueError: If title is invalid
        """
        task_id = self._get_next_id()
        task = Task(id=task_id, title=title, description=description)
        self._tasks[task_id] = task
        self._next_id = task_id + 1  # Update next ID to be after current
        self._save_tasks()
        return task_id

    def get_task(self, task_id: int) -> Task:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task object

        Raises:
            KeyError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID {task_id} does not exist")
        return self._tasks[task_id]

    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """
        Update the title and description of an existing task.

        Args:
            task_id: The ID of the task to update
            title: The new title
            description: The new description

        Returns:
            True if update was successful, False if task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        # Create updated task with same ID but new properties
        updated_task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=self._tasks[task_id].completed,
            created_at=self._tasks[task_id].created_at
        )
        self._tasks[task_id] = updated_task
        self._save_tasks()
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if deletion was successful, False if task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        self._save_tasks()
        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if operation was successful, False if task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        self._tasks[task_id].completed = True
        self._save_tasks()
        return True

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if operation was successful, False if task doesn't exist
        """
        if task_id not in self._tasks:
            return False

        self._tasks[task_id].completed = False
        self._save_tasks()
        return True

    def list_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the system.

        Returns:
            List of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def list_completed_tasks(self) -> List[Task]:
        """
        Retrieve only completed tasks in the system.

        Returns:
            List of completed Task objects, sorted by ID
        """
        completed_tasks = [task for task in self._tasks.values() if task.completed]
        return sorted(completed_tasks, key=lambda task: task.id)

    def list_pending_tasks(self) -> List[Task]:
        """
        Retrieve only pending (incomplete) tasks in the system.

        Returns:
            List of pending Task objects, sorted by ID
        """
        pending_tasks = [task for task in self._tasks.values() if not task.completed]
        return sorted(pending_tasks, key=lambda task: task.id)

    def get_next_id(self) -> int:
        """
        Get the next available ID without creating a task.

        Returns:
            The next available task ID
        """
        return self._get_next_id()