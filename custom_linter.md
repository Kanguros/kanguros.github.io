---
title: Custom Linter
date: 2026-03-11
status: draft
summary: Custom linter rules to fulfill specific needs.
---

[TOC]





```python

import ast
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class LintError:
    line: int
    col: int
    code: str
    message: str
    path: str

    def __str__(self):
        return f"{self.path}:{self.line}:{self.col}: [{self.code}] {self.message}"

# --- Linter Rules ---

def rule_line_length(tree, lines, path):
    """L001: Ensures lines don't exceed 88 characters."""
    errors = []
    for i, line in enumerate(lines, 1):
        if len(line.rstrip()) > 88:
            errors.append(LintError(i, 88, "L001", "Line too long", path))
    return errors

def rule_no_eval(tree, lines, path):
    """L002: Prohibits the use of the eval() function."""
    errors = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "eval":
                errors.append(LintError(node.lineno, node.col_offset, "L002", "Usage of eval()", path))
    return errors

# Register rules here
ACTIVE_RULES = [rule_line_length, rule_no_eval]

# --- Engine ---

def get_disabled_rules(lines):
    """Returns a map of line numbers to sets of disabled rule IDs."""
    noqa_regex = re.compile(r"#\s*noqa(?::\s*([A-Z0-9,\s]+))?", re.IGNORECASE)
    disabled = {}
    for i, line in enumerate(lines, 1):
        match = noqa_regex.search(line)
        if match:
            ids = match.group(1)
            disabled[i] = {id.strip().upper() for id in ids.split(",")} if ids else "ALL"
    return disabled

def lint_file(path):
    """Processes a single file and returns its errors."""
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.splitlines()
        
        tree = ast.parse(content)
        disabled_map = get_disabled_rules(lines)

        for rule_func in ACTIVE_RULES:
            for err in rule_func(tree, lines, path):
                line_disabled = disabled_map.get(err.line, set())
                if line_disabled == "ALL" or err.code in line_disabled:
                    continue
                errors.append(err)
    except Exception as e:
        print(f"Skipping {path}: {e}")
    return errors

def run_parallel_linting(files):
    """Executes linting across multiple files using threads."""
    all_errors = []
    with ThreadPoolExecutor() as executor:
        results = executor.map(lint_file, files)
        for file_errors in results:
            all_errors.extend(file_errors)
    return all_errors

def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(0)

    errors = run_parallel_linting(files)

    if errors:
        for error in sorted(errors, key=lambda x: (x.path, x.line)):
            print(error)
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()


```