from __future__ import annotations
import os
from modelz.utils import strtobool

PREFIX: str = "MODELZ_"


class EnvConfig:
    def __init__(self) -> None:
        self.api_key: str
        self.host: str = "https://{}.modelz.io/"
        self.update_from_env()

    def update_from_env(self):
        for key in ("api_key", "host", "ssl_verify"):
            val = os.environ.get(f"{PREFIX}{key.upper()}")
            if key == 'ssl_verify' and val is not None:
                val = strtobool(val)
            if val is not None:
                setattr(self, key, val)
