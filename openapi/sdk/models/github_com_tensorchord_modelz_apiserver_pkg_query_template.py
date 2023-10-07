from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pgtype_jsonb import PgtypeJSONB
    from ..models.sql_null_bool import SqlNullBool
    from ..models.sql_null_int_32 import SqlNullInt32
    from ..models.sql_null_string import SqlNullString


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverPkgQueryTemplate")


@_attrs_define
class GithubComTensorchordModelzApiserverPkgQueryTemplate:
    """
    Attributes:
        command (Union[Unset, SqlNullString]):
        created_at (Union[Unset, str]):
        deployment_source (Union[Unset, PgtypeJSONB]):
        description (Union[Unset, SqlNullString]):
        env_vars (Union[Unset, PgtypeJSONB]):
        framework (Union[Unset, SqlNullString]):
        http_probe_path (Union[Unset, SqlNullString]):
        id (Union[Unset, str]):
        image (Union[Unset, SqlNullString]):
        is_public (Union[Unset, SqlNullBool]):
        name (Union[Unset, str]):
        port (Union[Unset, SqlNullInt32]):
        readme (Union[Unset, SqlNullString]):
        repo (Union[Unset, SqlNullString]):
        server_resource (Union[Unset, SqlNullString]):
        suggest_name (Union[Unset, SqlNullString]):
        tags (Union[Unset, PgtypeJSONB]):
        updated_at (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    command: Union[Unset, "SqlNullString"] = UNSET
    created_at: Union[Unset, str] = UNSET
    deployment_source: Union[Unset, "PgtypeJSONB"] = UNSET
    description: Union[Unset, "SqlNullString"] = UNSET
    env_vars: Union[Unset, "PgtypeJSONB"] = UNSET
    framework: Union[Unset, "SqlNullString"] = UNSET
    http_probe_path: Union[Unset, "SqlNullString"] = UNSET
    id: Union[Unset, str] = UNSET
    image: Union[Unset, "SqlNullString"] = UNSET
    is_public: Union[Unset, "SqlNullBool"] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, "SqlNullInt32"] = UNSET
    readme: Union[Unset, "SqlNullString"] = UNSET
    repo: Union[Unset, "SqlNullString"] = UNSET
    server_resource: Union[Unset, "SqlNullString"] = UNSET
    suggest_name: Union[Unset, "SqlNullString"] = UNSET
    tags: Union[Unset, "PgtypeJSONB"] = UNSET
    updated_at: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.to_dict()

        created_at = self.created_at
        deployment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_source, Unset):
            deployment_source = self.deployment_source.to_dict()

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        framework: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.to_dict()

        http_probe_path: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.http_probe_path, Unset):
            http_probe_path = self.http_probe_path.to_dict()

        id = self.id
        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        is_public: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.is_public, Unset):
            is_public = self.is_public.to_dict()

        name = self.name
        port: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        readme: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.readme, Unset):
            readme = self.readme.to_dict()

        repo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repo, Unset):
            repo = self.repo.to_dict()

        server_resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server_resource, Unset):
            server_resource = self.server_resource.to_dict()

        suggest_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suggest_name, Unset):
            suggest_name = self.suggest_name.to_dict()

        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        updated_at = self.updated_at
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
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
        if image is not UNSET:
            field_dict["image"] = image
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
        if server_resource is not UNSET:
            field_dict["server_resource"] = server_resource
        if suggest_name is not UNSET:
            field_dict["suggest_name"] = suggest_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pgtype_jsonb import PgtypeJSONB
        from ..models.sql_null_bool import SqlNullBool
        from ..models.sql_null_int_32 import SqlNullInt32
        from ..models.sql_null_string import SqlNullString

        d = src_dict.copy()
        _command = d.pop("command", UNSET)
        command: Union[Unset, SqlNullString]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = SqlNullString.from_dict(_command)

        created_at = d.pop("created_at", UNSET)

        _deployment_source = d.pop("deployment_source", UNSET)
        deployment_source: Union[Unset, PgtypeJSONB]
        if isinstance(_deployment_source, Unset):
            deployment_source = UNSET
        else:
            deployment_source = PgtypeJSONB.from_dict(_deployment_source)

        _description = d.pop("description", UNSET)
        description: Union[Unset, SqlNullString]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = SqlNullString.from_dict(_description)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, PgtypeJSONB]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = PgtypeJSONB.from_dict(_env_vars)

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, SqlNullString]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = SqlNullString.from_dict(_framework)

        _http_probe_path = d.pop("http_probe_path", UNSET)
        http_probe_path: Union[Unset, SqlNullString]
        if isinstance(_http_probe_path, Unset):
            http_probe_path = UNSET
        else:
            http_probe_path = SqlNullString.from_dict(_http_probe_path)

        id = d.pop("id", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, SqlNullString]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = SqlNullString.from_dict(_image)

        _is_public = d.pop("is_public", UNSET)
        is_public: Union[Unset, SqlNullBool]
        if isinstance(_is_public, Unset):
            is_public = UNSET
        else:
            is_public = SqlNullBool.from_dict(_is_public)

        name = d.pop("name", UNSET)

        _port = d.pop("port", UNSET)
        port: Union[Unset, SqlNullInt32]
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = SqlNullInt32.from_dict(_port)

        _readme = d.pop("readme", UNSET)
        readme: Union[Unset, SqlNullString]
        if isinstance(_readme, Unset):
            readme = UNSET
        else:
            readme = SqlNullString.from_dict(_readme)

        _repo = d.pop("repo", UNSET)
        repo: Union[Unset, SqlNullString]
        if isinstance(_repo, Unset):
            repo = UNSET
        else:
            repo = SqlNullString.from_dict(_repo)

        _server_resource = d.pop("server_resource", UNSET)
        server_resource: Union[Unset, SqlNullString]
        if isinstance(_server_resource, Unset):
            server_resource = UNSET
        else:
            server_resource = SqlNullString.from_dict(_server_resource)

        _suggest_name = d.pop("suggest_name", UNSET)
        suggest_name: Union[Unset, SqlNullString]
        if isinstance(_suggest_name, Unset):
            suggest_name = UNSET
        else:
            suggest_name = SqlNullString.from_dict(_suggest_name)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, PgtypeJSONB]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PgtypeJSONB.from_dict(_tags)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        github_com_tensorchord_modelz_apiserver_pkg_query_template = cls(
            command=command,
            created_at=created_at,
            deployment_source=deployment_source,
            description=description,
            env_vars=env_vars,
            framework=framework,
            http_probe_path=http_probe_path,
            id=id,
            image=image,
            is_public=is_public,
            name=name,
            port=port,
            readme=readme,
            repo=repo,
            server_resource=server_resource,
            suggest_name=suggest_name,
            tags=tags,
            updated_at=updated_at,
            user_id=user_id,
        )

        github_com_tensorchord_modelz_apiserver_pkg_query_template.additional_properties = (
            d
        )
        return github_com_tensorchord_modelz_apiserver_pkg_query_template

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
