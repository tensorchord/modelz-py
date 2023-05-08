from __future__ import annotations
from typing import Any, Callable
from http import HTTPStatus
from urllib.parse import urljoin

import aiohttp

from rich.console import Console

from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from modelz.env import EnvConfig
from modelz.serde import Serde, SerdeEnum, TextSerde
from modelz.utils import get_ssl_context_no_verify


TIMEOUT = 300
console = Console()
DEFAULT_RESP_SERDE = TextSerde()
DEFAULT_RETRY = 3

def _create_retry_decorator(stop_after: int = DEFAULT_RETRY) -> Callable[[Any], Any]:
    import openai

    min_seconds = 4
    max_seconds = 10
    # Wait 2^x * 1 second between each retry starting with
    # 4 seconds, then up to 10 seconds, then 10 seconds afterwards
    return retry(
        reraise=True,
        stop=stop_after_attempt(stop_after),
        wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
    )

class ModelzAuth:
    def __init__(self, key: str | None = None) -> None:
        config = EnvConfig()
        self.key: str = key if key else config.api_key
        if not self.key:
            raise RuntimeError("cannot find the API key")

    def get_headers(self) -> dict:
        return {"X-API-Key": self.key}


class ModelzResponse:
    def __init__(self, resp: aiohttp.ClientResponse, serde: Serde = DEFAULT_RESP_SERDE):
        """Modelz internal response."""
        if resp.status != HTTPStatus.OK:
            console.print(f"[bold red]err[{resp.status}][/bold red]: {resp.text}")
            raise ValueError(f"inference err with code {resp.status}")
        self.resp = resp
        self.serde = serde
        self._data = None

    async def save_to_file(self, file: str):
        with open(file, "wb") as f:
            f.write(await self.data)

    @property
    async def data(self) -> Any:
        if not self._data:
            self._data = self.serde.decode(await self.resp.content.read())
        return self._data

    async def show(self):
        console.print(await self.data)


class AioModelzClient:
    def __init__(
        self,
        deployment: str | None = None,
        key: str | None = None,
        host: str | None = None,
        timeout: float = TIMEOUT,
    ) -> None:
        # ...
        config = EnvConfig()
        self.host = host if host else config.host
        self.deployment = deployment
        self.auth = ModelzAuth(key)
        self.timeout = timeout
        self.session_request_kwargs = {}
        if not getattr(config, "ssl_verify", True):
            self.session_request_kwargs.update({"ssl": get_ssl_context_no_verify()})

    async def _post(self, url, content, timeout):
        headers = self.auth.get_headers()
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                data=content,
                headers=headers,
                timeout=timeout,
                **self.session_request_kwargs,
            ) as response:
                return response

    async def _get(self, url, timeout):
        headers = self.auth.get_headers()
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers=headers, timeout=timeout, **self.session_request_kwargs
            ) as response:
                return response

    async def inference(
        self,
        params: Any,
        deployment: str | None = None,
        serde: str = "json",
    ) -> ModelzResponse:
        """Get the inference result.

        Args:
            params: request params, will be serialized by `serde`
            deployment: deployment ID
            serde: serialize/deserialize method, choose from ("json", "msg", "raw")
        """
        deploy = deployment if deployment else self.deployment
        assert deploy, "deployment is required"
        self.serde = SerdeEnum[serde.lower()].value()

        with console.status(f"[bold green]Modelz {deploy} inference..."):
            resp = await self._post(
                urljoin(self.host.format(deploy), "/inference"),
                self.serde.encode(params),
                self.timeout,
            )

        return ModelzResponse(resp, self.serde)

    async def metrics(self, deployment: str | None = None) -> ModelzResponse:
        """Get deployment metrics.

        Args:
            deployment: deployment ID
        """
        deploy = deployment if deployment else self.deployment
        assert deploy, "deployment is required"

        with console.status(f"[bold green]Modelz {deploy} metrics..."):
            resp = await self._get(
                urljoin(self.host.format(deploy), "/metrics"),
                self.timeout,
            )

        return ModelzResponse(resp)

    async def build(self, repo: str):
        """Build a Docker image and push it to the registry."""
        with console.status(f"[bold green]Modelz build {repo}..."):
            resp = await self._post(
                urljoin(self.host.format("api"), "/build"),
                None,
                self.timeout,
            )

        ModelzResponse(resp)
        console.print(f"created the build job for repo [bold cyan]{repo}[/bold cyan]")
