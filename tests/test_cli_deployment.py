import logging
from unittest.mock import patch

import pytest
from click.testing import CliRunner, Result

from modelz.args import (
    deployment_create,
    deployment_delete,
    deployment_list,
    deployment_update,
)
from openapi.sdk.models.deployment_create_request import DeploymentCreateRequest
from openapi.sdk.models.deployment_docker_source import DeploymentDockerSource
from openapi.sdk.models.deployment_list_response import DeploymentListResponse
from openapi.sdk.models.deployment_response import DeploymentResponse
from openapi.sdk.models.deployment_source import DeploymentSource
from openapi.sdk.models.deployment_spec import DeploymentSpec
from openapi.sdk.models.deployment_spec_env_vars import DeploymentSpecEnvVars
from openapi.sdk.models.deployment_update_request import DeploymentUpdateRequest
from openapi.sdk.models.framework_type import FrameworkType
from openapi.sdk.models.server_resource import ServerResource
from openapi.sdk.types import UNSET, Response


@pytest.mark.parametrize(
    "name, args, expect_spec",
    [
        (
            "basic",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "--image",
                "modelzai/testimage:latest",
                "--server-resource",
                "cpu-4c-16g",
                "--framework",
                "mosec",
                "--name",
                "instance",
            ],
            DeploymentSpec(
                deployment_source=DeploymentSource(
                    docker=DeploymentDockerSource(image="modelzai/testimage:latest")
                ),
                server_resource=ServerResource.CPU_4C_16G,
                framework=FrameworkType.MOSEC,
                name="instance",
                min_replicas=0,
                max_replicas=1,
                startup_duration=300,
                zero_duration=300,
                target_load=10,
                http_probe_path=UNSET,
                port=UNSET,
                command=UNSET,
                env_vars=DeploymentSpecEnvVars.from_dict({}),
            ),
        ),
        (
            "explicit",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "--image-source",
                "docker",
                "--image",
                "modelzai/testimage:latest",
                "--server-resource",
                "nvidia-ada-l4-2-24c-96g",
                "--framework",
                "gradio",
                "--name",
                "instance",
                "--max-replicas",
                "2",
                "--min-replicas",
                "1",
                "--port",
                "8080",
                "--command",
                "python main.py",
                "--http-probe-path",
                "/",
            ],
            DeploymentSpec(
                deployment_source=DeploymentSource(
                    docker=DeploymentDockerSource(image="modelzai/testimage:latest")
                ),
                server_resource=ServerResource.NVIDIA_ADA_L4_2_24C_96G,
                framework=FrameworkType.GRADIO,
                name="instance",
                min_replicas=1,
                max_replicas=2,
                zero_duration=300,
                startup_duration=300,
                target_load=10,
                http_probe_path="/",
                port=8080,
                command="python main.py",
                env_vars=DeploymentSpecEnvVars.from_dict({}),
            ),
        ),
        (
            "envvars",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "--image",
                "modelzai/testimage:latest",
                "--server-resource",
                "cpu-4c-16g",
                "--framework",
                "mosec",
                "--name",
                "instance",
                "--env-vars",
                '{"HUGGINGFACE_REPO":"www.repo.com","PATH":"/bin"}',
            ],
            DeploymentSpec(
                deployment_source=DeploymentSource(
                    docker=DeploymentDockerSource(image="modelzai/testimage:latest")
                ),
                server_resource=ServerResource.CPU_4C_16G,
                framework=FrameworkType.MOSEC,
                name="instance",
                min_replicas=0,
                max_replicas=1,
                startup_duration=300,
                zero_duration=300,
                target_load=10,
                http_probe_path=UNSET,
                port=UNSET,
                command=UNSET,
                env_vars=DeploymentSpecEnvVars.from_dict(
                    {"HUGGINGFACE_REPO": "www.repo.com", "PATH": "/bin"}
                ),
            ),
        ),
    ],
)
def test_deployment_create(name, args, expect_spec):
    with patch("modelz.openapi_client.DeploymentClient.create") as mock_func:
        mock_func.return_value = Response(
            status_code=200,
            content=b"",
            headers={},
            parsed=DeploymentResponse(spec=expect_spec),
        )
        runner = CliRunner()
        result = runner.invoke(deployment_create, args)
        assertResult(result)
        mock_func.assert_called_with(req=DeploymentCreateRequest(expect_spec))


@pytest.mark.parametrize(
    "name, args",
    [
        ("basic", ["-n", "00000000-1111-1111-1111-000000000000", "-k", "testkey"]),
    ],
)
def test_deployment_list(name, args):
    with patch("modelz.openapi_client.DeploymentClient.list") as mock_func:
        mock_func.return_value = Response(
            status_code=200,
            content=b"",
            headers={},
            parsed=DeploymentListResponse(deployments=UNSET),
        )
        runner = CliRunner()
        result = runner.invoke(deployment_list, args)
        logging.error("Exit code was not null!", exc_info=result.exc_info)
        assertResult(result)
        mock_func.assert_called_once()


@pytest.mark.parametrize(
    "name, args, expect_req",
    [
        (
            "basic",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "-d",
                "modelz-abc",
            ],
            DeploymentUpdateRequest(
                min_replicas=UNSET,
                max_replicas=UNSET,
                zero_duration=UNSET,
                http_probe_path=UNSET,
                port=UNSET,
                command=UNSET,
                env_vars=DeploymentSpecEnvVars.from_dict({}),
            ),
        ),
        (
            "explicit",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "-d",
                "modelz-abc",
                "--max-replicas",
                "2",
                "--min-replicas",
                "1",
                "--zero-duration",
                "600",
            ],
            DeploymentUpdateRequest(
                min_replicas=1,
                max_replicas=2,
                zero_duration=600,
                env_vars=DeploymentSpecEnvVars.from_dict({}),
            ),
        ),
        (
            "envvars",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "-d",
                "modelz-abc",
                "--env-vars",
                '{"HUGGINGFACE_REPO":"www.repo.com","PATH":"/bin"}',
            ],
            DeploymentUpdateRequest(
                min_replicas=UNSET,
                max_replicas=UNSET,
                zero_duration=UNSET,
                http_probe_path=UNSET,
                port=UNSET,
                command=UNSET,
                env_vars=DeploymentSpecEnvVars.from_dict(
                    {"HUGGINGFACE_REPO": "www.repo.com", "PATH": "/bin"}
                ),
            ),
        ),
    ],
)
def test_deployment_update(name, args, expect_req):
    with patch("modelz.openapi_client.DeploymentClient.update") as mock_func:
        mock_func.return_value = Response(
            status_code=200, content=b"", headers={}, parsed=DeploymentResponse()
        )
        runner = CliRunner()
        result = runner.invoke(deployment_update, args)
        assertResult(result)
        mock_func.assert_called_with(name="modelz-abc", req=expect_req)


@pytest.mark.parametrize(
    "name, args",
    [
        (
            "basic",
            [
                "-n",
                "00000000-1111-1111-1111-000000000000",
                "-k",
                "testkey",
                "-d",
                "modelz-abc",
            ],
        ),
    ],
)
def test_deployment_delete(name, args):
    with patch("modelz.openapi_client.DeploymentClient.delete") as mock_func:
        mock_func.return_value = Response(
            status_code=200, content=b"", headers={}, parsed=None
        )
        runner = CliRunner()
        result = runner.invoke(deployment_delete, args)
        assertResult(result)
        mock_func.assert_called_once()


def assertResult(result: Result):
    if result.exit_code != 0:
        logging.error("command run failed", exc_info=result.exc_info)
        raise AssertionError("exit code != 0")
