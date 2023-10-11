from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.framework_type import FrameworkType
from ..models.server_resource import ServerResource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_resource import DeploymentResource
    from ..models.deployment_source import DeploymentSource
    from ..models.deployment_spec_env_vars import DeploymentSpecEnvVars
    from ..models.image_config import ImageConfig


T = TypeVar("T", bound="DeploymentSpec")


@_attrs_define
class DeploymentSpec:
    """
    Attributes:
        cluster (Union[Unset, str]):
        command (Union[Unset, str]): Command is the command to run.
        deployment_resource (Union[Unset, DeploymentResource]):
        deployment_source (Union[Unset, DeploymentSource]):
        env_vars (Union[Unset, DeploymentSpecEnvVars]): EnvVars is the environment variables of the deployment.
        framework (Union[Unset, FrameworkType]):
        http_probe_path (Union[Unset, str]): HTTPProbePath is the user defined path of the http probe.
        id (Union[Unset, str]): ID holds the unique identifier of the deployment.
        image_config (Union[Unset, ImageConfig]):
        max_replicas (Union[Unset, int]): MaxReplicas is the maximum number of replicas of the deployment.
        min_replicas (Union[Unset, int]): MinReplicas is the minimum number of replicas of the deployment.
        name (Union[Unset, str]): Name is the name of the deployment. e.g. demo.
            [a-z0-9]([-a-z0-9]*[a-z0-9])?
        port (Union[Unset, int]): Port is the port of the deployment.
        secret (Union[Unset, List[str]]): Secret is the secret of the deployment.
        server_resource (Union[Unset, ServerResource]):
        spot_instance (Union[Unset, bool]):
        startup_duration (Union[Unset, int]): StartupDuration is the startup timeout.
        target_load (Union[Unset, int]): TargetLoad is the target load of the deployment. (inflight requests per
            replica)
        template_id (Union[Unset, str]): TemplateID is the template ID of the deployment.
        zero_duration (Union[Unset, int]): ZeroDuration is the idle timeout before scaling to zero.
    """

    cluster: Union[Unset, str] = UNSET
    command: Union[Unset, str] = UNSET
    deployment_resource: Union[Unset, "DeploymentResource"] = UNSET
    deployment_source: Union[Unset, "DeploymentSource"] = UNSET
    env_vars: Union[Unset, "DeploymentSpecEnvVars"] = UNSET
    framework: Union[Unset, FrameworkType] = UNSET
    http_probe_path: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image_config: Union[Unset, "ImageConfig"] = UNSET
    max_replicas: Union[Unset, int] = UNSET
    min_replicas: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    secret: Union[Unset, List[str]] = UNSET
    server_resource: Union[Unset, ServerResource] = UNSET
    spot_instance: Union[Unset, bool] = UNSET
    startup_duration: Union[Unset, int] = UNSET
    target_load: Union[Unset, int] = UNSET
    template_id: Union[Unset, str] = UNSET
    zero_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster = self.cluster
        command = self.command
        deployment_resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_resource, Unset):
            deployment_resource = self.deployment_resource.to_dict()

        deployment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_source, Unset):
            deployment_source = self.deployment_source.to_dict()

        env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        framework: Union[Unset, str] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.value

        http_probe_path = self.http_probe_path
        id = self.id
        image_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_config, Unset):
            image_config = self.image_config.to_dict()

        max_replicas = self.max_replicas
        min_replicas = self.min_replicas
        name = self.name
        port = self.port
        secret: Union[Unset, List[str]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret

        server_resource: Union[Unset, str] = UNSET
        if not isinstance(self.server_resource, Unset):
            server_resource = self.server_resource.value

        spot_instance = self.spot_instance
        startup_duration = self.startup_duration
        target_load = self.target_load
        template_id = self.template_id
        zero_duration = self.zero_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if command is not UNSET:
            field_dict["command"] = command
        if deployment_resource is not UNSET:
            field_dict["deployment_resource"] = deployment_resource
        if deployment_source is not UNSET:
            field_dict["deployment_source"] = deployment_source
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if framework is not UNSET:
            field_dict["framework"] = framework
        if http_probe_path is not UNSET:
            field_dict["http_probe_path"] = http_probe_path
        if id is not UNSET:
            field_dict["id"] = id
        if image_config is not UNSET:
            field_dict["image_config"] = image_config
        if max_replicas is not UNSET:
            field_dict["max_replicas"] = max_replicas
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if secret is not UNSET:
            field_dict["secret"] = secret
        if server_resource is not UNSET:
            field_dict["server_resource"] = server_resource
        if spot_instance is not UNSET:
            field_dict["spot_instance"] = spot_instance
        if startup_duration is not UNSET:
            field_dict["startup_duration"] = startup_duration
        if target_load is not UNSET:
            field_dict["target_load"] = target_load
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if zero_duration is not UNSET:
            field_dict["zero_duration"] = zero_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_resource import DeploymentResource
        from ..models.deployment_source import DeploymentSource
        from ..models.deployment_spec_env_vars import DeploymentSpecEnvVars
        from ..models.image_config import ImageConfig

        d = src_dict.copy()
        cluster = d.pop("cluster", UNSET)

        command = d.pop("command", UNSET)

        _deployment_resource = d.pop("deployment_resource", UNSET)
        deployment_resource: Union[Unset, DeploymentResource]
        if isinstance(_deployment_resource, Unset):
            deployment_resource = UNSET
        else:
            deployment_resource = DeploymentResource.from_dict(_deployment_resource)

        _deployment_source = d.pop("deployment_source", UNSET)
        deployment_source: Union[Unset, DeploymentSource]
        if isinstance(_deployment_source, Unset):
            deployment_source = UNSET
        else:
            deployment_source = DeploymentSource.from_dict(_deployment_source)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, DeploymentSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = DeploymentSpecEnvVars.from_dict(_env_vars)

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, FrameworkType]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = FrameworkType(_framework)

        http_probe_path = d.pop("http_probe_path", UNSET)

        id = d.pop("id", UNSET)

        _image_config = d.pop("image_config", UNSET)
        image_config: Union[Unset, ImageConfig]
        if isinstance(_image_config, Unset):
            image_config = UNSET
        else:
            image_config = ImageConfig.from_dict(_image_config)

        max_replicas = d.pop("max_replicas", UNSET)

        min_replicas = d.pop("min_replicas", UNSET)

        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        secret = cast(List[str], d.pop("secret", UNSET))

        _server_resource = d.pop("server_resource", UNSET)
        server_resource: Union[Unset, ServerResource]
        if isinstance(_server_resource, Unset):
            server_resource = UNSET
        else:
            server_resource = ServerResource(_server_resource)

        spot_instance = d.pop("spot_instance", UNSET)

        startup_duration = d.pop("startup_duration", UNSET)

        target_load = d.pop("target_load", UNSET)

        template_id = d.pop("templateId", UNSET)

        zero_duration = d.pop("zero_duration", UNSET)

        deployment_spec = cls(
            cluster=cluster,
            command=command,
            deployment_resource=deployment_resource,
            deployment_source=deployment_source,
            env_vars=env_vars,
            framework=framework,
            http_probe_path=http_probe_path,
            id=id,
            image_config=image_config,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            name=name,
            port=port,
            secret=secret,
            server_resource=server_resource,
            spot_instance=spot_instance,
            startup_duration=startup_duration,
            target_load=target_load,
            template_id=template_id,
            zero_duration=zero_duration,
        )

        deployment_spec.additional_properties = d
        return deployment_spec

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
