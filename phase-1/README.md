# In-Memory Python Console Todo Application

This is a simple, in-memory console-based todo application built with Python. All data is stored in memory only and will be lost when the application exits.

## Prerequisites

- Python 3.13 or higher

## Running the Application

1. Navigate to the project directory
2. Run the application:
   ```bash
   python phase-1/src/main.py
   ```

## Features

- Add new todos with title and optional description
- View all todos with their completion status
- Update existing todos
- Delete todos
- Mark todos as complete/incomplete

## Architecture

The application follows a clean architecture with separation of concerns:

- **Models**: Contains the Todo entity and in-memory storage mechanism
- **Services**: Contains the business logic for todo operations
- **CLI**: Handles user interface and input/output operations

## Limitations

- Data is stored in memory only (no persistence)
- Supports up to 1000 todos simultaneously
- Single-user application