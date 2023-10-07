from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_member import TeamMember


T = TypeVar("T", bound="TeamSpec")


@_attrs_define
class TeamSpec:
    """
    Attributes:
        api_key (Union[Unset, str]):
        avatar_url (Union[Unset, str]): AvatarUrl is the avatar url of the team.
        email (Union[Unset, str]): Email is the email of the team.
        id (Union[Unset, str]): ID holds the unique identifier of the team.
        members (Union[Unset, List['TeamMember']]):
        name (Union[Unset, str]): Name is the name of the team.
    """

    api_key: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    members: Union[Unset, List["TeamMember"]] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key = self.api_key
        avatar_url = self.avatar_url
        email = self.email
        id = self.id
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if members is not UNSET:
            field_dict["members"] = members
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_member import TeamMember

        d = src_dict.copy()
        api_key = d.pop("api_key", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = TeamMember.from_dict(members_item_data)

            members.append(members_item)

        name = d.pop("name", UNSET)

        team_spec = cls(
            api_key=api_key,
            avatar_url=avatar_url,
            email=email,
            id=id,
            members=members,
            name=name,
        )

        team_spec.additional_properties = d
        return team_spec

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
