import logging
from typing import Callable

from .models import SecurityRule

Result = tuple[bool, str]
RuleCheckFunction = Callable[[SecurityRule, SecurityRule], Result]
"""Typing for a ``check`` type of function"""

ValueAny = set("any")
"""Helper variable to represent ``list['any']`` in order to avoid writing it multiple times."""

logger = logging.getLogger(__name__)


def check_action(rule: SecurityRule, preceding_rule: SecurityRule) -> Result:
    """Checks if the action is the same in both rules."""
    result = rule.action == preceding_rule.action
    message = "Actions match" if result else "Actions differ"
    return result, message


def check_source_zone(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    """Checks the source zones of the preceding rule."""
    if rule.source_zones == preceding_rule.source_zones:
        return True, "Source zones are the same"

    if preceding_rule.source_zones.issubset(rule.source_zones):
        return True, "Preceding rule source zones cover rule's source zones"

    if ValueAny == preceding_rule.source_zones:
        return True, "Preceding rule source zones is 'any'"

    return False, "Source zones differ"


def check_destination_zone(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    """Checks the destination zones of the preceding rule."""
    if rule.destination_zones == preceding_rule.destination_zones:
        return True, "Source zones are the same"

    if preceding_rule.destination_zones.issubset(rule.destination_zones):
        return True, "Preceding rule source zones cover rule's source zones"

    if ValueAny == preceding_rule.destination_zones:
        return True, "Preceding rule source zones is 'any'"

    return False, "Source zones differ"


def check_source_address(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    """Checks the source addresses of the preceding rule's addresses."""
    if ValueAny == preceding_rule.source_addresses:
        return True, "Preceding rule allows any source address"

    for addr in rule.source_addresses_ip:
        if not any(
            addr.subnet_of(net) for net in preceding_rule.source_addresses_ip
        ):
            return False, f"Address {addr} is not covered by preceding rule"

    return True, "Preceding rule covers all source addresses"


def check_destination_address(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    """Checks if the destination addresses are
    identical, allow any, or are subsets of the preceding rule's addresses."""
    if ValueAny == preceding_rule.destination_addresses:
        return True, "Preceding rule allows any destination address"

    for addr in rule.destination_addresses_ip:
        if not any(
            addr.subnet_of(net)
            for net in preceding_rule.destination_addresses_ip
        ):
            return False, f"Address {addr} is not covered by preceding rule"

    return True, "Preceding rule covers all destination addresses"


def check_application(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    """Checks the applications of the preceding rule."""
    rule_apps = rule.applications
    preceding_apps = preceding_rule.applications

    if ValueAny == preceding_apps:
        return True, "Preceding rule allows any application"
    if ValueAny == rule_apps:
        return "any" in preceding_apps, "Rule allows any application"
    if all(rule_app in preceding_apps for rule_app in rule_apps):
        return True, "Preceding rule contains rule's applications"
    return False, "Preceding rule does not contain all rule's applications"


def check_services(rule: SecurityRule, preceding_rule: SecurityRule) -> Result:
    """Checks if the rule's ports are the same
    or a subset of the preceding rule's ports."""
    if rule.services == preceding_rule.services:
        return True, "Preceding rule and rule's services are the same"
    if all(
        rule_service in preceding_rule.services
        for rule_service in rule.services
    ):
        return True, "Preceding rule contains rule's applications"
    return False, "Preceding rule does not contain all rule's applications"


def check_services_and_application(
    rule: SecurityRule, preceding_rule: SecurityRule
) -> Result:
    pass


CHECKS: list[RuleCheckFunction] = [
    check_action,
    check_application,
    check_source_zone,
    check_destination_zone,
    check_source_address,
    check_destination_address,
    check_services,
]


def find_shadowed_rules(
    rules: list[SecurityRule],
    checks: list[RuleCheckFunction],
):
    """Finds security rules that are shadowed by preceding rules.

    Iterates through a list of firewall security rules and identifies rules that
    are completely covered by one or more preceding rules.

    Args:
        rules (list[SecurityRule]): A list of security rules to analyze.
        checks (list[RuleCheckFunction]): A list of check functions to determine shadowing.

    """
    shadowed_rules = []
    rules_count = len(rules)
    logger.info("Starting shadowed Rules detection")
    logger.info(f"Number of Rules to check: {rules_count}")
    logger.info("Checks:")
    for check in checks:
        logger.info(f"- {check.__name__}")

    for i, rule in enumerate(rules, start=0):
        shadowing_rules = []
        cid = f"[{i + 1}/{rules_count}][{rule.name}]"
        logger.info(f"{cid} Checking rule against {i} preceding Rules")

        for j in range(i):
            preceding_rule = rules[j]

            checks_results = []
            for check_func in checks:
                result = check_func(rule, preceding_rule)
                checks_results.append(result)

            if all(result[0] for result in checks_results):
                shadowing_rules.append((preceding_rule, checks_results))

        if shadowing_rules:
            logger.info(f"{cid} Shadowed by {len(shadowing_rules)} rule(s)")
            shadowed_rules.append((rule, shadowing_rules))
        else:
            logger.info(f"{cid} Not shadowed")

    logger.info("Shadowed rules detection complete")
    return shadowed_rules
