from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="SecretCreateResponse")


@_attrs_define
class SecretCreateResponse:
    """
    Attributes:
        secret (Union[Unset, List['Secret']]):
        uid (Union[Unset, str]):
    """

    secret: Union[Unset, List["Secret"]] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = []
            for secret_item_data in self.secret:
                secret_item = secret_item_data.to_dict()

                secret.append(secret_item)

        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret is not UNSET:
            field_dict["secret"] = secret
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.secret import Secret

        d = src_dict.copy()
        secret = []
        _secret = d.pop("secret", UNSET)
        for secret_item_data in _secret or []:
            secret_item = Secret.from_dict(secret_item_data)

            secret.append(secret_item)

        uid = d.pop("uid", UNSET)

        secret_create_response = cls(
            secret=secret,
            uid=uid,
        )

        secret_create_response.additional_properties = d
        return secret_create_response

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
