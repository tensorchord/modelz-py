from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentToken")


@_attrs_define
class AgentToken:
    """
    Attributes:
        cluster_id (Union[Unset, str]):
        cluster_name (Union[Unset, str]):
        token (Union[Unset, str]): Token is the token used by agent to register managed cluster
    """

    cluster_id: Union[Unset, str] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        cluster_name = self.cluster_name
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cluster_id = d.pop("cluster_id", UNSET)

        cluster_name = d.pop("cluster_name", UNSET)

        token = d.pop("token", UNSET)

        agent_token = cls(
            cluster_id=cluster_id,
            cluster_name=cluster_name,
            token=token,
        )

        agent_token.additional_properties = d
        return agent_token

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
