from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment import Deployment


T = TypeVar("T", bound="DeploymentListResponse")


@_attrs_define
class DeploymentListResponse:
    """
    Attributes:
        deployments (Union[Unset, List['Deployment']]):
    """

    deployments: Union[Unset, List["Deployment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = []
            for deployments_item_data in self.deployments:
                deployments_item = deployments_item_data.to_dict()

                deployments.append(deployments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployments is not UNSET:
            field_dict["deployments"] = deployments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment import Deployment

        d = src_dict.copy()
        deployments = []
        _deployments = d.pop("deployments", UNSET)
        for deployments_item_data in _deployments or []:
            deployments_item = Deployment.from_dict(deployments_item_data)

            deployments.append(deployments_item)

        deployment_list_response = cls(
            deployments=deployments,
        )

        deployment_list_response.additional_properties = d
        return deployment_list_response

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
