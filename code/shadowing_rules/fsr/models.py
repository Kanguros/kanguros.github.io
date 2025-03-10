from typing import Any, Literal, Union

from pydantic import BaseModel, Field, AliasPath, AliasChoices
from pydantic.networks import IPv4Network
from typing_extensions import Self

KeywordAny = Literal["any"]
ValueAny = set[KeywordAny]
KeywordAppDefault = Literal["application-default"]
ValueAppDefault = set[KeywordAppDefault]
SetStr = set[str]
Action = Literal["allow", "deny", "monitor"]

Alias = lambda attr_name, raw_name: AliasChoices(attr_name, AliasPath(raw_name, 'member'))


class SecurityRule(BaseModel):
    name: str
    """Name of a rule."""
    action: Action
    source_zones: Union[SetStr, ValueAny] = Field(validation_alias=Alias("source_zones", "from"))
    destination_zones: Union[SetStr, ValueAny] = Field(validation_alias=Alias("source_zones", "from"))
    source_addresses: Union[ValueAny, SetStr] = Field(validation_alias=Alias("source_zones", "from"))
    source_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )
    destination_addresses: Union[ValueAny, SetStr] = Field(validation_alias=Alias("source_zones", "from"))
    destination_addresses_ip: Union[set[IPv4Network], ValueAny] = Field(
        default_factory=set
    )
    applications: Union[SetStr, ValueAny] = Field(validation_alias=Alias("source_zones", "from"))
    services: Union[SetStr, set[Literal[KeywordAny]], set[KeywordAppDefault]] = Field(
        validation_alias=Alias("source_zones", "from"))
    category: Union[SetStr, ValueAny] = Field(validation_alias=Alias("source_zones", "from"))

    @classmethod
    def load(cls, data: dict[str, Any]) -> Self:
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
    def load_many(cls, data: list[dict]) -> list[Self]:
        return [cls.load(element) for element in data]


class AddressGroup(BaseModel):
    name: str
    description: str = ""
    tag: SetStr = Field(default_factory=set)
    static: SetStr = Field(default_factory=set)

    @classmethod
    def load(cls, data: dict) -> Self:
        return cls(
            name=data.get("@name"),
            description=data.get("description", ""),
            tag=data.get("tag", []),
            static=data.get("static", []),
        )

    @classmethod
    def load_many(cls, items: list[dict]) -> list[Self]:
        return [cls.load(item) for item in items]


class AddressObject(BaseModel):
    name: str
    ip_netmask: IPv4Network

    @classmethod
    def load(cls, data: dict) -> Self:
        ip_netmask = data.get("ip-netmask")
        if not ip_netmask:
            raise NotImplementedError(
                "Only Address Objects with ip-netmask are implemented"
            )
        ip_netmask = IPv4Network(ip_netmask, strict=False)
        return cls(name=data.get("@name"), ip_netmask=ip_netmask)

    @classmethod
    def load_many(cls, items: list[dict]) -> list[Self]:
        instances = []
        for item in items:
            try:
                instances.append(cls.load(item))
            except NotImplementedError:
                pass
        return instances
