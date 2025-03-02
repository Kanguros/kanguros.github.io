---
title: Finding shadowing policies
date: 2025-02-20
status: draft
summary: Python script for finding shadowing security policies on firewall.
---

[TOC]

## Data models

```python
--8<-- "code/shadowing_rules/models.py"
```

## Resolve addresses

```python
--8<-- "code/shadowing_rules/resolve_addresses.py"
```

## Finding shadowing rules

unit_tests

```python
--8<-- "code/shadowing_rules/main.py"

```
