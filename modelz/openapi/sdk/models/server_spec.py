from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_spec_labels import ServerSpecLabels


T = TypeVar("T", bound="ServerSpec")


@_attrs_define
class ServerSpec:
    """
    Attributes:
        labels (Union[Unset, ServerSpecLabels]):
        name (Union[Unset, str]):
    """

    labels: Union[Unset, "ServerSpecLabels"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_spec_labels import ServerSpecLabels

        d = src_dict.copy()
        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, ServerSpecLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServerSpecLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        server_spec = cls(
            labels=labels,
            name=name,
        )

        server_spec.additional_properties = d
        return server_spec

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
