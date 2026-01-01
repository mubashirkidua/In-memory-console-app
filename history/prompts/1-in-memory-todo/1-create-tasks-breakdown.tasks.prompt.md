---
id: 1
title: create-tasks-breakdown
stage: tasks
date: 2026-01-02
surface: agent
model: Qwen
feature: 1-in-memory-todo
branch: 1-in-memory-todo
user: user
command: /sp.tasks
labels: [tasks, todo-app, implementation]
links:
  spec: specs/1-in-memory-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-in-memory-todo/tasks.md
tests:
 - none
---

## Prompt

```
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
handoffs: 
  - label: Analyze For Consistency
    agent: sp.analyze
    prompt: Run a project analysis for consistency
    send: true
  - label: Implement Project
    agent: sp.implement
    prompt: Start the implementation in phases
    send: true
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/check-prerequisites.sh --json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: Phase I: In-Memory Python Console Todo Application Purpose: Decompose the Phase I implementation plan into a sequence of small, well-defined tasks that can be executed by Claude Code using a spec-driven, agentic development workflow. Task 1: Project structure initialization - Create a minimal, clean Python project structure - Define a clear entry point module - Ensure structure supports separation of CLI, services, and domain logic - Do not add external dependencies or configuration files Task 2: Define Todo domain model - Define the Todo entity with: - Unique identifier - Title - Optional description - Completion status - Keep the model simple and in-memory only - No persistence or serialization logic Task 3: Implement in-memory storage mechanism - Create an in-memory collection to store Todo items - Define ID generation strategy (incremental, in-process) - Ensure storage logic is isolated from CLI concerns Task 4: Define service layer interface - Define clear functions or methods for: - Add todo - Delete todo - Update todo - View todos - Mark todo as complete - Ensure service layer contains all business logic - Validate inputs (e.g., valid IDs, non-empty titles) Task 5: Implement service layer logic - Implement all Todo operations using the in-memory storage - Handle edge cases (empty list, invalid IDs) - Return structured results suitable for presentation Task 6: Design CLI menu and command routing - Define console menu options for all supported actions - Map menu selections to service layer operations - Keep CLI logic free of business rules Task 7: Implement user input handling and validation - Capture user input from the console - Validate input types and required fields - Handle invalid input with user-friendly messages Task 8: Implement output formatting and presentation - Format todo lists for clear console display - Display success and error messages consistently - Handle empty states gracefully Task 9: Integrate main application loop - Combine CLI, service layer, and domain model - Implement a main loop that: - Displays menu - Processes user actions - Returns control to the menu until exit - Ensure graceful termination of the application Task 10: Final review and cleanup - Ensure all 5 required features work end-to-end - Remove unused code or dead paths - Verify adherence to clean code principles - Confirm no persistence, files, or external services are used Constraints reaffirmed: - Python 3.13+ - In-memory only - Console-based interaction - No manual code edits (Claude Code only) - No scope beyond Phase I requirements Deliverable: - A complete, working in-memory console Todo application produced entirely via Claude Code following this task list.

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label  
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

---

/sp.tasks Phase I: In-Memory Python Console Todo Application

Purpose:
Decompose the Phase I implementation plan into a sequence of small, well-defined tasks that can be executed by Claude Code using a spec-driven, agentic development workflow.

Task 1: Project structure initialization
- Create a minimal, clean Python project structure
- Define a clear entry point module
- Ensure structure supports separation of CLI, services, and domain logic
- Do not add external dependencies or configuration files

Task 2: Define Todo domain model
- Define the Todo entity with:
  - Unique identifier
  - Title
  - Optional description
  - Completion status
- Keep the model simple and in-memory only
- No persistence or serialization logic

Task 3: Implement in-memory storage mechanism
- Create an in-memory collection to store Todo items
- Define ID generation strategy (incremental, in-process)
- Ensure storage logic is isolated from CLI concerns

Task 4: Define service layer interface
- Define clear functions or methods for:
  - Add todo
  - Delete todo
  - Update todo
  - View todos
  - Mark todo as complete
- Ensure service layer contains all business logic
- Validate inputs (e.g., valid IDs, non-empty titles)

Task 5: Implement service layer logic
- Implement all Todo operations using the in-memory storage
- Handle edge cases (empty list, invalid IDs)
- Return structured results suitable for presentation

Task 6: Design CLI menu and command routing
- Define console menu options for all supported actions
- Map menu selections to service layer operations
- Keep CLI logic free of business rules

Task 7: Implement user input handling and validation
- Capture user input from the console
- Validate input types and required fields
- Handle invalid input with user-friendly messages

Task 8: Implement output formatting and presentation
- Format todo lists for clear console display
- Display success and error messages consistently
- Handle empty states gracefully

Task 9: Integrate main application loop
- Combine CLI, service layer, and domain model
- Implement a main loop that:
  - Displays menu
  - Processes user actions
  - Returns control to the menu until exit
  - Ensure graceful termination of the application

Task 10: Final review and cleanup
- Ensure all 5 required features work end-to-end
- Remove unused code or dead paths
- Verify adherence to clean code principles
- Confirm no persistence, files, or external services are used

Constraints reaffirmed:
- Python 3.13+
- In-memory only
- Console-based interaction
- No manual code edits (Claude Code only)
- No scope beyond Phase I requirements

Deliverable:
- A complete, working in-memory console Todo application produced entirely via Claude Code following this task list.
```

## Response snapshot

I've created a comprehensive task breakdown for the In-Memory Python Console Todo Application. The tasks.md file includes:

1. 50 specific tasks organized across 8 phases:
   - Phase 1: Setup (3 tasks)
   - Phase 2: Foundational (6 tasks)
   - Phase 3: User Story 1 - Add Todo (7 tasks)
   - Phase 4: User Story 2 - View Todos (5 tasks)
   - Phase 5: User Story 3 - Mark Todo as Complete (5 tasks)
   - Phase 6: User Story 4 - Update Todo (5 tasks)
   - Phase 7: User Story 5 - Delete Todo (5 tasks)
   - Phase 8: Polish & Cross-Cutting Concerns (14 tasks)

2. Each task follows the required format with:
   - Checkbox for tracking
   - Sequential task ID (T001 to T051)
   - [P] marker for parallelizable tasks
   - [US#] label for user story-specific tasks
   - Clear description with exact file paths

3. The tasks follow the implementation strategy:
   - MVP approach starting with User Story 1
   - Clear dependencies and execution order
   - Parallel execution opportunities identified
   - Independent test criteria for each user story

The task breakdown is ready for execution by Claude Code following the spec-driven, agentic development workflow.

## Outcome

- ✅ Impact: Created comprehensive task breakdown with 51 specific tasks organized by user story
- 🧪 Tests: No automated tests required, manual tests included where appropriate
- 📁 Files: Created tasks.md with complete task breakdown
- 🔁 Next prompts: /sp.implement to start the implementation using Claude Code
- 🧠 Reflection: Tasks are well-structured for agentic development with clear dependencies

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All tasks follow required format
- Prompt variant (if applicable): Standard task breakdown
- Next experiment (smallest change to try): Begin implementation with /sp.implement
