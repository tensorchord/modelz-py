from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_resource import ServerResource
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerResourceInfo")


@_attrs_define
class ServerResourceInfo:
    """
    Attributes:
        cpu (Union[Unset, int]):
        gpu (Union[Unset, int]):
        gpu_memory (Union[Unset, int]):
        memory (Union[Unset, int]):
        name (Union[Unset, str]):
        price (Union[Unset, float]):
        resource (Union[Unset, ServerResource]):
    """

    cpu: Union[Unset, int] = UNSET
    gpu: Union[Unset, int] = UNSET
    gpu_memory: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    resource: Union[Unset, ServerResource] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu = self.cpu
        gpu = self.gpu
        gpu_memory = self.gpu_memory
        memory = self.memory
        name = self.name
        price = self.price
        resource: Union[Unset, str] = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if gpu_memory is not UNSET:
            field_dict["gpu_memory"] = gpu_memory
        if memory is not UNSET:
            field_dict["memory"] = memory
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu = d.pop("cpu", UNSET)

        gpu = d.pop("gpu", UNSET)

        gpu_memory = d.pop("gpu_memory", UNSET)

        memory = d.pop("memory", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: Union[Unset, ServerResource]
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = ServerResource(_resource)

        server_resource_info = cls(
            cpu=cpu,
            gpu=gpu,
            gpu_memory=gpu_memory,
            memory=memory,
            name=name,
            price=price,
            resource=resource,
        )

        server_resource_info.additional_properties = d
        return server_resource_info

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
