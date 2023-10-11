from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_type import SecretType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_secret import AWSSecret
    from ..models.docker_secret import DockerSecret
    from ..models.gcp_secret import GCPSecret


T = TypeVar("T", bound="Secret")


@_attrs_define
class Secret:
    """
    Attributes:
        aws (Union[Unset, AWSSecret]):
        docker (Union[Unset, DockerSecret]):
        gcp (Union[Unset, GCPSecret]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, SecretType]):
    """

    aws: Union[Unset, "AWSSecret"] = UNSET
    docker: Union[Unset, "DockerSecret"] = UNSET
    gcp: Union[Unset, "GCPSecret"] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, SecretType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aws: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        docker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker, Unset):
            docker = self.docker.to_dict()

        gcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        id = self.id
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws is not UNSET:
            field_dict["aws"] = aws
        if docker is not UNSET:
            field_dict["docker"] = docker
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aws_secret import AWSSecret
        from ..models.docker_secret import DockerSecret
        from ..models.gcp_secret import GCPSecret

        d = src_dict.copy()
        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, AWSSecret]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = AWSSecret.from_dict(_aws)

        _docker = d.pop("docker", UNSET)
        docker: Union[Unset, DockerSecret]
        if isinstance(_docker, Unset):
            docker = UNSET
        else:
            docker = DockerSecret.from_dict(_docker)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, GCPSecret]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = GCPSecret.from_dict(_gcp)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SecretType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SecretType(_type)

        secret = cls(
            aws=aws,
            docker=docker,
            gcp=gcp,
            id=id,
            name=name,
            type=type,
        )

        secret.additional_properties = d
        return secret

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
