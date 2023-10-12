import json
import os
import re

from rich.console import Console

from modelz.openapi.sdk.types import Response


class ModelzConsole:
    class Status:
        def __init__(self, msg) -> None:
            self.msg = msg

        def __enter__(self):
            print(self.msg)

        def __exit__(self, exc_type, exc_value, traceback):
            pass

    def __init__(self) -> None:
        self._remove_style = re.compile(r"\[.*?\]")
        self.formatter = lambda msg: self._remove_style.sub("", msg)

    def status(self, msg: str):
        return self.Status(self.formatter(msg))

    def print(self, msg: str):
        print(self.formatter(msg))


console = (
    ModelzConsole()
    if os.environ.get("MODELZ_DISABLE_RICH", "").lower() == "true"
    else Console()
)


def jsonFormattedPrint(resp: Response):
    if hasattr(resp.parsed, "to_dict") and callable(resp.parsed.to_dict):
        formatted = json.dumps(resp.parsed.to_dict(), indent=2)
    else:
        formatted = resp.content.decode(errors="ignore")
    console.print(formatted)
