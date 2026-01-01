"""
Main entry point for the In-Memory Python Console Todo Application.

This module initializes the application state, starts the main input loop,
and handles graceful exit.
"""

from cli.cli_interface import CLIInterface
from services.todo_service import TodoService


def main():
    """Main application entry point."""
    print("Welcome to the In-Memory Python Console Todo Application!")
    
    # Initialize the todo service (which manages in-memory storage)
    todo_service = TodoService()
    
    # Initialize the CLI interface
    cli = CLIInterface(todo_service)
    
    # Start the main application loop
    cli.run()


if __name__ == "__main__":
    main()