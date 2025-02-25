---
title: Finding shadowing policies
date: 2025-02-20
status: draft
summary: Python script for finding shadowing security policies on firewall.
---

[TOC]

## Code

```python

```

## Resolve addresses

```python
from typing import Dict, List, Set, Union
import ipaddress
from functools import lru_cache

# Type aliases
AddressObject = Union[ipaddress.IPv4Network, ipaddress.IPv6Network, str]  # "any" is allowed
AddressGroup = List[str]  # Can contain AOs or AGs

SecurityRule = Dict[str, List[str]]  # Placeholder for actual SecurityRule TypedDict

def resolve_security_rule_addresses(
    rules: List[SecurityRule],
    address_objects: Dict[str, List[AddressObject]],
    address_groups: Dict[str, AddressGroup]
) -> List[SecurityRule]:
    """Resolve Address Objects (AO) and Address Groups (AG) for all security rules."""
    resolved_rules = []

    for rule in rules:
        resolved_rule = rule.copy()
        resolved_rule["source_addresses"] = resolve_addresses(tuple(rule["source_addresses"]), address_objects, address_groups)
        resolved_rule["destination_addresses"] = resolve_addresses(tuple(rule["destination_addresses"]), address_objects, address_groups)
        resolved_rules.append(resolved_rule)

    return resolved_rules

@lru_cache(maxsize=None)
def resolve_addresses(
    input_addresses: Tuple[str, ...],
    address_objects: Dict[str, List[AddressObject]],
    address_groups: Dict[str, AddressGroup]
) -> Set[AddressObject]:
    """Resolve Address Objects (AO) and Address Groups (AG) to a set of actual IP addresses."""
    resolved: Set[AddressObject] = set()
    stack = list(input_addresses)
    visited = set()  # To prevent circular references

    while stack:
        current = stack.pop()

        if current in visited:
            continue
        visited.add(current)

        if current == "any":
            resolved.add("any")
            continue

        if current in address_objects:
            resolved.update(address_objects[current])
        elif current in address_groups:
            stack.extend(address_groups[current])  # Expand AG contents
        else:
            raise ValueError(f"Unknown address object or group: {current}")

    return resolved

# Example data
address_objects = {
    "AO1": [ipaddress.ip_network("192.168.1.0/24")],
    "AO2": [ipaddress.ip_network("10.0.0.0/8")],
    "AO3": [ipaddress.ip_network("2001:db8::/32")],
}

address_groups = {
    "AG1": ["AO1", "AO2"],
    "AG2": ["AG1", "AO3"],
    "AG3": ["AG2", "AG1"],  # Nested AGs
}

# Example security rules
security_rules = [
    {"name": "Rule1", "source_addresses": ["AG3"], "destination_addresses": ["AO2"]},
    {"name": "Rule2", "source_addresses": ["AO1"], "destination_addresses": ["AG1"]},
]

# Resolve addresses in rules
resolved_rules = resolve_security_rule_addresses(security_rules, address_objects, address_groups)
for rule in resolved_rules:
    print(rule)
```

## Unit tests

