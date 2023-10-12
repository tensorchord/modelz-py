from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AWSSecret")


@_attrs_define
class AWSSecret:
    """
    Attributes:
        access_key_id (Union[Unset, str]):
        region (Union[Unset, str]):
        secret_access_key (Union[Unset, str]):
    """

    access_key_id: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    secret_access_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key_id = self.access_key_id
        region = self.region
        secret_access_key = self.secret_access_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["access_key_id"] = access_key_id
        if region is not UNSET:
            field_dict["region"] = region
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key_id = d.pop("access_key_id", UNSET)

        region = d.pop("region", UNSET)

        secret_access_key = d.pop("secret_access_key", UNSET)

        aws_secret = cls(
            access_key_id=access_key_id,
            region=region,
            secret_access_key=secret_access_key,
        )

        aws_secret.additional_properties = d
        return aws_secret

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
