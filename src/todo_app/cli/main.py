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
import json
from datetime import datetime

# Add the src directory to the path so imports work when running from project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.todo_app.services.task_manager import TaskManager
from src.todo_app.utils.table_formatter import format_tasks_table


def interactive_mode():
    """Run the application in interactive mode with continuous table display and numeric menu."""
    task_manager = TaskManager()
    console = Console()

    print("[bold blue]Welcome to the Interactive Todo Application![/bold blue]")

    while True:
        try:
            # Show current tasks in table format
            tasks = task_manager.list_all_tasks()
            if tasks:
                table = format_tasks_table(tasks)
                console.clear()
                console.print(table)
            else:
                console.clear()
                print("[yellow]No tasks found. Add some tasks![/yellow]")

            # Show numeric menu
            print("\n[i]Select an option:[/i]")
            print("  [1] Add new task")
            print("  [2] Update task")
            print("  [3] Delete task")
            print("  [4] Mark task complete")
            print("  [5] Mark task incomplete")
            print("  [6] Exit")

            choice = Prompt.ask("\nEnter your choice [1-6]")

            if choice == '1':
                title = Prompt.ask("Enter task title")
                description = Prompt.ask("Enter task description (optional)", default="")

                try:
                    task_id = task_manager.add_task(title, description)
                    print(f"[green]Task {task_id} added successfully![/green]")
                    input("Press Enter to continue...")
                except ValueError as e:
                    print(f"[red]Error: {str(e)}[/red]")
                    input("Press Enter to continue...")
            elif choice == '2':
                if not tasks:
                    print("[yellow]No tasks available to update.[/yellow]")
                    input("Press Enter to continue...")
                    continue

                task_id = Prompt.ask("Enter task ID to update")
                try:
                    task_id = int(task_id)
                    # Check if task exists
                    current_task = task_manager.get_task(task_id)

                    title = Prompt.ask(f"Enter new title (current: {current_task.title})", default=current_task.title)
                    description = Prompt.ask(f"Enter new description (current: {current_task.description})", default=current_task.description)

                    success = task_manager.update_task(task_id, title, description)
                    if success:
                        print(f"[green]Task {task_id} updated successfully![/green]")
                    else:
                        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")
                    input("Press Enter to continue...")
                except ValueError:
                    print("[red]Error: Task ID must be a number[/red]")
                    input("Press Enter to continue...")
            elif choice == '3':
                if not tasks:
                    print("[yellow]No tasks available to delete.[/yellow]")
                    input("Press Enter to continue...")
                    continue

                task_id = Prompt.ask("Enter task ID to delete")
                try:
                    task_id = int(task_id)
                    success = task_manager.delete_task(task_id)
                    if success:
                        print(f"[green]Task {task_id} deleted successfully![/green]")
                    else:
                        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")
                    input("Press Enter to continue...")
                except ValueError:
                    print("[red]Error: Task ID must be a number[/red]")
                    input("Press Enter to continue...")
            elif choice == '4':
                if not tasks:
                    print("[yellow]No tasks available to mark complete.[/yellow]")
                    input("Press Enter to continue...")
                    continue

                task_id = Prompt.ask("Enter task ID to mark complete")
                try:
                    task_id = int(task_id)
                    success = task_manager.mark_complete(task_id)
                    if success:
                        print(f"[green]Task {task_id} marked as complete![/green]")
                    else:
                        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")
                    input("Press Enter to continue...")
                except ValueError:
                    print("[red]Error: Task ID must be a number[/red]")
                    input("Press Enter to continue...")
            elif choice == '5':
                if not tasks:
                    print("[yellow]No tasks available to mark incomplete.[/yellow]")
                    input("Press Enter to continue...")
                    continue

                task_id = Prompt.ask("Enter task ID to mark incomplete")
                try:
                    task_id = int(task_id)
                    success = task_manager.mark_incomplete(task_id)
                    if success:
                        print(f"[green]Task {task_id} marked as incomplete![/green]")
                    else:
                        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")
                    input("Press Enter to continue...")
                except ValueError:
                    print("[red]Error: Task ID must be a number[/red]")
                    input("Press Enter to continue...")
            elif choice == '6':
                print("[green]Goodbye![/green]")
                break
            else:
                print("[red]Invalid choice. Please select 1-6.[/red]")
                input("Press Enter to continue...")

        except KeyboardInterrupt:
            print("\n[green]Goodbye![/green]")
            break


def run_single_command():
    """Function for single command execution mode."""
    pass  # Placeholder for Typer commands below


# Create a Typer app instance
app = typer.Typer(add_completion=False, help="Enhanced Console Todo Application with Typer and Rich formatting.")


@app.command()
def add(title: str = typer.Option(..., "--title", "-t", help="Task title"),
        description: str = typer.Option("", "--description", "-d", help="Task description")):
    """
    Add a new task with title and optional description.
    """
    task_manager = TaskManager()
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
    task_manager = TaskManager()

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
    console = Console()
    console.print(table)


@app.command()
def update(task_id: int = typer.Option(..., "--id", "-i", help="Task ID to update"),
          title: str = typer.Option(None, "--title", "-t", help="New task title"),
          description: str = typer.Option(None, "--description", "-d", help="New task description")):
    """
    Update an existing task's title or description.
    """
    task_manager = TaskManager()

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
    task_manager = TaskManager()
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
    task_manager = TaskManager()
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
    task_manager = TaskManager()
    success = task_manager.mark_incomplete(task_id)
    if success:
        print(f"[green]Task {task_id} marked as incomplete[/green]")
    else:
        print(f"[red]Error: Task with ID {task_id} does not exist[/red]")


@app.command()
def interactive():
    """
    Run the application in interactive mode with continuous table display.
    """
    interactive_mode()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Enhanced Console Todo Application with Typer and Rich formatting.
    """
    if ctx.invoked_subcommand is None:
        # If no subcommand is provided, start interactive mode
        interactive_mode()


if __name__ == "__main__":
    app()