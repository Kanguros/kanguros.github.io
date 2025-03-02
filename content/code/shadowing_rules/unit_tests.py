import ipaddress

import pytest

from .main import (
    SecurityRule,
    check_action,
    check_application,
    check_destination_address,
    check_destination_zone,
    check_ports,
    check_source_address,
    check_source_zone,
    find_shadowed_rules,
    is_shadowing,
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
        (
            {"destination_zones": ["dmz"]},
            {"destination_zones": ["internal"]},
            False,
        ),
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
            {
                "destination_addresses": [
                    ipaddress.IPv4Network("192.168.1.0/24")
                ]
            },
            {
                "destination_addresses": [
                    ipaddress.IPv4Network("192.168.1.0/16")
                ]
            },
            True,
        ),
        (
            {
                "destination_addresses": [
                    ipaddress.IPv4Network("192.168.1.0/24")
                ]
            },
            {"destination_addresses": [ipaddress.IPv4Network("10.0.0.0/24")]},
            False,
        ),
        (
            {"destination_addresses": ["any"]},
            {
                "destination_addresses": [
                    ipaddress.IPv4Network("192.168.1.0/24")
                ]
            },
            False,
        ),
        (
            {
                "destination_addresses": [
                    ipaddress.IPv4Network("192.168.1.0/24")
                ]
            },
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
        (
            {"services": ["application-default"]},
            {"services": ["tcp/80"]},
            False,
        ),
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
                    destination_addresses=[
                        ipaddress.IPv4Network("192.168.1.0/24")
                    ],
                    applications=["http"],
                    services=["tcp/80"],
                ),
                SecurityRule(
                    name="Rule2",
                    action="allow",
                    source_zones=["internal"],
                    destination_zones=["dmz"],
                    source_addresses=[ipaddress.IPv4Network("10.0.0.0/24")],
                    destination_addresses=[
                        ipaddress.IPv4Network("192.168.1.0/24")
                    ],
                    applications=["http"],
                    services=["tcp/80"],
                ),
            ],
            [{"shadowed_rule": "Rule2", "shadowing_rules": ["Rule1"]}],
        ),
    ],
)
def test_find_shadowed_rules(rules: list[SecurityRule], expected):
    result = find_shadowed_rules(rules)
    assert [
        {
            **shadowed,
            "shadowed_rule": shadowed["shadowed_rule"]["name"],
            "shadowing_rules": [r["name"] for r in shadowed["shadowing_rules"]],
        }
        for shadowed in result
    ] == expected
