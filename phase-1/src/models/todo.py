"""
Todo entity definition and in-memory storage mechanism.

This module defines the Todo entity and provides in-memory storage
with ID generation strategy.
"""


class Todo:
    """
    Represents a todo item with id, title, description, and completion status.
    """
    
    def __init__(self, todo_id, title, description="", completed=False):
        """
        Initialize a Todo instance.
        
        Args:
            todo_id (int): Unique identifier for the todo
            title (str): Title of the todo
            description (str, optional): Detailed description of the todo
            completed (bool, optional): Completion status, defaults to False
        """
        self.id = todo_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        """String representation of the Todo."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def to_dict(self):
        """Convert the Todo to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }


class InMemoryStorage:
    """
    In-memory storage mechanism for Todo items.
    """
    
    def __init__(self):
        """Initialize the in-memory storage."""
        self.todos = {}  # Dictionary to store todos with ID as key
        self.current_id = 1  # Counter for generating unique IDs

    def add_todo(self, title, description=""):
        """
        Add a new todo to the storage.
        
        Args:
            title (str): Title of the todo
            description (str, optional): Description of the todo
            
        Returns:
            Todo: The newly created Todo instance
        """
        # Create a new todo with the current ID
        new_todo = Todo(self.current_id, title, description, False)
        
        # Store the todo
        self.todos[self.current_id] = new_todo
        
        # Increment the ID counter for the next todo
        self.current_id += 1
        
        return new_todo

    def get_todo(self, todo_id):
        """
        Get a todo by its ID.
        
        Args:
            todo_id (int): ID of the todo to retrieve
            
        Returns:
            Todo: The todo with the specified ID, or None if not found
        """
        return self.todos.get(todo_id)

    def get_all_todos(self):
        """
        Get all todos in the storage.
        
        Returns:
            list: List of all Todo instances
        """
        return list(self.todos.values())

    def update_todo(self, todo_id, title=None, description=None):
        """
        Update an existing todo.
        
        Args:
            todo_id (int): ID of the todo to update
            title (str, optional): New title for the todo
            description (str, optional): New description for the todo
            
        Returns:
            Todo: The updated Todo instance, or None if not found
        """
        if todo_id not in self.todos:
            return None
        
        todo = self.todos[todo_id]
        
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
            
        return todo

    def delete_todo(self, todo_id):
        """
        Delete a todo by its ID.
        
        Args:
            todo_id (int): ID of the todo to delete
            
        Returns:
            bool: True if the todo was deleted, False if not found
        """
        if todo_id not in self.todos:
            return False
        
        del self.todos[todo_id]
        return True

    def mark_complete(self, todo_id):
        """
        Mark a todo as complete.
        
        Args:
            todo_id (int): ID of the todo to mark as complete
            
        Returns:
            Todo: The updated Todo instance, or None if not found
        """
        if todo_id not in self.todos:
            return None
        
        self.todos[todo_id].completed = True
        return self.todos[todo_id]

    def mark_incomplete(self, todo_id):
        """
        Mark a todo as incomplete.
        
        Args:
            todo_id (int): ID of the todo to mark as incomplete
            
        Returns:
            Todo: The updated Todo instance, or None if not found
        """
        if todo_id not in self.todos:
            return None
        
        self.todos[todo_id].completed = False
        return self.todos[todo_id]