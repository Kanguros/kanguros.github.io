import ipaddress
from typing import Callable, Literal, Union

from pydantic import BaseModel

KeywordAny = Literal["any"]
KeywordAppDefault = Literal["application-default"]


class SecurityRule(BaseModel):
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
    services: Union[
        list[str], list[Literal[KeywordAny]], list[KeywordAppDefault]
    ]


RuleCheckFunction = Callable[[SecurityRule, SecurityRule], bool]
