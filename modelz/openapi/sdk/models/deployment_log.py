from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentLog")


@_attrs_define
class DeploymentLog:
    """
    Attributes:
        deployment_id (Union[Unset, str]):
        instance (Union[Unset, str]):
        text (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        user (Union[Unset, str]):
    """

    deployment_id: Union[Unset, str] = UNSET
    instance: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployment_id = self.deployment_id
        instance = self.instance
        text = self.text
        timestamp = self.timestamp
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment_id is not UNSET:
            field_dict["deployment_id"] = deployment_id
        if instance is not UNSET:
            field_dict["instance"] = instance
        if text is not UNSET:
            field_dict["text"] = text
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        deployment_id = d.pop("deployment_id", UNSET)

        instance = d.pop("instance", UNSET)

        text = d.pop("text", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        user = d.pop("user", UNSET)

        deployment_log = cls(
            deployment_id=deployment_id,
            instance=instance,
            text=text,
            timestamp=timestamp,
            user=user,
        )

        deployment_log.additional_properties = d
        return deployment_log

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
