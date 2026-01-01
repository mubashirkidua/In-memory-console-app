"""
Todo service layer implementation.

This module implements all Todo operations using the in-memory storage,
handles business logic and validation, and returns structured results
suitable for presentation.
"""

from models.todo import InMemoryStorage


class TodoService:
    """
    Service layer for Todo operations.
    """
    
    def __init__(self):
        """Initialize the Todo service with in-memory storage."""
        self.storage = InMemoryStorage()

    def add_todo(self, title, description=""):
        """
        Add a new todo.
        
        Args:
            title (str): Title of the todo (required)
            description (str, optional): Description of the todo
            
        Returns:
            dict: Result with 'success' status and 'todo' data or 'error'
        """
        # Validate inputs
        if not title or not title.strip():
            return {"success": False, "error": "Title is required and cannot be empty"}
        
        if len(title) > 200:
            return {"success": False, "error": "Title must be 200 characters or less"}
        
        if description and len(description) > 1000:
            return {"success": False, "error": "Description must be 1000 characters or less"}
        
        # Add the todo to storage
        new_todo = self.storage.add_todo(title.strip(), description.strip() if description else "")
        
        return {"success": True, "todo": new_todo}

    def get_all_todos(self):
        """
        Get all todos.
        
        Returns:
            dict: Result with 'success' status and 'todos' list
        """
        todos = self.storage.get_all_todos()
        return {"success": True, "todos": todos}

    def update_todo(self, todo_id, title=None, description=None):
        """
        Update an existing todo.
        
        Args:
            todo_id (int): ID of the todo to update
            title (str, optional): New title for the todo
            description (str, optional): New description for the todo
            
        Returns:
            dict: Result with 'success' status and 'todo' data or 'error'
        """
        # Validate inputs if provided
        if title is not None:
            if not title.strip():
                return {"success": False, "error": "Title cannot be empty"}
            
            if len(title) > 200:
                return {"success": False, "error": "Title must be 200 characters or less"}
        
        if description is not None and len(description) > 1000:
            return {"success": False, "error": "Description must be 1000 characters or less"}
        
        # Update the todo in storage
        updated_todo = self.storage.update_todo(
            todo_id, 
            title.strip() if title else None, 
            description.strip() if description else None
        )
        
        if updated_todo is None:
            return {"success": False, "error": f"Todo with ID {todo_id} not found"}
        
        return {"success": True, "todo": updated_todo}

    def delete_todo(self, todo_id):
        """
        Delete a todo.
        
        Args:
            todo_id (int): ID of the todo to delete
            
        Returns:
            dict: Result with 'success' status or 'error'
        """
        deleted = self.storage.delete_todo(todo_id)
        
        if not deleted:
            return {"success": False, "error": f"Todo with ID {todo_id} not found"}
        
        return {"success": True}

    def mark_complete(self, todo_id):
        """
        Mark a todo as complete.
        
        Args:
            todo_id (int): ID of the todo to mark as complete
            
        Returns:
            dict: Result with 'success' status and 'todo' data or 'error'
        """
        todo = self.storage.mark_complete(todo_id)
        
        if todo is None:
            return {"success": False, "error": f"Todo with ID {todo_id} not found"}
        
        return {"success": True, "todo": todo}

    def mark_incomplete(self, todo_id):
        """
        Mark a todo as incomplete.
        
        Args:
            todo_id (int): ID of the todo to mark as incomplete
            
        Returns:
            dict: Result with 'success' status and 'todo' data or 'error'
        """
        todo = self.storage.mark_incomplete(todo_id)
        
        if todo is None:
            return {"success": False, "error": f"Todo with ID {todo_id} not found"}
        
        return {"success": True, "todo": todo}