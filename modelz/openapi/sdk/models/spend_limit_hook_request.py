from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpendLimitHookRequest")


@_attrs_define
class SpendLimitHookRequest:
    """
    Attributes:
        current_value (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        customer_name (Union[Unset, str]):
        meter_id (Union[Unset, str]):
        meter_name (Union[Unset, str]):
        notification_id (Union[Unset, str]):
        notification_name (Union[Unset, str]):
        threshold_condition (Union[Unset, str]):
        threshold_value (Union[Unset, str]):
    """

    current_value: Union[Unset, str] = UNSET
    customer_id: Union[Unset, str] = UNSET
    customer_name: Union[Unset, str] = UNSET
    meter_id: Union[Unset, str] = UNSET
    meter_name: Union[Unset, str] = UNSET
    notification_id: Union[Unset, str] = UNSET
    notification_name: Union[Unset, str] = UNSET
    threshold_condition: Union[Unset, str] = UNSET
    threshold_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_value = self.current_value
        customer_id = self.customer_id
        customer_name = self.customer_name
        meter_id = self.meter_id
        meter_name = self.meter_name
        notification_id = self.notification_id
        notification_name = self.notification_name
        threshold_condition = self.threshold_condition
        threshold_value = self.threshold_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name
        if meter_id is not UNSET:
            field_dict["meter_id"] = meter_id
        if meter_name is not UNSET:
            field_dict["meter_name"] = meter_name
        if notification_id is not UNSET:
            field_dict["notification_id"] = notification_id
        if notification_name is not UNSET:
            field_dict["notification_name"] = notification_name
        if threshold_condition is not UNSET:
            field_dict["threshold_condition"] = threshold_condition
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_value = d.pop("current_value", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        customer_name = d.pop("customer_name", UNSET)

        meter_id = d.pop("meter_id", UNSET)

        meter_name = d.pop("meter_name", UNSET)

        notification_id = d.pop("notification_id", UNSET)

        notification_name = d.pop("notification_name", UNSET)

        threshold_condition = d.pop("threshold_condition", UNSET)

        threshold_value = d.pop("threshold_value", UNSET)

        spend_limit_hook_request = cls(
            current_value=current_value,
            customer_id=customer_id,
            customer_name=customer_name,
            meter_id=meter_id,
            meter_name=meter_name,
            notification_id=notification_id,
            notification_name=notification_name,
            threshold_condition=threshold_condition,
            threshold_value=threshold_value,
        )

        spend_limit_hook_request.additional_properties = d
        return spend_limit_hook_request

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
