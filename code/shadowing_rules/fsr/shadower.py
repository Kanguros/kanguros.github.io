import logging

from .check import CheckOutput, RuleCheckFunction
from .models import SecurityRule

logger = logging.getLogger(__name__)


def run_checks_on_rules(
    rules: list[SecurityRule], checks: list[RuleCheckFunction]
) -> dict[str, dict[str, dict[str, CheckOutput]]]:
    """Finds security rules that are shadowed by preceding rules.

    Iterates through a list of security rules and identifies rules that
    are completely covered by one or more preceding rules.

    Args:
        rules: A list of security rules to analyze.
        checks: A list of check functions to determine shadowing.



    """
    results = {}
    rules_count = len(rules)

    for i, rule in enumerate(rules):
        cid = f"[{i + 1}/{rules_count}][{rule.name}]"

        logger.info(f"{cid} Checking rule against {i} preceding Rules")

        preceding_results = {}
        for j in range(i):
            preceding_rule = rules[j]
            checks_results = {
                check_func.__name__: check_func(rule, preceding_rule)
                for check_func in checks
            }
            preceding_results[preceding_rule.name] = checks_results

        logger.info(f"{cid} Checking rule finished.")
        results[rule.name] = preceding_results

    logger.info("Shadowed rules detection complete")
    return results
