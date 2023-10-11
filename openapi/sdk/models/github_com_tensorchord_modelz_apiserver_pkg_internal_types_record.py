from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverPkgInternalTypesRecord")


@_attrs_define
class GithubComTensorchordModelzApiserverPkgInternalTypesRecord:
    """
    Attributes:
        avatar_url (Union[Unset, str]):
        email (Union[Unset, str]):
        full_name (Union[Unset, str]):
        id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        username (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    avatar_url: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar_url = self.avatar_url
        email = self.email
        full_name = self.full_name
        id = self.id
        updated_at = self.updated_at
        username = self.username
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if email is not UNSET:
            field_dict["email"] = email
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if username is not UNSET:
            field_dict["username"] = username
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar_url = d.pop("avatar_url", UNSET)

        email = d.pop("email", UNSET)

        full_name = d.pop("full_name", UNSET)

        id = d.pop("id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        username = d.pop("username", UNSET)

        website = d.pop("website", UNSET)

        github_com_tensorchord_modelz_apiserver_pkg_internal_types_record = cls(
            avatar_url=avatar_url,
            email=email,
            full_name=full_name,
            id=id,
            updated_at=updated_at,
            username=username,
            website=website,
        )

        github_com_tensorchord_modelz_apiserver_pkg_internal_types_record.additional_properties = (
            d
        )
        return github_com_tensorchord_modelz_apiserver_pkg_internal_types_record

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
