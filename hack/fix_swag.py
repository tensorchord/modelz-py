"""
Fix swagger document of wrong types
"""
import json
from os.path import dirname, join
from typing import Any, Dict, List, TypedDict

from jsonpath_ng import parse

docPath = join(dirname(dirname(__file__)), "openapi", "swagger_v3.json")
outPath = join(dirname(dirname(__file__)), "openapi", "swagger_fix.json")


RefDict = TypedDict("AllOfDict", {"$ref": str})

BeforeFixNode = TypedDict(
    "BeforeFixNode", {"type": str, "description": str, "allOf": List[RefDict]}
)

AfterFixNode = TypedDict(
    "BeforeFixNode", {"type": str, "description": str, "$ref": str}
)


jsonpath_expr_allof_nodes = parse("$..allOf.`parent`")
jsonpath_expr_ref = parse('$.."$ref"')
jsonpath_expr_components = parse("$.components.schemas")

with open(docPath, "r") as f:
    data = json.load(f)

# Before example:
# 'allOf': [{'$ref': '#/definitions/github_com_tensorchord_modelz_apiserver_api_types.DeploymentSource'} # noqa
# After fix example:
# '$ref': '#/components/schemas/github_com_tensorchord_modelz_apiserver_api_types.DeploymentSource' # noqa
for parent in jsonpath_expr_allof_nodes.find(data):
    node: BeforeFixNode = parent.value

    ref: List[RefDict] = node.pop("allOf")

    fixednode: AfterFixNode = node.copy()
    fixednode["$ref"] = ref[0]["$ref"].replace("definitions", "components/schemas")

    data = parent.full_path.update(data, fixednode)

# Before example:
# '$ref': '#/components/schemas/github_com_tensorchord_modelz_apiserver_api_types.DeploymentSource' # noqa
# After fix example:
# '$ref': '#/components/schemas/api_types.DeploymentSource'

# At node reference
for parent in jsonpath_expr_ref.find(data):
    node: str = parent.value
    fixednode = node.replace("github_com_tensorchord_modelz_apiserver_api_types.", "")
    data = parent.full_path.update(data, fixednode)

# At schema definition
for parent in jsonpath_expr_components.find(data):
    node: Dict[str, Any] = parent.value
    fixednode = {
        k.replace("github_com_tensorchord_modelz_apiserver_api_types.", ""): v
        for k, v in node.items()
    }
    data = parent.full_path.update(data, fixednode)

with open(outPath, "w") as f:
    json.dump(data, f, indent=2)
