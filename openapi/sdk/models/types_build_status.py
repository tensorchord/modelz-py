from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.types_build_phase import TypesBuildPhase
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesBuildStatus")


@_attrs_define
class TypesBuildStatus:
    """
    Attributes:
        phase (Union[Unset, TypesBuildPhase]):
    """

    phase: Union[Unset, TypesBuildPhase] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, TypesBuildPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = TypesBuildPhase(_phase)

        types_build_status = cls(
            phase=phase,
        )

        types_build_status.additional_properties = d
        return types_build_status

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
