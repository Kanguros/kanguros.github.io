from typing import TYPE_CHECKING, Literal, Optional, Union

from pydantic import AliasChoices, AliasPath, BaseModel, Field
from pydantic.networks import IPv4Network
from typing_extensions import Self

from .utils import load_json

if TYPE_CHECKING:
    from pathlib import Path

KeywordAny = Literal["any"]
ValueAny = set[KeywordAny]
KeywordAppDefault = Literal["application-default"]
ValueAppDefault = set[KeywordAppDefault]
SetStr = set[str]
Action = Literal["allow", "deny", "monitor"]

# noqa: E731
Alias = lambda attr, name: AliasChoices(  # noqa: E731
    AliasPath(name, "member"), attr
)
"""Utility one-line function to handle nested data in attribute"""


class MainModel(BaseModel):
    """Base class for all data models. Contain shared methods."""

    @classmethod
    def load_from_json(cls, file_path: Union[str, "Path"]) -> list[Self]:
        data = load_json(file_path)
        return cls.load_many(data)

    @classmethod
    def load_many(cls, data: list[dict]) -> list[Self]:
        return [cls(**item) for item in data]


class SecurityRule(MainModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    """Name of a rule."""
    action: Action
    source_zones: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("source_zones", "from")
    )
    destination_zones: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("destination_zones", "to")
    )
    """Set of destination zones or 'any' to match traffic destined to."""

    source_addresses: Union[ValueAny, SetStr] = Field(
        validation_alias=Alias("source_addresses", "source")
    )
    """Set of source address objects/groups or 'any' to match traffic from specific IP addresses or subnets."""

    destination_addresses: Union[ValueAny, SetStr] = Field(
        validation_alias=Alias("destination_addresses", "destination")
    )
    """Set of destination address objects/groups or 'any' to match traffic to specific IP addresses or subnets."""

    applications: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("applications", "application")
    )
    """Set of applications or 'any' that the rule applies to."""

    services: Union[SetStr, ValueAny, ValueAppDefault] = Field(
        validation_alias=Alias("services", "service")
    )
    """Set of services (e.g., TCP/UDP ports) or 'any'/'application-default' that the rule applies to."""

    category: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("category", "category")
    )
    """Set of URL categories or 'any' that the rule applies to."""

    source_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )
    """Resolved set of source IP address networks or 'any' after address objects/groups are expanded."""

    destination_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )
    """Resolved set of destination IP address networks or 'any' after address objects/groups are expanded."""


class AddressGroup(MainModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    description: str = Field(default="")
    tag: SetStr = Field(default_factory=set)
    static: SetStr = Field(default_factory=set)


class AddressObject(MainModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    ip_netmask: str = Field(
        ..., validation_alias=AliasChoices("ip_netmask", "ip-netmask")
    )
    value: Optional[IPv4Network] = Field(None)
