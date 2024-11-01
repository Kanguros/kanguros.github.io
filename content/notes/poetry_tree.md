Title: Poetry tree  
Date: 2023-07-10  
Tags: notes, poetry, graph  
Category: Note  
Summary: Poetry tree as graph.

This module provides functions to parse and work with a dependency tree output. The primary
function, `parse_dependency_tree`, takes a tree-like output and converts it into a hierarchical data structure for
further processing.

## `dependency_parser.py`

```python

def parse_dependency_tree(tree_output):
    tree_lines = tree_output.strip().split("\n")
    dependencies = {}
    current_package = None

    for line in tree_lines:
        if line.endswith(" "):  # Indication of a dependency
            package_name = line.strip()
            dependencies[package_name] = []
            current_package = package_name
        elif line.startswith("├── ") or line.startswith("└── "):  # Sub-dependency
            sub_dependency = line[4:].strip()
            if current_package:
                dependencies[current_package].append(sub_dependency)

    return dependencies

```

## `test_dependency_parser.py`

```python

import dependency_parser

def test_parse_dependency_tree():
    tree_output = """
    requests
    ├── certifi
    ├── charset-normalizer
    ├── idna
    └── urllib3
    sqlalchemy
    └── greenlet
    celery
    ├── billiard
    ├── kombu
    │   └── amqp
    └── vine
    """

    expected_dependencies = {
        'requests': ['certifi', 'charset-normalizer', 'idna', 'urllib3'],
        'sqlalchemy': ['greenlet'],
        'celery': ['billiard', {'kombu': ['amqp']}, 'vine']
    }

    assert dependency_parser.parse_dependency_tree(tree_output) == expected_dependencies

```
