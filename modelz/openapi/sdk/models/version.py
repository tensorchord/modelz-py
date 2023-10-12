from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_version_info import AgentVersionInfo
    from ..models.version_info import VersionInfo


T = TypeVar("T", bound="Version")


@_attrs_define
class Version:
    """
    Attributes:
        agents (Union[Unset, List['AgentVersionInfo']]):
        version (Union[Unset, VersionInfo]):
    """

    agents: Union[Unset, List["AgentVersionInfo"]] = UNSET
    version: Union[Unset, "VersionInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()

                agents.append(agents_item)

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agents is not UNSET:
            field_dict["agents"] = agents
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agent_version_info import AgentVersionInfo
        from ..models.version_info import VersionInfo

        d = src_dict.copy()
        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = AgentVersionInfo.from_dict(agents_item_data)

            agents.append(agents_item)

        _version = d.pop("version", UNSET)
        version: Union[Unset, VersionInfo]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = VersionInfo.from_dict(_version)

        version = cls(
            agents=agents,
            version=version,
        )

        version.additional_properties = d
        return version

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
