from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentResource")


@_attrs_define
class DeploymentResource:
    """
    Attributes:
        cpu (Union[Unset, str]):
        gpu (Union[Unset, str]):
        memory (Union[Unset, str]):
    """

    cpu: Union[Unset, str] = UNSET
    gpu: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu = self.cpu
        gpu = self.gpu
        memory = self.memory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if gpu is not UNSET:
            field_dict["gpu"] = gpu
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu = d.pop("cpu", UNSET)

        gpu = d.pop("gpu", UNSET)

        memory = d.pop("memory", UNSET)

        deployment_resource = cls(
            cpu=cpu,
            gpu=gpu,
            memory=memory,
        )

        deployment_resource.additional_properties = d
        return deployment_resource

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
