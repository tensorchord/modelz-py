from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_docker_source import DeploymentDockerSource
    from ..models.deployment_git_source import DeploymentGitSource
    from ..models.deployment_huggingface_space_source import (
        DeploymentHuggingfaceSpaceSource,
    )


T = TypeVar("T", bound="DeploymentSource")


@_attrs_define
class DeploymentSource:
    """
    Attributes:
        docker (Union[Unset, DeploymentDockerSource]):
        git (Union[Unset, DeploymentGitSource]):
        huggingface (Union[Unset, DeploymentHuggingfaceSpaceSource]):
    """

    docker: Union[Unset, "DeploymentDockerSource"] = UNSET
    git: Union[Unset, "DeploymentGitSource"] = UNSET
    huggingface: Union[Unset, "DeploymentHuggingfaceSpaceSource"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        docker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker, Unset):
            docker = self.docker.to_dict()

        git: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        huggingface: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.huggingface, Unset):
            huggingface = self.huggingface.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docker is not UNSET:
            field_dict["docker"] = docker
        if git is not UNSET:
            field_dict["git"] = git
        if huggingface is not UNSET:
            field_dict["huggingface"] = huggingface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deployment_docker_source import DeploymentDockerSource
        from ..models.deployment_git_source import DeploymentGitSource
        from ..models.deployment_huggingface_space_source import (
            DeploymentHuggingfaceSpaceSource,
        )

        d = src_dict.copy()
        _docker = d.pop("docker", UNSET)
        docker: Union[Unset, DeploymentDockerSource]
        if isinstance(_docker, Unset):
            docker = UNSET
        else:
            docker = DeploymentDockerSource.from_dict(_docker)

        _git = d.pop("git", UNSET)
        git: Union[Unset, DeploymentGitSource]
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = DeploymentGitSource.from_dict(_git)

        _huggingface = d.pop("huggingface", UNSET)
        huggingface: Union[Unset, DeploymentHuggingfaceSpaceSource]
        if isinstance(_huggingface, Unset):
            huggingface = UNSET
        else:
            huggingface = DeploymentHuggingfaceSpaceSource.from_dict(_huggingface)

        deployment_source = cls(
            docker=docker,
            git=git,
            huggingface=huggingface,
        )

        deployment_source.additional_properties = d
        return deployment_source

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
