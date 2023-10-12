import json
import sys
from typing import List, Literal, Optional

import click

from modelz.client import ModelzClient
from modelz.console import console, jsonFormattedPrint
from modelz.openapi.sdk.models import (
    DeploymentCreateRequest,
    DeploymentDockerSource,
    DeploymentSource,
    DeploymentSpec,
    DeploymentSpecEnvVars,
    DeploymentUpdateRequest,
    FrameworkType,
    ServerResource,
)
from modelz.openapi.sdk.types import UNSET
from modelz.openapi_client import DeploymentClient

click_option_host = click.option(
    "--host",
    type=str,
    default="https://cloud.modelz.ai/api/v1",
    envvar="MODELZ_CTRL_HOST",
    help="Control Apiserver host for Modelz, "
    + "will read from env $MODELZ_CTRL_HOST if not provided",
)
click_option_user_id = click.option(
    "--user-id",
    "-u",
    type=click.UUID,
    required=True,
    envvar="MODELZ_USER",
    help="login name for Modelz, will read from env $MODELZ_USER if not provided",
)
click_option_key = click.option(
    "--key",
    "-k",
    type=str,
    required=True,
    envvar="MODELZ_API_KEY",
    help="API key for Modelz, will read from env $MODELZ_API_KEY if not provided",
)
click_option_deployment = click.option(
    "--deployment",
    "-d",
    type=str,
    required=True,
    help="Deployment id",
)


def parse_unknown_args(args: List[str]):
    """Parse unknown args to key-value pairs or strings."""
    if not args:
        return None
    if "=" in args[0]:
        return dict(pair.split("=", maxsplit=1) for pair in args)
    if len(args) == 1:
        return args[0]
    raise RuntimeError("failed to parse unknown args", args)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """modelZ CLI

    you could pass unknown options to comamnd by key1=value1 key2=value2..."""
    pass


@cli.command(
    context_settings=dict(
        help_option_names=["-h", "--help"], ignore_unknown_options=True
    ),
)
@click_option_key
@click.option(
    "--endpoint",
    "-e",
    type=str,
    required=True,
    help="Inference endpoint for Modelz deployment",
)
@click.option(
    "--serde",
    type=click.Choice(["json", "msgpack", "raw"], case_sensitive=False),
    default="json",
    help="Serialization/deserialization method",
)
@click.option(
    "--read-stdin",
    is_flag=True,
    help="Read bytes from stdin",
)
@click.option(
    "--write-file",
    default=None,
    type=click.Path(writable=True),
    help="Write received data to file",
)
@click.argument("unknown", nargs=-1, type=click.UNPROCESSED)
def inference(
    key: str,
    endpoint: str,
    serde: Literal["json", "msgpack", "raw"],
    read_stdin: bool,
    write_file: str,
    unknown: str,
):
    """
    Make an inference to ModelZ deployment
    """
    data = parse_unknown_args(unknown)
    if read_stdin:
        # override req data
        data = sys.stdin.buffer.read()

    client = ModelzClient(key=key, endpoint=endpoint)
    resp = client.inference(params=data, serde=serde)
    if not write_file:
        console.print(resp.data)
    else:
        resp.save_to_file(write_file)
        console.print(f"result has been written in [bold cyan]{write_file}[/bold cyan]")


@cli.command(context_settings={"help_option_names": ["-h", "--help"]})
@click_option_key
@click_option_deployment
def metrics(
    key: str,
    deployment: str,
):
    """
    Get metric from ModelZ deployment
    """
    client = ModelzClient(deployment=deployment, key=key)
    client.metrics().show()


@cli.command(context_settings={"help_option_names": ["-h", "--help"]})
def build():
    """
    Build image by ModelZ builder
    """
    raise NotImplementedError


@cli.group(context_settings={"help_option_names": ["-h", "--help"]})
def deployment():
    """
    Operate to ModelZ deployments
    """
    pass


