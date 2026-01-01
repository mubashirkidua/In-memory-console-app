---

description: "Task list template for feature implementation"
---

# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `/specs/1-in-memory-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in phase-1/
- [x] T002 Initialize Python project with standard library dependencies only
- [x] T003 [P] Create source directory structure: phase-1/src/, phase-1/src/models/, phase-1/src/services/, phase-1/src/cli/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Create Todo entity definition in phase-1/src/models/todo.py
- [x] T005 [P] Create in-memory storage mechanism in phase-1/src/models/todo.py
- [x] T006 [P] Create ID generation strategy in phase-1/src/models/todo.py
- [x] T007 Create TodoService interface in phase-1/src/services/todo_service.py
- [x] T008 Create CLI interface structure in phase-1/src/cli/cli_interface.py
- [x] T009 Create main application entry point in phase-1/src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todos to the in-memory list

**Independent Test**: Users can enter a todo title and optionally a description, and the todo appears in the list when viewing todos.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [x] T010 [P] [US1] Manual test for adding todo with title only
- [x] T011 [P] [US1] Manual test for adding todo with title and description

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Todo model with id, title, description, completed status in phase-1/src/models/todo.py
- [x] T013 [US1] Implement add_todo method in phase-1/src/services/todo_service.py
- [x] T014 [US1] Implement input handling for adding todos in phase-1/src/cli/cli_interface.py
- [x] T015 [US1] Implement output formatting for success message in phase-1/src/cli/cli_interface.py
- [x] T016 [US1] Add validation for todo title in phase-1/src/services/todo_service.py
- [x] T017 [US1] Integrate add todo functionality in main application loop in phase-1/src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Allow users to view all todos with their status (complete/incomplete)

**Independent Test**: Users can see all todos in a clear, readable format when requested.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T018 [P] [US2] Manual test for viewing todos when list is empty
- [x] T019 [P] [US2] Manual test for viewing todos with mixed completion status

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement get_all_todos method in phase-1/src/services/todo_service.py
- [x] T021 [US2] Implement CLI display for todo list in phase-1/src/cli/cli_interface.py
- [x] T022 [US2] Format todo list for console display in phase-1/src/cli/cli_interface.py
- [x] T023 [US2] Handle empty todo list case in phase-1/src/cli/cli_interface.py
- [x] T024 [US2] Integrate view todos functionality in main application loop in phase-1/src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Allow users to mark specific todos as complete

**Independent Test**: Users can mark specific todos as complete, which updates their status in the in-memory list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T025 [P] [US3] Manual test for marking an existing todo as complete
- [x] T026 [P] [US3] Manual test for attempting to mark a non-existent todo as complete

### Implementation for User Story 3

- [x] T027 [P] [US3] Implement mark_complete method in phase-1/src/services/todo_service.py
- [x] T028 [US3] Implement input handling for marking todos in phase-1/src/cli/cli_interface.py
- [x] T029 [US3] Implement validation for todo ID in phase-1/src/services/todo_service.py
- [x] T030 [US3] Add success/error messaging for marking complete in phase-1/src/cli/cli_interface.py
- [x] T031 [US3] Integrate mark complete functionality in main application loop in phase-1/src/main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo (Priority: P3)

**Goal**: Allow users to update the description of existing todos

**Independent Test**: Users can update the description of an existing todo in the in-memory list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T032 [P] [US4] Manual test for updating an existing todo's title
- [x] T033 [P] [US4] Manual test for attempting to update a non-existent todo

### Implementation for User Story 4

- [x] T034 [P] [US4] Implement update_todo method in phase-1/src/services/todo_service.py
- [x] T035 [US4] Implement input handling for updating todos in phase-1/src/cli/cli_interface.py
- [x] T036 [US4] Implement validation for update inputs in phase-1/src/services/todo_service.py
- [x] T037 [US4] Add success/error messaging for updates in phase-1/src/cli/cli_interface.py
- [x] T038 [US4] Integrate update todo functionality in main application loop in phase-1/src/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to delete specific todos from the in-memory list

**Independent Test**: Users can remove specific todos from the in-memory list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T039 [P] [US5] Manual test for deleting an existing todo
- [x] T040 [P] [US5] Manual test for attempting to delete a non-existent todo

### Implementation for User Story 5

- [x] T041 [P] [US5] Implement delete_todo method in phase-1/src/services/todo_service.py
- [x] T042 [US5] Implement input handling for deleting todos in phase-1/src/cli/cli_interface.py
- [x] T043 [US5] Implement validation for delete operation in phase-1/src/services/todo_service.py
- [x] T044 [US5] Add success/error messaging for deletion in phase-1/src/cli/cli_interface.py
- [x] T045 [US5] Integrate delete todo functionality in main application loop in phase-1/src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T046 [P] Add comprehensive error handling throughout the application
- [x] T047 [P] Improve user experience with better prompts and messages
- [x] T048 [P] Add graceful exit functionality to main application loop
- [x] T049 [P] Code cleanup and refactoring
- [x] T050 [P] Documentation updates in README.md
- [x] T051 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Manual test for adding todo with title only in phase-1/src/cli/cli_interface.py"
Task: "Manual test for adding todo with title and description in phase-1/src/cli/cli_interface.py"

# Launch all models for User Story 1 together:
Task: "Create Todo model with id, title, description, completed status in phase-1/src/models/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence