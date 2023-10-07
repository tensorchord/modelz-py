from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentGitSource")


@_attrs_define
class DeploymentGitSource:
    """
    Attributes:
        branch (Union[Unset, str]):
        builder (Union[Unset, str]):
        directory (Union[Unset, str]): directory is the target directory name.
            Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the
            git repository.  Otherwise, if specified, the volume will contain the git repository in
            the subdirectory with the given name.
            +optional
        image (Union[Unset, str]):
        image_tag (Union[Unset, str]):
        repo (Union[Unset, str]):
        revision (Union[Unset, str]):
    """

    branch: Union[Unset, str] = UNSET
    builder: Union[Unset, str] = UNSET
    directory: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    image_tag: Union[Unset, str] = UNSET
    repo: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch = self.branch
        builder = self.builder
        directory = self.directory
        image = self.image
        image_tag = self.image_tag
        repo = self.repo
        revision = self.revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if builder is not UNSET:
            field_dict["builder"] = builder
        if directory is not UNSET:
            field_dict["directory"] = directory
        if image is not UNSET:
            field_dict["image"] = image
        if image_tag is not UNSET:
            field_dict["image_tag"] = image_tag
        if repo is not UNSET:
            field_dict["repo"] = repo
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch = d.pop("branch", UNSET)

        builder = d.pop("builder", UNSET)

        directory = d.pop("directory", UNSET)

        image = d.pop("image", UNSET)

        image_tag = d.pop("image_tag", UNSET)

        repo = d.pop("repo", UNSET)

        revision = d.pop("revision", UNSET)

        deployment_git_source = cls(
            branch=branch,
            builder=builder,
            directory=directory,
            image=image,
            image_tag=image_tag,
            repo=repo,
            revision=revision,
        )

        deployment_git_source.additional_properties = d
        return deployment_git_source

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
