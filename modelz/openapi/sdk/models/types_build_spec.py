from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_auth_n import TypesAuthN
    from ..models.types_build_target import TypesBuildTarget


T = TypeVar("T", bound="TypesBuildSpec")


@_attrs_define
class TypesBuildSpec:
    """
    Attributes:
        authn (Union[Unset, TypesAuthN]):
        branch (Union[Unset, str]):
        build_target (Union[Unset, TypesBuildTarget]):
        image (Union[Unset, str]):
        image_tag (Union[Unset, str]):
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
        repository (Union[Unset, str]): repository is the URL
        revision (Union[Unset, str]): revision is the commit hash for the specified revision.
            +optional
        secret_id (Union[Unset, str]):
    """

    authn: Union[Unset, "TypesAuthN"] = UNSET
    branch: Union[Unset, str] = UNSET
    build_target: Union[Unset, "TypesBuildTarget"] = UNSET
    image: Union[Unset, str] = UNSET
    image_tag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    secret_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authn: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authn, Unset):
            authn = self.authn.to_dict()

        branch = self.branch
        build_target: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.build_target, Unset):
            build_target = self.build_target.to_dict()

        image = self.image
        image_tag = self.image_tag
        name = self.name
        namespace = self.namespace
        repository = self.repository
        revision = self.revision
        secret_id = self.secret_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authn is not UNSET:
            field_dict["authn"] = authn
        if branch is not UNSET:
            field_dict["branch"] = branch
        if build_target is not UNSET:
            field_dict["buildTarget"] = build_target
        if image is not UNSET:
            field_dict["image"] = image
        if image_tag is not UNSET:
            field_dict["image_tag"] = image_tag
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if repository is not UNSET:
            field_dict["repository"] = repository
        if revision is not UNSET:
            field_dict["revision"] = revision
        if secret_id is not UNSET:
            field_dict["secret_id"] = secret_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.types_auth_n import TypesAuthN
        from ..models.types_build_target import TypesBuildTarget

        d = src_dict.copy()
        _authn = d.pop("authn", UNSET)
        authn: Union[Unset, TypesAuthN]
        if isinstance(_authn, Unset):
            authn = UNSET
        else:
            authn = TypesAuthN.from_dict(_authn)

        branch = d.pop("branch", UNSET)

        _build_target = d.pop("buildTarget", UNSET)
        build_target: Union[Unset, TypesBuildTarget]
        if isinstance(_build_target, Unset):
            build_target = UNSET
        else:
            build_target = TypesBuildTarget.from_dict(_build_target)

        image = d.pop("image", UNSET)

        image_tag = d.pop("image_tag", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        repository = d.pop("repository", UNSET)

        revision = d.pop("revision", UNSET)

        secret_id = d.pop("secret_id", UNSET)

        types_build_spec = cls(
            authn=authn,
            branch=branch,
            build_target=build_target,
            image=image,
            image_tag=image_tag,
            name=name,
            namespace=namespace,
            repository=repository,
            revision=revision,
            secret_id=secret_id,
        )

        types_build_spec.additional_properties = d
        return types_build_spec

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
