from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlNullBool")


@_attrs_define
class SqlNullBool:
    """
    Attributes:
        bool_ (Union[Unset, bool]):
        valid (Union[Unset, bool]): Valid is true if Bool is not NULL
    """

    bool_: Union[Unset, bool] = UNSET
    valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bool_ = self.bool_
        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bool_ is not UNSET:
            field_dict["bool"] = bool_
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bool_ = d.pop("bool", UNSET)

        valid = d.pop("valid", UNSET)

        sql_null_bool = cls(
            bool_=bool_,
            valid=valid,
        )

        sql_null_bool.additional_properties = d
        return sql_null_bool

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