```python

import pytest
import ipaddress
from typing import List
from your_module import (  # Replace 'your_module' with the actual module name
    SecurityRule,
    is_shadowing,
    find_shadowed_rules,
    check_action,
    check_application,
    check_source_zone,
    check_destination_zone,
    check_source_address,
    check_destination_address,
    check_ports,
)

@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        ({"action": "allow"}, {"action": "allow"}, True),
        ({"action": "allow"}, {"action": "deny"}, False),
    ],
)
def test_check_action(rule, preceding_rule, expected):
    assert check_action(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        ({"applications": ["http"]}, {"applications": ["http", "https"]}, True),
        ({"applications": ["ftp"]}, {"applications": ["http"]}, False),
        ({"applications": ["any"]}, {"applications": ["http"]}, False),
        ({"applications": ["http"]}, {"applications": ["any"]}, True),
    ],
)
def test_check_application(rule, preceding_rule, expected):
    assert check_application(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        ({"source_zones": ["internal"]}, {"source_zones": ["internal"]}, True),
        ({"source_zones": ["internal"]}, {"source_zones": ["external"]}, False),
        ({"source_zones": ["internal"]}, {"source_zones": ["any"]}, True),
    ],
)
def test_check_source_zone(rule, preceding_rule, expected):
    assert check_source_zone(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        ({"destination_zones": ["dmz"]}, {"destination_zones": ["dmz"]}, True),
        ({"destination_zones": ["dmz"]}, {"destination_zones": ["internal"]}, False),
        ({"destination_zones": ["dmz"]}, {"destination_zones": ["any"]}, True),
    ],
)
def test_check_destination_zone(rule, preceding_rule, expected):
    assert check_destination_zone(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        (
            {"source_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            {"source_addresses": [ipaddress.IPv4Network("10.0.0.0/16")]},
            True,
        ),
        (
            {"source_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            {"source_addresses": [ipaddress.IPv4Network("192.168.1.0/24")]},
            False,
        ),
        (
            {"source_addresses": ["any"]},
            {"source_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            False,
        ),
        (
            {"source_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            {"source_addresses": ["any"]},
            True,
        ),
    ],
)
def test_check_source_address(rule, preceding_rule, expected):
    assert check_source_address(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        (
            {"destination_addresses": [ipaddress.IPv4Network("192.168.1.0/24")]},
            {"destination_addresses": [ipaddress.IPv4Network("192.168.1.0/16")]},
            True,
        ),
        (
            {"destination_addresses": [ipaddress.IPv4Network("192.168.1.0/24")]},
            {"destination_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            False,
        ),
        (
            {"destination_addresses": ["any"]},
            {"destination_addresses": [ipaddress.IPv4Network("192.168.1.0/24")]},
            False,
        ),
        (
            {"destination_addresses": [ipaddress.IPv4Network("192.168.1.0/24")]},
            {"destination_addresses": ["any"]},
            True,
        ),
    ],
)
def test_check_destination_address(rule, preceding_rule, expected):
    assert check_destination_address(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        ({"services": ["tcp/80"]}, {"services": ["tcp/80", "tcp/443"]}, True),
        ({"services": ["tcp/22"]}, {"services": ["tcp/80"]}, False),
        ({"services": ["application-default"]}, {"services": ["tcp/80"]}, False),
        ({"services": ["tcp/80"]}, {"services": ["application-default"]}, True),
    ],
)
def test_check_ports(rule, preceding_rule, expected):
    assert check_ports(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rule, preceding_rule, expected",
    [
        (
            SecurityRule(
                name="Rule1",
                action="allow",
                source_zones=["internal"],
                destination_zones=["dmz"],
                source_addresses=[ipaddress.IPv4Network("10.0.0.0/24")],
                destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                applications=["http"],
                services=["tcp/80"],
            ),
            SecurityRule(
                name="Rule2",
                action="allow",
                source_zones=["internal"],
                destination_zones=["dmz"],
                source_addresses=[ipaddress.IPv4Network("10.0.0.0/16")],
                destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                applications=["http", "https"],
                services=["tcp/80", "tcp/443"],
            ),
            True,
        ),
        (
            SecurityRule(
                name="Rule1",
                action="allow",
                source_zones=["internal"],
                destination_zones=["dmz"],
                source_addresses=[ipaddress.IPv4Network("10.0.0.0/24")],
                destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                applications=["http"],
                services=["tcp/80"],
            ),
            SecurityRule(
                name="Rule2",
                action="deny",
                source_zones=["internal"],
                destination_zones=["dmz"],
                source_addresses=[ipaddress.IPv4Network("10.0.0.0/16")],
                destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                applications=["http", "https"],
                services=["tcp/80", "tcp/443"],
            ),
            False,
        ),
    ],
)
def test_is_shadowing(rule, preceding_rule, expected):
    assert is_shadowing(rule, preceding_rule) == expected


@pytest.mark.parametrize(
    "rules, expected",
    [
        (
            [
                SecurityRule(
                    name="Rule1",
                    action="allow",
                    source_zones=["internal"],
                    destination_zones=["dmz"],
                    source_addresses=[ipaddress.IPv4Network("10.0.0.0/16")],
                    destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                    applications=["http"],
                    services=["tcp/80"],
                ),
                SecurityRule(
                    name="Rule2",
                    action="allow",
                    source_zones=["internal"],
                    destination_zones=["dmz"],
                    source_addresses=[ipaddress.IPv4Network("10.0.0.0/24")],
                    destination_addresses=[ipaddress.IPv4Network("192.168.1.0/24")],
                    applications=["http"],
                    services=["tcp/80"],
                ),
            ],
            [{"shadowed_rule": "Rule2", "shadowing_rules": ["Rule1"]}],
        ),
    ],
)
def test_find_shadowed_rules(rules: List[SecurityRule], expected):
    result = find_shadowed_rules(rules)
    assert [{**shadowed, "shadowed_rule": shadowed["shadowed_rule"]["name"], "shadowing_rules": [r["name"] for r in shadowed["shadowing_rules"]]} for shadowed in result] == expected

```
