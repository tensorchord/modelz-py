from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_spec import ServerSpec
    from ..models.server_status import ServerStatus


T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """
    Attributes:
        spec (Union[Unset, ServerSpec]):
        status (Union[Unset, ServerStatus]):
    """

    spec: Union[Unset, "ServerSpec"] = UNSET
    status: Union[Unset, "ServerStatus"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.server_spec import ServerSpec
        from ..models.server_status import ServerStatus

        d = src_dict.copy()
        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, ServerSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = ServerSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ServerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ServerStatus.from_dict(_status)

        server = cls(
            spec=spec,
            status=status,
        )

        server.additional_properties = d
        return server

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
