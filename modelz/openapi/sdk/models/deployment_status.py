from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentStatus")


@_attrs_define
class DeploymentStatus:
    """
    Attributes:
        available_replicas (Union[Unset, int]): AvailableReplicas is the count of replicas ready to receive
            invocations as reported by the faas-provider
        build_id (Union[Unset, str]):
        created_at (Union[Unset, str]): CreatedAt is the time read back from the faas backend's
            data store for when the function or its container was created.
        endpoint (Union[Unset, str]): Endpoint is the endpoint of the deployment. e.g.
            https://df433125-bdaa-4180-9087-313d5f64a3d5.modelz.ai
        image (Union[Unset, str]): Image is the image name of the deployment.
        innocation_count (Union[Unset, int]): InvocationCount count of invocations
        phase (Union[Unset, str]): Phase is the current phase of the deployment.
        replicas (Union[Unset, int]): Replicas desired within the cluster
    """

    available_replicas: Union[Unset, int] = UNSET
    build_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    innocation_count: Union[Unset, int] = UNSET
    phase: Union[Unset, str] = UNSET
    replicas: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_replicas = self.available_replicas
        build_id = self.build_id
        created_at = self.created_at
        endpoint = self.endpoint
        image = self.image
        innocation_count = self.innocation_count
        phase = self.phase
        replicas = self.replicas

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_replicas is not UNSET:
            field_dict["available_replicas"] = available_replicas
        if build_id is not UNSET:
            field_dict["build_id"] = build_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if image is not UNSET:
            field_dict["image"] = image
        if innocation_count is not UNSET:
            field_dict["innocation_count"] = innocation_count
        if phase is not UNSET:
            field_dict["phase"] = phase
        if replicas is not UNSET:
            field_dict["replicas"] = replicas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available_replicas = d.pop("available_replicas", UNSET)

        build_id = d.pop("build_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        image = d.pop("image", UNSET)

        innocation_count = d.pop("innocation_count", UNSET)

        phase = d.pop("phase", UNSET)

        replicas = d.pop("replicas", UNSET)

        deployment_status = cls(
            available_replicas=available_replicas,
            build_id=build_id,
            created_at=created_at,
            endpoint=endpoint,
            image=image,
            innocation_count=innocation_count,
            phase=phase,
            replicas=replicas,
        )

        deployment_status.additional_properties = d
        return deployment_status

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
