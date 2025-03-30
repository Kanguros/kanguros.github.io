---
title: Getting information from Azure Devops
status: draft
date: 2025-03-30
summary: Script for extracting information about Repos from Azure
    Devops.
---

[TOC]

## Code

```{ .python }
--8<-- "code/azure_repos/script.py"
```

## Prompt

```markdown
## Goal

Generate a Python script that retrieves repository, build, and
pipeline data from Azure DevOps and saves it as a CSV.

## Functionality

- Accepts a list of repository prefixes as input.
- Identifies all Azure Repositories whose names start with any of the
  given prefixes.
- For each matching repository:
    - Retrieves all Builds associated with it.
    - Retrieves all Pipelines associated with it.
- Saves the collected data into a CSV file in a structured format.

## Requirements

- KISS (Keep It Simple, Stupid) – Maintain simplicity and avoid
  unnecessary complexity.
- SRP (Single Responsibility Principle) – Ensure each function has a
  well-defined, singular purpose.
- DRY (Don't Repeat Yourself) - Avoid code duplication.
- Modular Design – Organize code into reusable functions for clarity
  and maintainability.
- Use Python's typing – Implement type hints for better readability
  and robustness.
    - BAD - `List[Dict[str, Any]]`
    - GOOD - `list[dict[str, Any]]`
- No inline comments – Use docstrings instead for documentation.
- Docstring should be concise and short.
- Single script file – Keep the entire implementation in one .py file
  with a structured if **name** == "**main**": block.
- Use the azure-devops package (GitHub) for API interactions
  (https://github.com/microsoft/azure-devops-python-api).
- Constants like Azure Devops Project or PAT hardcoded in
  `__main__` block.
- Use `logging.basicConfig` to configure logging and display logs in
  the terminal.
- Use `logger` calls at appropriate levels.

## Expected Output

A well-structured and maintainable Python script that efficiently
retrieves and stores Azure DevOps repository, build, and pipeline
data, adhering to best coding practices
```
