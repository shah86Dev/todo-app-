<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles:
- Added I. In-Memory Storage (new)
- Added III. Test-First (new)
- Added IV. Clean Code & Modularity (new)
- Added V. Spec-Driven Development (new)
- Added VI. Dependency Management (new)
- Updated II. CLI Interface with specific requirements
Added sections: Additional Constraints, Development Workflow
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ⚠ pending
- .specify/templates/spec-template.md ⚠ pending
- .specify/templates/tasks-template.md ⚠ pending
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# Todo In-Memory Python Console Application Constitution

## Core Principles

### I. In-Memory Storage
All task data must be stored strictly in memory with no persistence to disk or database. The system must reset all data when the application terminates. This ensures simplicity and local execution without external dependencies.
<!-- Storage: In-memory only (no persistence) -->

### II. CLI Interface
The application must be executed as a command-line program running locally in a terminal environment. The console user interface must use Typer for CLI command handling and Rich for enhanced terminal output including colored messages and table-based task listings. The application must remain a pure console-based application with no web frameworks, APIs, or external services.
<!-- CLI: Typer for commands, Rich for formatting, Console-only execution -->

### III. Test-First
All components must have unit tests written first following TDD principles. Tests must be written before implementation, with tests failing → implementation → then passing (Red-Green-Refactor cycle). All functionality must be independently testable.

### IV. Clean Code & Modularity
Clean code principles and modular design with proper Python project structure are mandatory. The codebase must follow separation of concerns with clear boundaries between UI layer (CLI), business logic (services), and data models. Code must be maintainable, readable, and well-structured.

### V. Spec-Driven Development
Development must follow a spec-driven workflow using Claude Code and Spec-Kit Plus with no manual coding outside of the specified tools. All generated artifacts must be traceable to specifications and tasks. No ad-hoc development is permitted without proper specification first.

### VI. Dependency Management
UV must be used for dependency management and execution. All project dependencies must be managed through UV, with proper pyproject.toml configuration. No other dependency management tools are permitted.

## Additional Constraints
Technology stack requirements: Python 3.13+ only, Typer for CLI, Rich for formatting, UV for dependencies. No web frameworks, APIs, authentication, databases, or external services are permitted. The system must support a single user and run locally in a terminal environment only.

## Development Workflow
Development must follow Claude Code and Spec-Kit Plus workflows. All changes must be spec-driven with proper traceability. Code review requirements mandate verification of constitution compliance. All artifacts must be linked to specifications and tasks.

## Governance
The constitution supersedes all other practices. All pull requests and reviews must verify compliance with these principles. Complexity must be justified with clear reasoning. All generated artifacts must be traceable to specifications and tasks.

**Version**: 1.1.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
