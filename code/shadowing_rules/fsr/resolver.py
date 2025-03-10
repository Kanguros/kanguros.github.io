from typing import Union

from .models import AddressGroup, AddressObject, SecurityRule


class Resolver:
    def __init__(
        self,
        address_objects: list[AddressObject],
        address_groups: list[AddressGroup],
    ):
        self.address_objects = {ao.name: ao for ao in address_objects}
        self.address_groups = {ag.name: set(ag.static) for ag in address_groups}
        self.resolved_cache: dict[
            Union[str, tuple[str]], set[AddressObject]
        ] = {}

    def resolve_addresses(
        self, input_addresses: set[str]
    ) -> set[AddressObject]:
        """
        Resolve a list of address names into actual AddressObjects.

        - Expands Address Groups (AG) recursively.
        - Converts Address Objects (AO) into IP networks.
        """
        resolved = set()
        stack = list(input_addresses)
        visited = set()

        while stack:
            current = stack.pop()

            if current in visited:
                continue
            visited.add(current)

            if current == "any":
                resolved.add("any")
                continue

            if current in self.resolved_cache:
                resolved.update(self.resolved_cache[current])
                continue

            if current in self.address_objects:
                resolved.add(self.address_objects[current])
                self.resolved_cache[current] = {self.address_objects[current]}
            elif current in self.address_groups:
                stack.extend(self.address_groups[current])
            else:
                raise ValueError(f"Unknown address object or group: {current}")

        self.resolved_cache[tuple(input_addresses)] = resolved
        return resolved


def resolve_rules_addresses(
    rules: list[SecurityRule],
    address_objects: list[AddressObject],
    address_groups: list[AddressGroup],
) -> list[SecurityRule]:
    resolver = Resolver(address_objects, address_groups)
    for rule in rules:
        rule.source_addresses_ip = resolver.resolve_addresses(
            rule.source_addresses
        )
        rule.destination_addresses_ip = resolver.resolve_addresses(
            rule.destination_addresses
        )
    return rules
