from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedCluster")


@_attrs_define
class ManagedCluster:
    """
    Attributes:
        created_at (Union[Unset, str]):
        id (Union[Unset, str]):
        kubernetes_version (Union[Unset, str]):
        name (Union[Unset, str]): For show name
        platform (Union[Unset, str]):
        prometheus_url (Union[Unset, str]):
        region (Union[Unset, str]):
        server_resources (Union[Unset, str]):
        status (Union[Unset, str]):
        token_id (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    kubernetes_version: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    prometheus_url: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    server_resources: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    token_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        id = self.id
        kubernetes_version = self.kubernetes_version
        name = self.name
        platform = self.platform
        prometheus_url = self.prometheus_url
        region = self.region
        server_resources = self.server_resources
        status = self.status
        token_id = self.token_id
        updated_at = self.updated_at
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if kubernetes_version is not UNSET:
            field_dict["kubernetes_version"] = kubernetes_version
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if prometheus_url is not UNSET:
            field_dict["prometheus_url"] = prometheus_url
        if region is not UNSET:
            field_dict["region"] = region
        if server_resources is not UNSET:
            field_dict["server_resources"] = server_resources
        if status is not UNSET:
            field_dict["status"] = status
        if token_id is not UNSET:
            field_dict["token_id"] = token_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        id = d.pop("id", UNSET)

        kubernetes_version = d.pop("kubernetes_version", UNSET)

        name = d.pop("name", UNSET)

        platform = d.pop("platform", UNSET)

        prometheus_url = d.pop("prometheus_url", UNSET)

        region = d.pop("region", UNSET)

        server_resources = d.pop("server_resources", UNSET)

        status = d.pop("status", UNSET)

        token_id = d.pop("token_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        version = d.pop("version", UNSET)

        managed_cluster = cls(
            created_at=created_at,
            id=id,
            kubernetes_version=kubernetes_version,
            name=name,
            platform=platform,
            prometheus_url=prometheus_url,
            region=region,
            server_resources=server_resources,
            status=status,
            token_id=token_id,
            updated_at=updated_at,
            version=version,
        )

        managed_cluster.additional_properties = d
        return managed_cluster

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