@deployment.command(
    name="create", context_settings={"help_option_names": ["-h", "--help"]}
)
@click_option_host
@click_option_user_id
@click_option_key
@click.option(
    "--image-source",
    type=click.Choice(["docker", "huggingface"], case_sensitive=False),
    default="docker",
    help="Image pull source",
)
@click.option(
    "--image",
    type=str,
    help="URL of Docker image path or HuggingFace project Path",
    required=True,
)
@click.option(
    "--server-resource",
    type=click.Choice([r.value for r in ServerResource], case_sensitive=False),
    required=True,
    help="Server Resource used for deployment",
)
@click.option(
    "--framework",
    type=click.Choice([f.value for f in FrameworkType], case_sensitive=False),
    required=True,
    help="Framework of deployment",
)
@click.option("--name", type=str, help="Name of deployment", required=True)
@click.option(
    "--min-replicas",
    type=click.IntRange(min=0, max=5),
    default=0,
    help="MinReplicas is the minimum number of replicas of the deployment",
)
@click.option(
    "--max-replicas",
    type=click.IntRange(min=0, max=5),
    default=1,
    help="MaxReplicas is the maximum number of replicas of the deployment",
)
@click.option(
    "--target-load",
    type=click.IntRange(min=0),
    default=10,
    help="TargetLoad is the target load of the deployment. "
    + "(inflight requests per replica)",
)
@click.option(
    "--startup-duration",
    type=click.IntRange(min=0),
    default=300,
    help="StartupDuration is the startup timeout",
)
@click.option(
    "--zero-duration",
    type=click.IntRange(min=0),
    default=300,
    help="ZeroDuration is the idle timeout before scaling to zero",
)
@click.option(
    "--http-probe-path",
    type=str,
    help="HTTPProbePath is the user defined path of the http probe",
)
@click.option(
    "--port",
    type=click.IntRange(min=0, max=65535),
    help="Port is the port of the deployment",
)
@click.option(
    "--command",
    type=str,
    help="Command is the command to run",
)
@click.option(
    "--env-vars",
    type=str,
    default="{}",
    help="EnvVars is the environment variables of the deployment, "
    + "input it by minified json",
)
def deployment_create(  # noqa PLR0913
    host: str,
    user_id: str,
    key: str,
    image_source: Literal["docker"],
    image: str,
    server_resource: str,
    framework: str,
    name: str,
    min_replicas: int,
    max_replicas: int,
    target_load: int,
    startup_duration: int,
    zero_duration: int,
    http_probe_path: Optional[str],
    port: Optional[int],
    command: Optional[str],
    env_vars: str,
):
    envs = json.loads(env_vars)
    if image_source == "docker":
        deployment_source = DeploymentSource(docker=DeploymentDockerSource(image=image))
    else:
        raise NotImplementedError
    spec = DeploymentSpec(
        deployment_source=deployment_source,
        server_resource=ServerResource(server_resource),
        framework=FrameworkType(framework),
        name=name,
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        startup_duration=startup_duration,
        zero_duration=zero_duration,
        target_load=target_load,
        http_probe_path=http_probe_path if http_probe_path else UNSET,
        port=port if port else UNSET,
        command=command if command else UNSET,
        env_vars=DeploymentSpecEnvVars.from_dict(envs),
    )
    client = DeploymentClient(login_name=user_id, key=key, host=host)
    resp = client.create(req=DeploymentCreateRequest(spec))
    jsonFormattedPrint(resp)


@deployment.command(
    name="list", context_settings={"help_option_names": ["-h", "--help"]}
)
@click_option_host
@click_option_user_id
@click_option_key
def deployment_list(host: str, user_id: str, key: str):
    client = DeploymentClient(login_name=user_id, key=key, host=host)
    resp = client.list()
    jsonFormattedPrint(resp)


@deployment.command(
    name="get", context_settings={"help_option_names": ["-h", "--help"]}
)
@click_option_host
@click_option_user_id
@click_option_key
@click_option_deployment
def deployment_get(host: str, user_id: str, key: str, deployment: str):
    client = DeploymentClient(login_name=user_id, key=key, host=host)
    resp = client.get(deployment)
    jsonFormattedPrint(resp)


@deployment.command(
    name="update", context_settings={"help_option_names": ["-h", "--help"]}
)
@click_option_host
@click_option_user_id
@click_option_key
@click_option_deployment
@click.option(
    "--min-replicas",
    type=click.IntRange(min=0, max=5),
    help="MinReplicas is the minimum number of replicas of the deployment",
)
@click.option(
    "--max-replicas",
    type=click.IntRange(min=0, max=5),
    help="MaxReplicas is the maximum number of replicas of the deployment",
)
@click.option(
    "--target-load",
    type=click.IntRange(min=0),
    help="TargetLoad is the target load of the deployment. "
    + "(inflight requests per replica)",
)
@click.option(
    "--startup-duration",
    type=click.IntRange(min=0),
    help="StartupDuration is the startup timeout",
)
@click.option(
    "--zero-duration",
    type=click.IntRange(min=0),
    help="ZeroDuration is the idle timeout before scaling to zero",
)
@click.option(
    "--env-vars",
    type=str,
    default="{}",
    help="EnvVars is the environment variables of the deployment, "
    + "input it by minified json",
)
def deployment_update(  # noqa: PLR0913
    host: str,
    user_id: str,
    key: str,
    deployment: str,
    min_replicas: Optional[int],
    max_replicas: Optional[int],
    target_load: Optional[int],
    startup_duration: Optional[int],
    zero_duration: Optional[int],
    env_vars: Optional[str],
):
    envs = (
        UNSET
        if env_vars is None
        else DeploymentSpecEnvVars.from_dict(json.loads(env_vars))
    )
    param = DeploymentUpdateRequest(
        min_replicas=min_replicas if min_replicas else UNSET,
        max_replicas=max_replicas if max_replicas else UNSET,
        target_load=target_load if target_load else UNSET,
        startup_duration=startup_duration if startup_duration else UNSET,
        zero_duration=zero_duration if zero_duration else UNSET,
        http_probe_path=UNSET,
        port=UNSET,
        command=UNSET,
        env_vars=envs,
    )
    client = DeploymentClient(login_name=user_id, key=key, host=host)
    resp = client.update(name=deployment, req=param)
    jsonFormattedPrint(resp)


@deployment.command(
    name="delete", context_settings={"help_option_names": ["-h", "--help"]}
)
@click_option_host
@click_option_user_id
@click_option_key
@click_option_deployment
def deployment_delete(host: str, user_id: str, key: str, deployment: str):
    client = DeploymentClient(login_name=user_id, key=key, host=host)
    resp = client.delete(deployment)
    if resp.parsed is not None:
        jsonFormattedPrint(resp)


def main():
    """CLI entrypoint."""
    cli()
