import sys
from typing import Dict, Optional

from rich.console import Console

from modelz.args import build_argument_parser, parse_arguments
from modelz.client import ModelzClient

console = Console()


def inference(
    deployment: str,
    params: Optional[Dict[str, str]] = None,
    read_stdin: bool = False,
    write_file: Optional[str] = None,
    key: Optional[str] = None,
    serde: str = "json",
):
    """Model inference.

    Example:
        ``modelz inference -d $DEPLOYMENT prompt='cut cat'``

    Args:
        deployment: deployment id
        params: request params dict
        read_stdin: read stdin as request body
        write_file: write response to the file
        key: API key, will try to read from env ``MODELZ_API_KEY`` if not provided
        serde: serilize/deserilize method, choose from [json|msgpack|raw]
        output: output target, choose from [console|file]
    """
    data = params
    if read_stdin:
        # override req data
        data = sys.stdin.buffer.read()

    client = ModelzClient(key=key, deployment=deployment)
    resp = client.inference(params=data, serde=serde)

    if not write_file:
        console.print(resp.data)
    else:
        resp.save_to_file(write_file)
        console.print(f"result has been written in [bold cyan]{write_file}[/bold cyan]")


def metrics(deployment: str, key: Optional[str] = None):
    """Model service metrics.

    Usage:
        ``modelz metrics -d $DEPLOYMENT``

    Args:
        key: API key, will try to read from env ``MODELZ_API_KEY`` if not provided
        deployment: deployment id
    """
    client = ModelzClient(key=key, deployment=deployment)
    client.metrics().show()


def build(repo: str, key: Optional[str] = None):
    """Build the docker image from a GitHub repo"""
    pass


def main():
    """CLI entrypoint."""
    command, args, params = parse_arguments(build_argument_parser())
    if command.startswith("inf"):
        inference(**args, params=params)
    elif command.startswith("metrics"):
        metrics(**args)
    elif command.startswith("build"):
        build(**args)
    else:
        raise NotImplementedError(command)
