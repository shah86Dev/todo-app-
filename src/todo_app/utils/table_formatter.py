"""
Rich table formatter for the console todo application.
Provides formatted table output for task lists using Rich.
"""
from rich.table import Table
from rich.text import Text
from typing import List

from src.todo_app.models.task import Task


def format_tasks_table(tasks: List[Task], title: str = "Todo Tasks") -> Table:
    """
    Format a list of tasks into a Rich table with colored output and status indicators.

    Args:
        tasks: List of Task objects to display
        title: Title for the table (default: "Todo Tasks")

    Returns:
        Rich Table object with formatted tasks
    """
    # Create a Rich table with headers
    table = Table(title=title, title_style="bold blue", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=5)
    table.add_column("Title", style="bold", min_width=15)
    table.add_column("Description", min_width=20)
    table.add_column("Status", justify="center", width=12)

    # Add rows for each task
    for task in tasks:
        # Determine status indicator
        status_icon = "[Done]" if task.completed else "[Pending]"
        status_color = "green" if task.completed else "red"
        status_text = Text(status_icon, style=status_color, justify="center")

        # Add row to table
        table.add_row(
            str(task.id),
            task.title,
            task.description if task.description else "[italic dim]No description[/italic dim]",
            status_text
        )

    return table