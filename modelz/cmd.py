from typing import Optional, List

import typer

from .client import ModelzClient


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
    read_file: Optional[str] = None,
    write_file: Optional[str] = None,
    key: Optional[str] = None,
    serde: str = "json",
):
    """Model inference.

    Example:

        `modelz inference $PROJECT --param prompt="cut cat"`

    Args:

        project: project id

        params: request params list in the "key=value" format
            i.e. `--params prompt='cute cat' --params temperature=0.75"`

        read_file: read file as request body. If params are also provided,
            this will be append as the value of "file" in the request body.

        write_file: write response to the file

        key: API key, will try to read from env `MODELZ_API_KEY` if not provided

        serde: serilize/deserilize method, choose from [json|msgpack|raw]

        output: output target, choose from [console|file]
    """
    data = dict(pair.split("=", 1) for pair in params)
    if read_file:
        with open(read_file, "rb") as f:
            content = f.read()
        if data:
            data["file"] = content
        else:
            data = content

    client = ModelzClient(key=key, project=project, serde=serde)
    resp = client.inference(params=data)

    if not write_file:
        print(resp.data)
    else:
        resp.save_to_file(write_file)
        print(f"result has been written in {write_file}")


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
