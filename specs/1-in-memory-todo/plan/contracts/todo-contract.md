# Todo Application API Contract

## Overview
This contract defines the interface for the in-memory console todo application. Since this is a console application without a traditional API, the contract specifies the expected behavior of each operation from a user interaction perspective.

## Operations

### Add Todo
- **User Action**: Select "Add Todo" option from menu
- **Input**: Todo title (required), description (optional)
- **Validation**: Title must be non-empty and ≤ 200 characters
- **Success Response**: Todo added with unique ID, confirmation message
- **Error Response**: Error message if validation fails

### View Todos
- **User Action**: Select "View Todos" option from menu
- **Input**: None
- **Success Response**: List of all todos with ID, title, and completion status
- **Error Response**: "No todos found" if list is empty

### Update Todo
- **User Action**: Select "Update Todo" option from menu
- **Input**: Todo ID, new title (optional), new description (optional)
- **Validation**: ID must exist, title ≤ 200 characters if provided
- **Success Response**: Todo updated, confirmation message
- **Error Response**: Error message if ID doesn't exist or validation fails

### Delete Todo
- **User Action**: Select "Delete Todo" option from menu
- **Input**: Todo ID
- **Validation**: ID must exist
- **Success Response**: Todo removed, confirmation message
- **Error Response**: Error message if ID doesn't exist

### Mark Todo Complete/Incomplete
- **User Action**: Select "Mark Todo Complete/Incomplete" option from menu
- **Input**: Todo ID
- **Validation**: ID must exist
- **Success Response**: Todo status updated, confirmation message
- **Error Response**: Error message if ID doesn't exist