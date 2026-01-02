"""
Main entry point for the enhanced console todo application.
Implements the Typer-based CLI with Rich formatted output.
"""
import typer
from rich.console import Console
from rich.prompt import Prompt
from rich import print
import sys
import os

# Add the src directory to the path so imports work when running from project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.todo_app.services.task_manager import TaskManager
from src.todo_app.utils.table_formatter import format_tasks_table

# Create a Typer app instance
app = typer.Typer(add_completion=False)
console = Console()

# Global task manager instance
task_manager = TaskManager()


@app.command()
def add(title: str = typer.Option(..., "--title", "-t", help="Task title"),
        description: str = typer.Option("", "--description", "-d", help="Task description")):
    """
    Add a new task with title and optional description.
    """
    try:
        task_id = task_manager.add_task(title, description)
        print(f"[green]Task added successfully with ID: {task_id}[/green]")
    except ValueError as e:
        print(f"[red]Error adding task: {str(e)}[/red]")


@app.command()
def list_tasks(all_tasks: bool = typer.Option(True, "--all", help="Show all tasks (default)"),
              completed: bool = typer.Option(False, "--completed", help="Show only completed tasks"),
              pending: bool = typer.Option(False, "--pending", help="Show only pending tasks")):
    """
    Display all tasks in a formatted table with Rich.
    """
    # Get tasks based on filter options
    if completed:
        tasks = task_manager.list_completed_tasks()
    elif pending:
        tasks = task_manager.list_pending_tasks()
    else:  # all_tasks or default
        tasks = task_manager.list_all_tasks()

    if not tasks:
        print("[yellow]No tasks found.[/yellow]")
        return

    # Create and display Rich table
    table = format_tasks_table(tasks)
    console.print(table)


@app.command()
def update(task_id: int = typer.Option(..., "--id", "-i", help="Task ID to update"),
          title: str = typer.Option(None, "--title", "-t", help="New task title"),
          description: str = typer.Option(None, "--description", "-d", help="New task description")):
    """
    Update an existing task's title or description.
    """
    # Get current task to use existing values if not provided
    try:
        current_task = task_manager.get_task(task_id)
    except KeyError:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")
        return

    # Use provided values or keep existing ones
    new_title = title if title is not None else current_task.title
    new_description = description if description is not None else current_task.description

    success = task_manager.update_task(task_id, new_title, new_description)
    if success:
        print(f"[green]Task {task_id} updated successfully[/green]")
    else:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")


@app.command()
def delete(task_id: int = typer.Option(..., "--id", "-i", help="Task ID to delete")):
    """
    Remove a task by its ID.
    """
    success = task_manager.delete_task(task_id)
    if success:
        print(f"[green]Task {task_id} deleted successfully[/green]")
    else:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")


@app.command()
def complete(task_id: int = typer.Option(..., "--id", "-i", help="Task ID to mark complete"),
            status: bool = typer.Option(True, "--status", help="Completion status (default: True)")):
    """
    Mark a task as complete or incomplete.
    """
    if status:
        success = task_manager.mark_complete(task_id)
        action = "complete"
    else:
        success = task_manager.mark_incomplete(task_id)
        action = "incomplete"

    if success:
        print(f"[green]Task {task_id} marked as {action}[/green]")
    else:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")


@app.command()
def incomplete(task_id: int = typer.Option(..., "--id", "-i", help="Task ID to mark incomplete")):
    """
    Mark a task as incomplete.
    """
    success = task_manager.mark_incomplete(task_id)
    if success:
        print(f"[green]Task {task_id} marked as incomplete[/green]")
    else:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Enhanced Console Todo Application with Typer and Rich formatting.
    """
    if ctx.invoked_subcommand is None:
        # If no subcommand is provided, show help
        print("[bold blue]Welcome to the Enhanced Console Todo Application![/bold blue]")
        print("[bold]Usage:[/bold] todo [OPTIONS] COMMAND [ARGS]...")
        print("\n[bold]Commands:[/bold]")
        print("  add      Add a new task")
        print("  list     Display all tasks in a formatted table")
        print("  update   Update an existing task")
        print("  delete   Remove a task by ID")
        print("  complete Mark a task as complete/incomplete")
        print("  incomplete Mark a task as incomplete")
        print("\n[bold]Examples:[/bold]")
        print("  todo add --title \"Buy groceries\" --description \"Milk, bread, eggs\"")
        print("  todo list --completed")
        print("  todo update --id 1 --title \"Updated title\"")
        print("  todo complete --id 1 --status True")


if __name__ == "__main__":
    app()