import ipaddress
from functools import cache
from typing import Union

# Type aliases
AddressObject = Union[
    ipaddress.IPv4Network, ipaddress.IPv6Network, str
]  # "any" is allowed
AddressGroup = list[str]  # Can contain AOs or AGs

SecurityRule = dict[
    str, list[str]
]  # Placeholder for actual SecurityRule Typeddict


def resolve_security_rule_addresses(
    rules: list[SecurityRule],
    address_objects: dict[str, list[AddressObject]],
    address_groups: dict[str, AddressGroup],
) -> list[SecurityRule]:
    """Resolve Address Objects (AO) and Address Groups (AG) for all security rules."""
    resolved_rules = []

    for rule in rules:
        resolved_rule = rule.copy()
        resolved_rule["source_addresses"] = resolve_addresses(
            tuple(rule["source_addresses"]), address_objects, address_groups
        )
        resolved_rule["destination_addresses"] = resolve_addresses(
            tuple(rule["destination_addresses"]),
            address_objects,
            address_groups,
        )
        resolved_rules.append(resolved_rule)

    return resolved_rules


@cache
def resolve_addresses(
    input_addresses: tuple[str, ...],
    address_objects: dict[str, list[AddressObject]],
    address_groups: dict[str, AddressGroup],
) -> set[AddressObject]:
    """Resolve Address Objects (AO) and Address Groups (AG) to a set of actual IP addresses."""
    resolved: set[AddressObject] = set()
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
    {
        "name": "Rule1",
        "source_addresses": ["AG3"],
        "destination_addresses": ["AO2"],
    },
    {
        "name": "Rule2",
        "source_addresses": ["AO1"],
        "destination_addresses": ["AG1"],
    },
]

# Resolve addresses in rules
resolved_rules = resolve_security_rule_addresses(
    security_rules, address_objects, address_groups
)
for rule in resolved_rules:
    print(rule)
