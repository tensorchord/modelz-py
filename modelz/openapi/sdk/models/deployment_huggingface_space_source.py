from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentHuggingfaceSpaceSource")


@_attrs_define
class DeploymentHuggingfaceSpaceSource:
    """
    Attributes:
        space (Union[Unset, str]):
        tag (Union[Unset, str]): tag is the tag of the docker image. (Optional)
            If not set, we will get from the huggingface API.
    """

    space: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        space = self.space
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if space is not UNSET:
            field_dict["space"] = space
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        space = d.pop("space", UNSET)

        tag = d.pop("tag", UNSET)

        deployment_huggingface_space_source = cls(
            space=space,
            tag=tag,
        )

        deployment_huggingface_space_source.additional_properties = d
        return deployment_huggingface_space_source

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
