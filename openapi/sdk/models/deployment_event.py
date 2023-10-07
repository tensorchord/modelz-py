from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentEvent")


@_attrs_define
class DeploymentEvent:
    """
    Attributes:
        created_at (Union[Unset, str]):
        deployment_id (Union[Unset, str]):
        event_type (Union[Unset, str]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    deployment_id: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        deployment_id = self.deployment_id
        event_type = self.event_type
        id = self.id
        message = self.message
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deployment_id is not UNSET:
            field_dict["deployment_id"] = deployment_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        deployment_id = d.pop("deployment_id", UNSET)

        event_type = d.pop("event_type", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        user_id = d.pop("user_id", UNSET)

        deployment_event = cls(
            created_at=created_at,
            deployment_id=deployment_id,
            event_type=event_type,
            id=id,
            message=message,
            user_id=user_id,
        )

        deployment_event.additional_properties = d
        return deployment_event

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
