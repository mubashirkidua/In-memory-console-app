# Phase 1 – In-Memory Python Console Todo App

## 📌 Overview

This repository contains **Phase 1** of a multi-phase project to build an AI‑native Todo system.

Phase 1 focuses on creating a **simple, in-memory, console-based Todo application** using **spec-driven, agentic development** with **Spec-Kit Plus** and **Claude Code**.

The emphasis of this phase is **process correctness, clean architecture, and strict scope control**, not feature richness.

---

## 🎯 Objective

* Build a command-line Todo application that stores tasks **only in memory**.
* Implement the application using **agent-driven development** (no manual coding).
* Demonstrate a disciplined workflow:

  ```
  sp.specify → sp.plan → sp.tasks → implementation
  ```

---

## ✅ Features (Phase 1 Only)

The application supports **exactly five basic features**:

1. Add a todo
2. Delete a todo
3. Update a todo
4. View all todos
5. Mark a todo as complete

> ⚠️ No additional features are allowed in Phase 1.

---

## 🧱 Architecture Overview

Phase 1 uses a **simple monolithic structure** with clear separation of concerns:

### 1. CLI Layer

* Displays menu options
* Handles user input and output
* Routes commands to the service layer

### 2. Service Layer

* Contains all business logic
* Implements todo operations
* Validates todo IDs and state

### 3. Domain Model

* Represents a Todo entity
* Stores todos in memory
* Generates incremental IDs

---

## 🔄 Data Flow

```
User Input
   ↓
CLI Menu & Validation
   ↓
Service Layer Logic
   ↓
In-Memory Todo Store
   ↓
Console Output
```

---

## 🛠 Technology Stack

* **Python**: 3.13+
* **Environment Manager**: UV
* **Development Tools**:

  * Claude Code
  * Spec-Kit Plus
* **Runtime**: Console / Terminal

---

## 🤖 Agent Setup

Phase 1 is built using **three agents**:

### 🧠 Main Agent (Primary Orchestrator)

* Controls workflow order
* Prevents scope creep
* Validates transitions between phases

### 🧩 Sub-Agent 1: Architecture / Design Agent

* Defines domain model
* Designs component boundaries
* Specifies in-memory data flow

### ⚙️ Sub-Agent 2: Implementation Agent

* Implements tasks sequentially
* Generates Python code via Claude Code
* Ensures clean and readable output

---

## 📐 Development Workflow

The project must follow this workflow strictly:

1. Write specification using `/sp.specify`
2. Create architecture plan using `/sp.plan`
3. Break work into tasks using `/sp.tasks`
4. Implement tasks using Claude Code

> ❌ Manual coding is not allowed in Phase 1.

---

## 🚫 Constraints

* In-memory only (no files, no databases)
* Console-based interaction only
* No external Python libraries
* No tests, CI/CD, or deployment setup
* No AI/chat features inside the app
* No future-phase abstractions

---

## 🧪 Success Criteria

Phase 1 is considered successful if:

* All five features work end-to-end
* Application runs entirely in memory
* Console UX is clear and usable
* Code follows clean architecture
* Workflow order is preserved
* No scope creep is introduced

---

## ❌ Not Included in Phase 1

* Web or GUI interface
* Database or file persistence
* Authentication or user accounts
* Advanced todo features (tags, due dates, priorities)
* Docker, Kubernetes, or cloud deployment

---

## 📦 Outcome

At the end of Phase 1, this repository provides:

* A working in-memory console Todo app
* A fully auditable, spec-driven development process
* A solid foundation for Phase 2 (Full‑Stack Web Application)

Phase 1 prioritizes **discipline, clarity, and correctness** over complexity.
