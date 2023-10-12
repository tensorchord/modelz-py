from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_ping_response_200_additional_property import (
        GetPingResponse200AdditionalProperty,
    )


T = TypeVar("T", bound="GetPingResponse200")


@_attrs_define
class GetPingResponse200:
    """ """

    additional_properties: Dict[
        str, "GetPingResponse200AdditionalProperty"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_ping_response_200_additional_property import (
            GetPingResponse200AdditionalProperty,
        )

        d = src_dict.copy()
        get_ping_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetPingResponse200AdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        get_ping_response_200.additional_properties = additional_properties
        return get_ping_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "GetPingResponse200AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: "GetPingResponse200AdditionalProperty"
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
