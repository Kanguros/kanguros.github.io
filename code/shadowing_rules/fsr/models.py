from typing import List, Literal, Optional, Union

from pydantic import AliasChoices, AliasPath, BaseModel, Field, RootModel
from pydantic.networks import IPv4Network

KeywordAny = Literal["any"]
ValueAny = set[KeywordAny]
KeywordAppDefault = Literal["application-default"]
ValueAppDefault = set[KeywordAppDefault]
SetStr = set[str]
Action = Literal["allow", "deny", "monitor"]

Alias = lambda attr_name, raw_name: AliasChoices(
    attr_name, AliasPath(raw_name, "member")
)  # noqa: E731


class SecurityRule(BaseModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    """Name of a rule."""
    action: Action
    source_zones: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("source_zones", "from")
    )
    destination_zones: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("destination_zones", "to")
    )
    source_addresses: Union[ValueAny, SetStr] = Field(
        validation_alias=Alias("source_addresses", "source")
    )
    destination_addresses: Union[ValueAny, SetStr] = Field(
        validation_alias=Alias("destination_addresses", "destination")
    )
    applications: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("applications", "application")
    )
    services: Union[SetStr, ValueAny, ValueAppDefault] = Field(
        validation_alias=Alias("services", "service")
    )
    category: Union[SetStr, ValueAny] = Field(
        validation_alias=Alias("category", "category")
    )
    source_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )
    destination_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )


SecurityRules = RootModel[list[SecurityRule]]


class AddressGroup(BaseModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    description: str = ""
    tag: SetStr = Field(default_factory=set)
    static: SetStr = Field(default_factory=set)


AddressGroups = RootModel[list[AddressGroup]]


class AddressObject(BaseModel):
    name: str = Field(..., validation_alias=AliasChoices("name", "@name"))
    ip_netmask: str = Field(
        ..., validation_alias=AliasChoices("ip_netmask", "ip-netmask")
    )
    value: Optional[IPv4Network] = Field(None)


AddressObjects = RootModel[list[AddressObject]]
