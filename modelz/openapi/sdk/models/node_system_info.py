from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeSystemInfo")


@_attrs_define
class NodeSystemInfo:
    """
    Attributes:
        architecture (Union[Unset, str]): The Architecture reported by the node
        kernel_version (Union[Unset, str]): Kernel Version reported by the node from 'uname -r' (e.g.
            3.16.0-0.bpo.4-amd64).
        machine_id (Union[Unset, str]): MachineID reported by the node. For unique machine identification
            in the cluster this field is preferred. Learn more from man(5)
            machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html
        operating_system (Union[Unset, str]): The Operating System reported by the node
        os_image (Union[Unset, str]): OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7
            (wheezy)).
    """

    architecture: Union[Unset, str] = UNSET
    kernel_version: Union[Unset, str] = UNSET
    machine_id: Union[Unset, str] = UNSET
    operating_system: Union[Unset, str] = UNSET
    os_image: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        architecture = self.architecture
        kernel_version = self.kernel_version
        machine_id = self.machine_id
        operating_system = self.operating_system
        os_image = self.os_image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if kernel_version is not UNSET:
            field_dict["kernelVersion"] = kernel_version
        if machine_id is not UNSET:
            field_dict["machineID"] = machine_id
        if operating_system is not UNSET:
            field_dict["operatingSystem"] = operating_system
        if os_image is not UNSET:
            field_dict["osImage"] = os_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        architecture = d.pop("architecture", UNSET)

        kernel_version = d.pop("kernelVersion", UNSET)

        machine_id = d.pop("machineID", UNSET)

        operating_system = d.pop("operatingSystem", UNSET)

        os_image = d.pop("osImage", UNSET)

        node_system_info = cls(
            architecture=architecture,
            kernel_version=kernel_version,
            machine_id=machine_id,
            operating_system=operating_system,
            os_image=os_image,
        )

        node_system_info.additional_properties = d
        return node_system_info

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
