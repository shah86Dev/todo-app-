"""
Task model for the console todo application.
Defines the data structure for todo tasks with validation.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, and completion status.
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Validate task attributes after initialization."""
        if self.created_at is None:
            self.created_at = datetime.now()

        # Validate ID
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")

        # Validate title
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty or contain only whitespace")
        if len(self.title.strip()) > 200:
            raise ValueError("Title cannot exceed 200 characters")

        # Validate description
        if self.description and len(self.description) > 1000:
            raise ValueError("Description cannot exceed 1000 characters")

        # Update title to stripped version
        self.title = self.title.strip()