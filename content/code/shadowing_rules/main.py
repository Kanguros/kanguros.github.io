import ipaddress
from typing import Callable, Literal, TypedDict, Union

KeywordAny = Literal["any"]
KeywordAppDefault = Literal["application-default"]


class SecurityRule(TypedDict):
    name: str
    action: Literal["allow", "deny"]
    source_zones: Union[list[str], list[KeywordAny]]
    destination_zones: Union[list[str], list[KeywordAny]]
    source_addresses: Union[
        list[ipaddress.IPv4Network],
        list[ipaddress.IPv6Network],
        list[KeywordAny],
    ]
    destination_addresses: Union[
        list[ipaddress.IPv4Network],
        list[ipaddress.IPv6Network],
        list[KeywordAny],
    ]
    applications: Union[list[str], list[KeywordAny]]
    services: Union[list[str], list[Literal[KeywordAny, KeywordAppDefault]]]


RuleCheckFunction = Callable[[SecurityRule, SecurityRule], bool]


def check_action(rule: SecurityRule, preceding_rule: SecurityRule) -> bool:
    """Checks if the action is the same in both rules."""
    return rule["action"] == preceding_rule["action"]


def check_application(rule: SecurityRule, preceding_rule: SecurityRule) -> bool:
    """Checks if the rule's applications are the same or a subset of the preceding rule's applications."""
    rule_apps = set(rule["applications"])
    preceding_apps = set(preceding_rule["applications"])

    if "any" in preceding_apps:
        return True
    if "any" in rule_apps:
        return "any" in preceding_apps
    return rule_apps.issubset(preceding_apps)


def check_source_zone(rule: SecurityRule, preceding_rule: SecurityRule) -> bool:
    """Checks if the source zones are identical or if the preceding rule allows any zone."""
    return (
        rule["source_zones"] == preceding_rule["source_zones"]
        or "any" in preceding_rule["source_zones"]
    )


def check_destination_zone(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> bool:
    """Checks if the destination zones are identical or if the preceding rule allows any zone."""
    return (
        rule["destination_zones"] == preceding_rule["destination_zones"]
        or "any" in preceding_rule["destination_zones"]
    )


def check_source_address(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> bool:
    """Checks if the source addresses are identical, allow any, or are subsets of the preceding rule's addresses."""
    if "any" in preceding_rule["source_addresses"]:
        return True

    for addr in rule["source_addresses"]:
        if not any(
            addr.subnet_of(net) for net in preceding_rule["source_addresses"]
        ):
            return False

    return True


def check_destination_address(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> bool:
    """Checks if the destination addresses are
    identical, allow any, or are subsets of the preceding rule's addresses."""
    if "any" in preceding_rule["destination_addresses"]:
        return True

    for addr in rule["destination_addresses"]:
        if not any(
            addr.subnet_of(net)
            for net in preceding_rule["destination_addresses"]
        ):
            return False

    return True


def check_ports(rule: SecurityRule, preceding_rule: SecurityRule) -> bool:
    """Checks if the rule's ports are the same
    or a subset of the preceding rule's ports."""
    return (
        rule["services"] == preceding_rule["services"]
        or "application-default" in preceding_rule["services"]
        or set(rule["services"]).issubset(set(preceding_rule["services"]))
    )


CHECKS: list[RuleCheckFunction] = [
    check_action,
    check_application,
    check_source_zone,
    check_destination_zone,
    check_source_address,
    check_destination_address,
    check_ports,
]


def is_shadowing(
    rule: SecurityRule,
    preceding_rule: SecurityRule,
    checks: list[RuleCheckFunction],
) -> bool:
    """Checks if a security rule is shadowed by a preceding rule.

    A rule is shadowed if all checks in the provided list return True, meaning
    the preceding rule covers all aspects of the given rule.

    Args:
        rule (SecurityRule): The security rule being checked for shadowing.
        preceding_rule (SecurityRule): The rule that may be shadowing the given rule.
        checks (list[RuleCheckFunction]): A list of functions that validate different rule attributes.

    Returns:
        bool: True if `rule` is shadowed by `preceding_rule`, otherwise False.

    Example:
        >>> rule1 = {"name": "Allow Web", "action": "allow", "application": ["web-browsing"], ...}
        >>> rule2 = {"name": "Allow All", "action": "allow", "application": ["any"], ...}
        >>> is_shadowing(rule1, rule2, CHECKS)
        True
    """
    for check in checks:
        if not check(rule, preceding_rule):
            return False
    return True


def find_shadowed_rules(
    rules: list[SecurityRule], checks: list[RuleCheckFunction]
) -> list[tuple[SecurityRule, list[SecurityRule]]]:
    """Finds security rules that are shadowed by preceding rules.

    Iterates through a list of firewall security rules and identifies rules that
    are completely covered by one or more preceding rules.

    Args:
        rules (list[SecurityRule]): A list of security rules to analyze.
        checks (list[RuleCheckFunction]): A list of check functions to determine shadowing.

    Returns:
        list[tuple[SecurityRule, list[SecurityRule]]]: A list of tuples where each tuple contains:
            - The shadowed rule.
            - A list of preceding rules that are shadowing it.

    Example:
        >>> rules = [
        ...     {"name": "Allow All", "action": "allow", "application": ["any"], ...},
        ...     {"name": "Allow Web", "action": "allow", "application": ["web-browsing"], ...},
        ... ]
        >>> find_shadowed_rules(rules, CHECKS)
        [(rule2, [rule1])]
    """
    shadowed_rules: list[tuple[SecurityRule, list[SecurityRule]]] = []

    for i, rule in enumerate(rules):
        shadowing_rules = []
        for j in range(i):
            if is_shadowing(rule, rules[j], checks):
                shadowing_rules.append(rules[j])

        if shadowing_rules:
            shadowed_rules.append((rule, shadowing_rules))

    return shadowed_rules
