from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_build import TypesBuild


T = TypeVar("T", bound="BuildListResponse")


@_attrs_define
class BuildListResponse:
    """
    Attributes:
        deployment (Union[Unset, List['TypesBuild']]):
    """

    deployment: Union[Unset, List["TypesBuild"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deployment, Unset):
            deployment = []
            for deployment_item_data in self.deployment:
                deployment_item = deployment_item_data.to_dict()

                deployment.append(deployment_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployment is not UNSET:
            field_dict["deployment"] = deployment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.types_build import TypesBuild

        d = src_dict.copy()
        deployment = []
        _deployment = d.pop("deployment", UNSET)
        for deployment_item_data in _deployment or []:
            deployment_item = TypesBuild.from_dict(deployment_item_data)

            deployment.append(deployment_item)

        build_list_response = cls(
            deployment=deployment,
        )

        build_list_response.additional_properties = d
        return build_list_response

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
