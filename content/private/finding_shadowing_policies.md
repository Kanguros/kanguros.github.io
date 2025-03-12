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
--8<-- "code/shadowing_rules/fsr/resolver.py"
```

## Finding shadowing rules

```python
--8<-- "code/shadowing_rules/fsr/shadower.py"
```

## Utils

```python
--8<-- "code/shadowing_rules/fsr/utils.py"
```

## CLI

```python
--8<-- "code/shadowing_rules/fsr/__main__.py"
```

## Unit tests

```python
--8<-- "code/shadowing_rules/fsr/test.py"
```
