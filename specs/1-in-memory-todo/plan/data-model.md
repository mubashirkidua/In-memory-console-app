# Data Model: In-Memory Python Console Todo Application

## Todo Entity

### Attributes
- **id** (int): Unique identifier for the todo item
  - Auto-generated using incremental strategy
  - Primary identifier for operations
- **title** (str): Title or brief description of the todo
  - Required field
  - Max length: 200 characters
- **description** (str): Detailed description of the todo (optional)
  - Optional field
  - Max length: 1000 characters
- **completed** (bool): Status indicating completion
  - Default: False
  - True if completed, False if pending

### State Transitions
- New todo: `completed = False`
- Mark complete: `completed = True`
- Mark incomplete: `completed = False` (if supported)

## In-Memory Storage

### Collection Structure
- **todos** (list): List of todo dictionaries
  - Maintains order of creation
  - Provides O(n) search by ID
  - Maximum capacity: 1000 items

### ID Generation
- **current_id** (int): Counter for generating unique IDs
  - Starts at 1
  - Increments with each new todo
  - Reset only when todos list is cleared (not supported in Phase I)

## Validation Rules

### Todo Creation
- Title must be provided (non-empty)
- Title must be ≤ 200 characters
- Description, if provided, must be ≤ 1000 characters

### Todo Updates
- ID must exist in the collection
- Updated title must follow creation validation rules
- Updated description must follow creation validation rules

### Todo Operations
- ID for operations must exist in the collection
- Marking complete/incomplete requires valid ID