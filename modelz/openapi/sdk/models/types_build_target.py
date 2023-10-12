from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.types_builder_type import TypesBuilderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesBuildTarget")


@_attrs_define
class TypesBuildTarget:
    """
    Attributes:
        builder (Union[Unset, TypesBuilderType]):
        digest (Union[Unset, str]):
        directory (Union[Unset, str]): directory is the target directory name.
            Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the
            git repository.  Otherwise, if specified, the volume will contain the git repository in
            the subdirectory with the given name.
            +optional
        duration (Union[Unset, str]):
        image (Union[Unset, str]):
        image_tag (Union[Unset, str]):
        registry (Union[Unset, str]):
        registry_token (Union[Unset, str]):
    """

    builder: Union[Unset, TypesBuilderType] = UNSET
    digest: Union[Unset, str] = UNSET
    directory: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    image_tag: Union[Unset, str] = UNSET
    registry: Union[Unset, str] = UNSET
    registry_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        builder: Union[Unset, str] = UNSET
        if not isinstance(self.builder, Unset):
            builder = self.builder.value

        digest = self.digest
        directory = self.directory
        duration = self.duration
        image = self.image
        image_tag = self.image_tag
        registry = self.registry
        registry_token = self.registry_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if builder is not UNSET:
            field_dict["builder"] = builder
        if digest is not UNSET:
            field_dict["digest"] = digest
        if directory is not UNSET:
            field_dict["directory"] = directory
        if duration is not UNSET:
            field_dict["duration"] = duration
        if image is not UNSET:
            field_dict["image"] = image
        if image_tag is not UNSET:
            field_dict["image_tag"] = image_tag
        if registry is not UNSET:
            field_dict["registry"] = registry
        if registry_token is not UNSET:
            field_dict["registry_token"] = registry_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _builder = d.pop("builder", UNSET)
        builder: Union[Unset, TypesBuilderType]
        if isinstance(_builder, Unset):
            builder = UNSET
        else:
            builder = TypesBuilderType(_builder)

        digest = d.pop("digest", UNSET)

        directory = d.pop("directory", UNSET)

        duration = d.pop("duration", UNSET)

        image = d.pop("image", UNSET)

        image_tag = d.pop("image_tag", UNSET)

        registry = d.pop("registry", UNSET)

        registry_token = d.pop("registry_token", UNSET)

        types_build_target = cls(
            builder=builder,
            digest=digest,
            directory=directory,
            duration=duration,
            image=image,
            image_tag=image_tag,
            registry=registry,
            registry_token=registry_token,
        )

        types_build_target.additional_properties = d
        return types_build_target

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
