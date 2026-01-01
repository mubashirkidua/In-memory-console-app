---
id: 1
title: create-impl-plan
stage: plan
date: 2026-01-02
surface: agent
model: Qwen
feature: 1-in-memory-todo
branch: 1-in-memory-todo
user: user
command: /sp.plan
labels: [implementation-plan, todo-app, python]
links:
  spec: specs/1-in-memory-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-in-memory-todo/plan/plan.md
 - specs/1-in-memory-todo/plan/research.md
 - specs/1-in-memory-todo/plan/data-model.md
 - specs/1-in-memory-todo/plan/contracts/todo-contract.md
 - specs/1-in-memory-todo/plan/quickstart.md
tests:
 - none
---

## Prompt

```
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
handoffs: 
  - label: Create Tasks
    agent: sp.tasks
    prompt: Break the plan into tasks
    send: true
  - label: Create Checklist
    agent: sp.checklist
    prompt: Create a checklist for the following domain...
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/bash/setup-plan.sh --json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/bash/update-agent-context.sh qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

---

/sp.plan Phase I: In-Memory Python Console Todo Application

Purpose:
Translate the Phase I specification into a clear, high-level implementation plan that defines
architecture, components, data flow, and development sequence for an in-memory console-based
Todo application built using Claude Code and Spec-Kit Plus.

System architecture:
- Application type: Monolithic, single-process, in-memory console application
- Interaction model: Synchronous, menu-driven command-line interface
- State management: In-memory data structures only (no persistence)
- Execution flow: User input → Command routing → Business logic → Output rendering

Core components:
1. Entry Point
   - Initializes application state
   - Starts main input loop
   - Handles graceful exit

2. Command-Line Interface (CLI) Layer
   - Displays menu options
   - Captures and validates user input
   - Maps user commands to application actions
   - Handles invalid input and retry logic

3. Application / Service Layer
   - Implements core Todo operations:
     - Add todo
     - Delete todo
     - Update todo
     - View todos
     - Mark todo as complete
   - Enforces business rules (e.g., valid IDs, state transitions)
   - Remains independent of input/output concerns

4. Domain Model
   - Todo entity definition (id, title, description, completed status)
   - In-memory collection to store todos
   - ID generation strategy (incremental, in-memory)

5. Output / Presentation Layer
   - Formats todo lists for console display
   - Provides user feedback messages (success, error, empty state)
   - Ensures consistent and readable console output

Data flow:
- User selects an action from the CLI menu
- CLI validates raw input and converts it into structured commands
- Service layer executes the requested operation on in-memory data
- Results are returned to the presentation layer
- Output is rendered to the console
- Application returns to main loop

Development sequence:
1. Define domain model and in-memory storage strategy
2. Design service layer interfaces for todo operations
3. Design CLI menu structure and command routing
4. Define input validation and error handling strategy
5. Define output formatting conventions
6. Integrate components through a main application loop

Design principles:
- Single responsibility per component
- Clear separation between CLI, business logic, and data model
- Simplicity over extensibility (Phase I only)
- Readability and maintainability prioritized over optimization
- No external dependencies beyond standard Python libraries

Constraints reaffirmed:
- Python 3.13+
- Console-only interface
- No file system access
- No databases or external services
- No AI, agents, or automation beyond Claude Code execution

Deliverable:
- A complete, reviewable implementation plan suitable for conversion into task-level prompts
  for Claude Code via Spec-Kit Plus.
```

## Response snapshot

I've created a comprehensive implementation plan for the In-Memory Python Console Todo Application. Here's what was completed:

1. Created the implementation plan file (plan.md) with:
   - Technical context including language, constraints, and goals
   - Constitution check confirming alignment with project principles
   - Project structure outlining all necessary files and directories
   - Complexity tracking section

2. Completed Phase 0 (Research) with research.md containing:
   - Decisions on Python version and standard libraries
   - In-memory data structure approach
   - Command-line interface approach
   - Todo entity structure
   - ID generation strategy
   - Error handling approach

3. Completed Phase 1 (Design) with:
   - Data model (data-model.md) defining the Todo entity and in-memory storage
   - API contracts (todo-contract.md) specifying the behavior of each operation
   - Quickstart guide (quickstart.md) for running and using the application

All required artifacts have been created and the implementation plan is ready for the next phase. The plan follows all specified constraints and design principles, focusing on simplicity and clear separation of concerns.

## Outcome

- ✅ Impact: Created complete implementation plan with all required artifacts for development
- 🧪 Tests: No tests required for planning phase
- 📁 Files: Created plan.md, research.md, data-model.md, contracts, and quickstart.md
- 🔁 Next prompts: /sp.tasks to break the plan into implementation tasks
- 🧠 Reflection: Plan addresses all requirements and constraints while maintaining simplicity

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All required artifacts created
- Prompt variant (if applicable): Standard implementation planning
- Next experiment (smallest change to try): Begin task breakdown with /sp.tasks
