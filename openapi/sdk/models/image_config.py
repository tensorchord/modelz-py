from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageConfig")


@_attrs_define
class ImageConfig:
    """
    Attributes:
        enable_cache_optimize (Union[Unset, bool]): EnableCacheOptimize is the flag to enable image cache optimization.
        secret_id (Union[Unset, str]): Secret for private registry
    """

    enable_cache_optimize: Union[Unset, bool] = UNSET
    secret_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_cache_optimize = self.enable_cache_optimize
        secret_id = self.secret_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_cache_optimize is not UNSET:
            field_dict["enable_cache_optimize"] = enable_cache_optimize
        if secret_id is not UNSET:
            field_dict["secret_id"] = secret_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_cache_optimize = d.pop("enable_cache_optimize", UNSET)

        secret_id = d.pop("secret_id", UNSET)

        image_config = cls(
            enable_cache_optimize=enable_cache_optimize,
            secret_id=secret_id,
        )

        image_config.additional_properties = d
        return image_config

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
