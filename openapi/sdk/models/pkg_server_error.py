from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pkg_server_error_error import PkgServerErrorError


T = TypeVar("T", bound="PkgServerError")


@_attrs_define
class PkgServerError:
    """
    Attributes:
        error (Union[Unset, PkgServerErrorError]):
        http_status_code (Union[Unset, int]): Machine-readable error code.
        message (Union[Unset, str]): Human-readable message.
        op (Union[Unset, str]): Logical operation and nested error.
        request (Union[Unset, str]):
    """

    error: Union[Unset, "PkgServerErrorError"] = UNSET
    http_status_code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    op: Union[Unset, str] = UNSET
    request: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        http_status_code = self.http_status_code
        message = self.message
        op = self.op
        request = self.request

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if http_status_code is not UNSET:
            field_dict["http_status_code"] = http_status_code
        if message is not UNSET:
            field_dict["message"] = message
        if op is not UNSET:
            field_dict["op"] = op
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pkg_server_error_error import PkgServerErrorError

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, PkgServerErrorError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PkgServerErrorError.from_dict(_error)

        http_status_code = d.pop("http_status_code", UNSET)

        message = d.pop("message", UNSET)

        op = d.pop("op", UNSET)

        request = d.pop("request", UNSET)

        pkg_server_error = cls(
            error=error,
            http_status_code=http_status_code,
            message=message,
            op=op,
            request=request,
        )

        pkg_server_error.additional_properties = d
        return pkg_server_error

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
