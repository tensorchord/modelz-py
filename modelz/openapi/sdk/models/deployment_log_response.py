from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_log import DeploymentLog


T = TypeVar("T", bound="DeploymentLogResponse")


@_attrs_define
class DeploymentLogResponse:
    """
    Attributes:
        logs (Union[Unset, List['DeploymentLog']]):
    """

    logs: Union[Unset, List["DeploymentLog"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()

                logs.append(logs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_log import DeploymentLog

        d = src_dict.copy()
        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = DeploymentLog.from_dict(logs_item_data)

            logs.append(logs_item)

        deployment_log_response = cls(
            logs=logs,
        )

        deployment_log_response.additional_properties = d
        return deployment_log_response

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
