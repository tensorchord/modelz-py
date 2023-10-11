from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InstanceStatus")


@_attrs_define
class InstanceStatus:
    """
    Attributes:
        created_at (Union[Unset, str]):
        message (Union[Unset, str]):
        phase (Union[Unset, str]):
        reason (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    phase: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        message = self.message
        phase = self.phase
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if message is not UNSET:
            field_dict["message"] = message
        if phase is not UNSET:
            field_dict["phase"] = phase
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("createdAt", UNSET)

        message = d.pop("message", UNSET)

        phase = d.pop("phase", UNSET)

        reason = d.pop("reason", UNSET)

        instance_status = cls(
            created_at=created_at,
            message=message,
            phase=phase,
            reason=reason,
        )

        instance_status.additional_properties = d
        return instance_status

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
