from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pgtype_status import PgtypeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PgtypeJSONB")


@_attrs_define
class PgtypeJSONB:
    """
    Attributes:
        bytes_ (Union[Unset, List[int]]):
        status (Union[Unset, PgtypeStatus]):
    """

    bytes_: Union[Unset, List[int]] = UNSET
    status: Union[Unset, PgtypeStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bytes_: Union[Unset, List[int]] = UNSET
        if not isinstance(self.bytes_, Unset):
            bytes_ = self.bytes_

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bytes_ = cast(List[int], d.pop("bytes", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PgtypeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PgtypeStatus(_status)

        pgtype_jsonb = cls(
            bytes_=bytes_,
            status=status,
        )

        pgtype_jsonb.additional_properties = d
        return pgtype_jsonb

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
