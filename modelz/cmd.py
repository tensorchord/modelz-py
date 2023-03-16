from typing import Optional, List
from enum import Enum
from random import randrange

import typer

from .client import ModelzClient


class Output(str, Enum):
    console = "console"
    file = "file"


cli = typer.Typer(
    name="modelz",
    no_args_is_help=True,
    pretty_exceptions_short=True,
    pretty_exceptions_show_locals=False,
)


@cli.command(no_args_is_help=True)
def inference(
    project: str,
    params: List[str] = None,
    file: Optional[str] = None,
    key: Optional[str] = None,
    serde: str = "json",
    output: Output = Output.console,
):
    """Model inference.

    Example:

        `modelz inference $PROJECT --param prompt="cut cat"`

    Args:

        project: project id

        params: request params list in the "key=value" format
            i.e. `--params prompt='cute cat' --params temperature=0.75"`

        file: read file as request body

        key: API key, will try to read from env `MODELZ_API_KEY` if not provided

        serde: serilization method, choose from [json|msgpack|raw]

        output: output target, choose from [console|file]
    """
    data = dict(pair.split("=", 1) for pair in params)
    if file:
        with open(file, "rb") as f:
            data = f.read()
    client = ModelzClient(key=key, project=project, serde=serde)
    resp = client.inference(params=data)

    if output == output.console:
        print(resp.data)
    elif output == output.file:
        filename = f"modelz_{project}_{randrange(2**32):x}"
        with open(filename, "wb") as f:
            f.write(data)
        print(f"result has been written in {filename}")


@cli.command(no_args_is_help=True)
def metrics(project: str, key: Optional[str] = None):
    """Model service metrics.

    Usage:
        `modelz metrics $PROJECT`

    Args:

        key: API key, will try to read from env `MODELZ_API_KEY` if not provided

        project: project id
    """
    client = ModelzClient(key=key, project=project)
    print(client.metrics())


def main():
    cli()
