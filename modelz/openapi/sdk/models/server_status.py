from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_system_info import NodeSystemInfo
    from ..models.resource_list import ResourceList


T = TypeVar("T", bound="ServerStatus")


@_attrs_define
class ServerStatus:
    """
    Attributes:
        allocatable (Union[Unset, ResourceList]):
        capacity (Union[Unset, ResourceList]):
        phase (Union[Unset, str]):
        system (Union[Unset, NodeSystemInfo]):
    """

    allocatable: Union[Unset, "ResourceList"] = UNSET
    capacity: Union[Unset, "ResourceList"] = UNSET
    phase: Union[Unset, str] = UNSET
    system: Union[Unset, "NodeSystemInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocatable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allocatable, Unset):
            allocatable = self.allocatable.to_dict()

        capacity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()

        phase = self.phase
        system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocatable is not UNSET:
            field_dict["allocatable"] = allocatable
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if phase is not UNSET:
            field_dict["phase"] = phase
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.node_system_info import NodeSystemInfo
        from ..models.resource_list import ResourceList

        d = src_dict.copy()
        _allocatable = d.pop("allocatable", UNSET)
        allocatable: Union[Unset, ResourceList]
        if isinstance(_allocatable, Unset):
            allocatable = UNSET
        else:
            allocatable = ResourceList.from_dict(_allocatable)

        _capacity = d.pop("capacity", UNSET)
        capacity: Union[Unset, ResourceList]
        if isinstance(_capacity, Unset):
            capacity = UNSET
        else:
            capacity = ResourceList.from_dict(_capacity)

        phase = d.pop("phase", UNSET)

        _system = d.pop("system", UNSET)
        system: Union[Unset, NodeSystemInfo]
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = NodeSystemInfo.from_dict(_system)

        server_status = cls(
            allocatable=allocatable,
            capacity=capacity,
            phase=phase,
            system=system,
        )

        server_status.additional_properties = d
        return server_status

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
