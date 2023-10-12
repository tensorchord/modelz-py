from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """
    Attributes:
        build_date (Union[Unset, str]):
        compiler (Union[Unset, str]):
        git_commit (Union[Unset, str]):
        git_tag (Union[Unset, str]):
        git_tree_state (Union[Unset, str]):
        go_version (Union[Unset, str]):
        platform (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    build_date: Union[Unset, str] = UNSET
    compiler: Union[Unset, str] = UNSET
    git_commit: Union[Unset, str] = UNSET
    git_tag: Union[Unset, str] = UNSET
    git_tree_state: Union[Unset, str] = UNSET
    go_version: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        build_date = self.build_date
        compiler = self.compiler
        git_commit = self.git_commit
        git_tag = self.git_tag
        git_tree_state = self.git_tree_state
        go_version = self.go_version
        platform = self.platform
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_date is not UNSET:
            field_dict["build_date"] = build_date
        if compiler is not UNSET:
            field_dict["compiler"] = compiler
        if git_commit is not UNSET:
            field_dict["git_commit"] = git_commit
        if git_tag is not UNSET:
            field_dict["git_tag"] = git_tag
        if git_tree_state is not UNSET:
            field_dict["git_tree_state"] = git_tree_state
        if go_version is not UNSET:
            field_dict["go_version"] = go_version
        if platform is not UNSET:
            field_dict["platform"] = platform
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        build_date = d.pop("build_date", UNSET)

        compiler = d.pop("compiler", UNSET)

        git_commit = d.pop("git_commit", UNSET)

        git_tag = d.pop("git_tag", UNSET)

        git_tree_state = d.pop("git_tree_state", UNSET)

        go_version = d.pop("go_version", UNSET)

        platform = d.pop("platform", UNSET)

        version = d.pop("version", UNSET)

        version_info = cls(
            build_date=build_date,
            compiler=compiler,
            git_commit=git_commit,
            git_tag=git_tag,
            git_tree_state=git_tree_state,
            go_version=go_version,
            platform=platform,
            version=version,
        )

        version_info.additional_properties = d
        return version_info

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
