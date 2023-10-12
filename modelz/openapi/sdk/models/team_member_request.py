from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.member_role import MemberRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamMemberRequest")


@_attrs_define
class TeamMemberRequest:
    """
    Attributes:
        email (str):
        member_id (Union[Unset, str]):
        role (Union[Unset, MemberRole]):
        team_id (Union[Unset, str]):
    """

    email: str
    member_id: Union[Unset, str] = UNSET
    role: Union[Unset, MemberRole] = UNSET
    team_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        member_id = self.member_id
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        team_id = self.team_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if role is not UNSET:
            field_dict["role"] = role
        if team_id is not UNSET:
            field_dict["team_id"] = team_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        member_id = d.pop("member_id", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, MemberRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = MemberRole(_role)

        team_id = d.pop("team_id", UNSET)

        team_member_request = cls(
            email=email,
            member_id=member_id,
            role=role,
            team_id=team_id,
        )

        team_member_request.additional_properties = d
        return team_member_request

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
