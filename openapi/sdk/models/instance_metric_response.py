from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instance import Instance
    from ..models.metric_response import MetricResponse


T = TypeVar("T", bound="InstanceMetricResponse")


@_attrs_define
class InstanceMetricResponse:
    """
    Attributes:
        instance (Union[Unset, Instance]):
        metrics (Union[Unset, MetricResponse]):
    """

    instance: Union[Unset, "Instance"] = UNSET
    metrics: Union[Unset, "MetricResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        metrics: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance is not UNSET:
            field_dict["instance"] = instance
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instance import Instance
        from ..models.metric_response import MetricResponse

        d = src_dict.copy()
        _instance = d.pop("instance", UNSET)
        instance: Union[Unset, Instance]
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = Instance.from_dict(_instance)

        _metrics = d.pop("metrics", UNSET)
        metrics: Union[Unset, MetricResponse]
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = MetricResponse.from_dict(_metrics)

        instance_metric_response = cls(
            instance=instance,
            metrics=metrics,
        )

        instance_metric_response.additional_properties = d
        return instance_metric_response

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
