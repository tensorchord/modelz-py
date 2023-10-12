from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.framework_type import FrameworkType
from ..models.server_resource import ServerResource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_source import DeploymentSource
    from ..models.template_env_vars import TemplateEnvVars


T = TypeVar("T", bound="Template")


@_attrs_define
class Template:
    """
    Attributes:
        command (Union[Unset, str]):
        deployment_source (Union[Unset, DeploymentSource]):
        description (Union[Unset, str]):
        env_vars (Union[Unset, TemplateEnvVars]):
        framework (Union[Unset, FrameworkType]):
        http_probe_path (Union[Unset, str]):
        id (Union[Unset, str]):
        is_public (Union[Unset, bool]):
        name (Union[Unset, str]):
        port (Union[Unset, int]):
        readme (Union[Unset, str]):
        repo (Union[Unset, str]):
        server_source (Union[Unset, ServerResource]):
        suggest_name (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
    """

    command: Union[Unset, str] = UNSET
    deployment_source: Union[Unset, "DeploymentSource"] = UNSET
    description: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "TemplateEnvVars"] = UNSET
    framework: Union[Unset, FrameworkType] = UNSET
    http_probe_path: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    readme: Union[Unset, str] = UNSET
    repo: Union[Unset, str] = UNSET
    server_source: Union[Unset, ServerResource] = UNSET
    suggest_name: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command = self.command
        deployment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_source, Unset):
            deployment_source = self.deployment_source.to_dict()

        description = self.description
        env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        framework: Union[Unset, str] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.value

        http_probe_path = self.http_probe_path
        id = self.id
        is_public = self.is_public
        name = self.name
        port = self.port
        readme = self.readme
        repo = self.repo
        server_source: Union[Unset, str] = UNSET
        if not isinstance(self.server_source, Unset):
            server_source = self.server_source.value

        suggest_name = self.suggest_name
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if deployment_source is not UNSET:
            field_dict["deployment_source"] = deployment_source
        if description is not UNSET:
            field_dict["description"] = description
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if framework is not UNSET:
            field_dict["framework"] = framework
        if http_probe_path is not UNSET:
            field_dict["http_probe_path"] = http_probe_path
        if id is not UNSET:
            field_dict["id"] = id
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if readme is not UNSET:
            field_dict["readme"] = readme
        if repo is not UNSET:
            field_dict["repo"] = repo
        if server_source is not UNSET:
            field_dict["server_source"] = server_source
        if suggest_name is not UNSET:
            field_dict["suggest_name"] = suggest_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_source import DeploymentSource
        from ..models.template_env_vars import TemplateEnvVars

        d = src_dict.copy()
        command = d.pop("command", UNSET)

        _deployment_source = d.pop("deployment_source", UNSET)
        deployment_source: Union[Unset, DeploymentSource]
        if isinstance(_deployment_source, Unset):
            deployment_source = UNSET
        else:
            deployment_source = DeploymentSource.from_dict(_deployment_source)

        description = d.pop("description", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, TemplateEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = TemplateEnvVars.from_dict(_env_vars)

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, FrameworkType]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = FrameworkType(_framework)

        http_probe_path = d.pop("http_probe_path", UNSET)

        id = d.pop("id", UNSET)

        is_public = d.pop("is_public", UNSET)

        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        readme = d.pop("readme", UNSET)

        repo = d.pop("repo", UNSET)

        _server_source = d.pop("server_source", UNSET)
        server_source: Union[Unset, ServerResource]
        if isinstance(_server_source, Unset):
            server_source = UNSET
        else:
            server_source = ServerResource(_server_source)

        suggest_name = d.pop("suggest_name", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        template = cls(
            command=command,
            deployment_source=deployment_source,
            description=description,
            env_vars=env_vars,
            framework=framework,
            http_probe_path=http_probe_path,
            id=id,
            is_public=is_public,
            name=name,
            port=port,
            readme=readme,
            repo=repo,
            server_source=server_source,
            suggest_name=suggest_name,
            tags=tags,
        )

        template.additional_properties = d
        return template

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
