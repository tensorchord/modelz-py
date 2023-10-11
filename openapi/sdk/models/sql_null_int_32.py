from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlNullInt32")


@_attrs_define
class SqlNullInt32:
    """
    Attributes:
        int32 (Union[Unset, int]):
        valid (Union[Unset, bool]): Valid is true if Int32 is not NULL
    """

    int32: Union[Unset, int] = UNSET
    valid: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        int32 = self.int32
        valid = self.valid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if int32 is not UNSET:
            field_dict["int32"] = int32
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        int32 = d.pop("int32", UNSET)

        valid = d.pop("valid", UNSET)

        sql_null_int_32 = cls(
            int32=int32,
            valid=valid,
        )

        sql_null_int_32.additional_properties = d
        return sql_null_int_32

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
