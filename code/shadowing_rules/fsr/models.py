import ipaddress
from typing import Any, Literal, Union

from pydantic import BaseModel
from typing_extensions import Self

KeywordAny = Literal["any"]
KeywordAppDefault = Literal["application-default"]


class SecurityRule(BaseModel):
    name: str
    action: Literal["allow", "deny"]
    source_zones: Union[list[str], list[KeywordAny]]
    destination_zones: Union[list[str], list[KeywordAny]]
    source_addresses: Union[list[KeywordAny], list[str]]
    source_addresses_ip: Union[
        list[ipaddress.IPv4Network],
        list[ipaddress.IPv6Network],
        list[KeywordAny],
    ] = []
    destination_addresses: Union[list[KeywordAny], list[str]]
    destination_addresses_ip: Union[
        list[ipaddress.IPv4Network],
        list[ipaddress.IPv6Network],
        list[KeywordAny],
    ] = []
    applications: Union[list[str], list[KeywordAny]]
    services: Union[
        list[str], list[Literal[KeywordAny]], list[KeywordAppDefault]
    ]
    category: Union[list[str], list[KeywordAny]]

    @classmethod
    def from_entry(cls, data: dict[str, Any]) -> Self:
        rule_data = {
            "name": data.get("@name"),
            "action": data.get("action"),
        }
        keys_attributes = (
            ("from", "source_zones"),
            ("to", "destination_zones"),
            ("source", "source_addresses"),
            ("destination", "destination_addresses"),
            ("application", "applications"),
            ("category", "category"),
            ("service", "services"),
        )
        for key, attribute in keys_attributes:
            rule_data[attribute] = data.get(key, {}).get("member", [])
        return cls(**rule_data)

    @classmethod
    def from_entries(cls, data: list[dict]) -> list[Self]:
        return [cls.from_entry(element) for element in data]
