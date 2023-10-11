from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_role import MemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamMemberEditableFields")


@_attrs_define
class TeamMemberEditableFields:
    """
    Attributes:
        role (Union[Unset, MemberRole]):
    """

    role: Union[Unset, MemberRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _role = d.pop("role", UNSET)
        role: Union[Unset, MemberRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = MemberRole(_role)

        team_member_editable_fields = cls(
            role=role,
        )

        team_member_editable_fields.additional_properties = d
        return team_member_editable_fields

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
