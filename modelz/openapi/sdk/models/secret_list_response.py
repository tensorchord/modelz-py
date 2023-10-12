from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="SecretListResponse")


@_attrs_define
class SecretListResponse:
    """
    Attributes:
        secrets (Union[Unset, List['Secret']]):
    """

    secrets: Union[Unset, List["Secret"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secrets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()

                secrets.append(secrets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.secret import Secret

        d = src_dict.copy()
        secrets = []
        _secrets = d.pop("secrets", UNSET)
        for secrets_item_data in _secrets or []:
            secrets_item = Secret.from_dict(secrets_item_data)

            secrets.append(secrets_item)

        secret_list_response = cls(
            secrets=secrets,
        )

        secret_list_response.additional_properties = d
        return secret_list_response

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
