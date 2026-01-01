"""
Command-Line Interface for the Todo Application.

This module handles user input, displays menus, and formats output
for console display.
"""

from services.todo_service import TodoService


class CLIInterface:
    """
    Command-line interface for the Todo application.
    """
    
    def __init__(self, todo_service):
        """
        Initialize the CLI interface.
        
        Args:
            todo_service (TodoService): The todo service to interact with
        """
        self.todo_service = todo_service
        self.running = True

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("TODO APPLICATION MENU")
        print("="*40)
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Update an existing todo")
        print("4. Delete a todo")
        print("5. Mark a todo as complete")
        print("6. Mark a todo as incomplete")
        print("7. Exit")
        print("="*40)

    def get_user_choice(self):
        """
        Get the user's menu choice.
        
        Returns:
            str: The user's choice
        """
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled by user.")
            return "7"  # Treat as exit

    def handle_add_todo(self):
        """Handle adding a new todo."""
        print("\n--- Add New Todo ---")
        title = input("Enter the title: ").strip()
        
        if not title:
            print("Error: Title is required and cannot be empty.")
            return
        
        description = input("Enter the description (optional, press Enter to skip): ").strip()
        
        result = self.todo_service.add_todo(title, description if description else "")
        
        if result["success"]:
            print(f"✓ Todo added successfully with ID: {result['todo'].id}")
        else:
            print(f"✗ Error: {result['error']}")

    def handle_view_todos(self):
        """Handle viewing all todos."""
        print("\n--- All Todos ---")
        result = self.todo_service.get_all_todos()
        
        if result["success"]:
            todos = result["todos"]
            
            if not todos:
                print("No todos found.")
            else:
                for todo in todos:
                    status = "✓" if todo.completed else "○"
                    print(f"[{status}] {todo.id}. {todo.title}")
                    if todo.description:
                        print(f"    Description: {todo.description}")
        else:
            print(f"✗ Error: {result.get('error', 'Unknown error')}")

    def handle_update_todo(self):
        """Handle updating an existing todo."""
        print("\n--- Update Todo ---")
        
        try:
            todo_id = int(input("Enter the ID of the todo to update: "))
        except ValueError:
            print("Error: Please enter a valid ID (number).")
            return
        
        # Check if the todo exists
        temp_result = self.todo_service.get_all_todos()
        if temp_result["success"]:
            existing_todos = {todo.id: todo for todo in temp_result["todos"]}
            if todo_id not in existing_todos:
                print(f"Error: Todo with ID {todo_id} not found.")
                return
        
        title = input("Enter the new title (or press Enter to keep current): ").strip()
        title = title if title else None
        
        description = input("Enter the new description (or press Enter to keep current): ").strip()
        description = description if description else None
        
        # If both are None, no update is needed
        if title is None and description is None:
            print("No changes provided, nothing to update.")
            return
        
        result = self.todo_service.update_todo(todo_id, title, description)
        
        if result["success"]:
            print("✓ Todo updated successfully.")
        else:
            print(f"✗ Error: {result['error']}")

    def handle_delete_todo(self):
        """Handle deleting a todo."""
        print("\n--- Delete Todo ---")
        
        try:
            todo_id = int(input("Enter the ID of the todo to delete: "))
        except ValueError:
            print("Error: Please enter a valid ID (number).")
            return
        
        result = self.todo_service.delete_todo(todo_id)
        
        if result["success"]:
            print("✓ Todo deleted successfully.")
        else:
            print(f"✗ Error: {result['error']}")

    def handle_mark_complete(self):
        """Handle marking a todo as complete."""
        print("\n--- Mark Todo as Complete ---")
        
        try:
            todo_id = int(input("Enter the ID of the todo to mark as complete: "))
        except ValueError:
            print("Error: Please enter a valid ID (number).")
            return
        
        result = self.todo_service.mark_complete(todo_id)
        
        if result["success"]:
            print("✓ Todo marked as complete successfully.")
        else:
            print(f"✗ Error: {result['error']}")

    def handle_mark_incomplete(self):
        """Handle marking a todo as incomplete."""
        print("\n--- Mark Todo as Incomplete ---")
        
        try:
            todo_id = int(input("Enter the ID of the todo to mark as incomplete: "))
        except ValueError:
            print("Error: Please enter a valid ID (number).")
            return
        
        result = self.todo_service.mark_incomplete(todo_id)
        
        if result["success"]:
            print("✓ Todo marked as incomplete successfully.")
        else:
            print(f"✗ Error: {result['error']}")

    def run(self):
        """Run the main application loop."""
        print("Starting the Todo Application...")
        
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.handle_add_todo()
            elif choice == "2":
                self.handle_view_todos()
            elif choice == "3":
                self.handle_update_todo()
            elif choice == "4":
                self.handle_delete_todo()
            elif choice == "5":
                self.handle_mark_complete()
            elif choice == "6":
                self.handle_mark_incomplete()
            elif choice == "7":
                print("Thank you for using the Todo Application. Goodbye!")
                self.running = False
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")