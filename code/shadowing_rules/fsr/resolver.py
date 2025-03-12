from ipaddress import IPv4Network
from typing import Union

from .models import AddressGroup, AddressObject, SecurityRule


class Resolver:
    def __init__(
        self,
        address_objects: list[AddressObject],
        address_groups: list[AddressGroup],
    ):
        self.address_objects = {
            ao.name: ao.ip_netmask for ao in address_objects
        }
        self.address_groups = {ag.name: set(ag.static) for ag in address_groups}
        self.resolved_cache: dict[Union[str, tuple[str]], set[IPv4Network]] = {}

    def resolve_addresses(
        self, objects_name: set[str]
    ) -> Union[set[IPv4Network]]:
        """
        Resolve a list of address names into actual AddressObjects.

        - Expands Address Groups (AG) recursively.
        - Converts Address Objects (AO) into IP networks.
        """
        resolved = set()
        stack = list(objects_name)
        visited = set()

        while stack:
            current = stack.pop()

            if current in visited:
                continue
            visited.add(current)

            if current in self.resolved_cache:
                resolved.update(self.resolved_cache[current])
                continue

            if current in self.address_groups:
                stack.extend(self.address_groups[current])
                continue

            if current in self.address_objects:
                ip_address = IPv4Network(
                    self.address_objects[current], strict=False
                )
                resolved.add(ip_address)
                self.resolved_cache[current] = {ip_address}
                continue

            raise ValueError(f"Unknown address object or group: {current}")

        self.resolved_cache[tuple(objects_name)] = resolved
        return resolved

    def rule_addresses(self, rule: SecurityRule) -> SecurityRule:
        if rule.source_addresses != {"any"}:
            rule.source_addresses_ip = self.resolve_addresses(
                rule.source_addresses
            )

        if rule.destination_addresses != {"any"}:
            rule.destination_addresses_ip = self.resolve_addresses(
                rule.destination_addresses
            )

        return rule


def resolve_rules_addresses(
    rules: list[SecurityRule],
    address_objects: list[AddressObject],
    address_groups: list[AddressGroup],
) -> list[SecurityRule]:
    resolver = Resolver(address_objects, address_groups)
    return [resolver.rule_addresses(rule) for rule in rules]
