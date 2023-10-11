from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_update_request_env_vars import (
        DeploymentUpdateRequestEnvVars,
    )


T = TypeVar("T", bound="DeploymentUpdateRequest")


@_attrs_define
class DeploymentUpdateRequest:
    """
    Attributes:
        command (Union[Unset, str]): Command is the command to run.
        env_vars (Union[Unset, DeploymentUpdateRequestEnvVars]): EnvVars is the environment variables of the deployment.
        http_probe_path (Union[Unset, str]): HTTPProbePath is the user defined path of the http probe.
        max_replicas (Union[Unset, int]): MaxReplicas is the maximum number of replicas of the deployment.
        min_replicas (Union[Unset, int]): MinReplicas is the minimum number of replicas of the deployment.
        port (Union[Unset, int]): Port is the port of the deployment.
        secret (Union[Unset, List[str]]): Secret is the secret of the deployment.
        startup_duration (Union[Unset, int]): StartupDuration is the startup timeout.
        target_load (Union[Unset, int]): TargetLoad is the target load of the deployment. (inflight requests per
            replica)
        zero_duration (Union[Unset, int]): ZeroDuration is the idle timeout before scaling to zero.
    """

    command: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "DeploymentUpdateRequestEnvVars"] = UNSET
    http_probe_path: Union[Unset, str] = UNSET
    max_replicas: Union[Unset, int] = UNSET
    min_replicas: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    secret: Union[Unset, List[str]] = UNSET
    startup_duration: Union[Unset, int] = UNSET
    target_load: Union[Unset, int] = UNSET
    zero_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command = self.command
        env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        http_probe_path = self.http_probe_path
        max_replicas = self.max_replicas
        min_replicas = self.min_replicas
        port = self.port
        secret: Union[Unset, List[str]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret

        startup_duration = self.startup_duration
        target_load = self.target_load
        zero_duration = self.zero_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if http_probe_path is not UNSET:
            field_dict["http_probe_path"] = http_probe_path
        if max_replicas is not UNSET:
            field_dict["max_replicas"] = max_replicas
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if port is not UNSET:
            field_dict["port"] = port
        if secret is not UNSET:
            field_dict["secret"] = secret
        if startup_duration is not UNSET:
            field_dict["startup_duration"] = startup_duration
        if target_load is not UNSET:
            field_dict["target_load"] = target_load
        if zero_duration is not UNSET:
            field_dict["zero_duration"] = zero_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_update_request_env_vars import (
            DeploymentUpdateRequestEnvVars,
        )

        d = src_dict.copy()
        command = d.pop("command", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, DeploymentUpdateRequestEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = DeploymentUpdateRequestEnvVars.from_dict(_env_vars)

        http_probe_path = d.pop("http_probe_path", UNSET)

        max_replicas = d.pop("max_replicas", UNSET)

        min_replicas = d.pop("min_replicas", UNSET)

        port = d.pop("port", UNSET)

        secret = cast(List[str], d.pop("secret", UNSET))

        startup_duration = d.pop("startup_duration", UNSET)

        target_load = d.pop("target_load", UNSET)

        zero_duration = d.pop("zero_duration", UNSET)

        deployment_update_request = cls(
            command=command,
            env_vars=env_vars,
            http_probe_path=http_probe_path,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            port=port,
            secret=secret,
            startup_duration=startup_duration,
            target_load=target_load,
            zero_duration=zero_duration,
        )

        deployment_update_request.additional_properties = d
        return deployment_update_request

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
