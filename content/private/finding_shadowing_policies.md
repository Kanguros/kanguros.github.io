---
title: Finding shadowing policies
date: 2025-02-20
status: draft
summary: Python script for finding shadowing security policies on firewall.
---

[TOC]

## Models

```python
--8<-- "code/shadowing_rules/fsr/models.py"
```

## Resolve addresses

```python
--8<-- "code/shadowing_rules/fsr/resolve_addresses.py"
```

## Finding shadowing rules

```python
--8<-- "code/shadowing_rules/fsr/found_shadowing.py"
```

## Unit tests

```json
--8<-- "code/shadowing_rules/fsr/test_models.py"
```
