from __future__ import annotations
from typing import Any
from http import HTTPStatus
from urllib.parse import urljoin

import aiohttp

# from aiohttp import hdrs
from rich.console import Console

from .env import EnvConfig
from .serde import Serde, SerdeEnum, TextSerde


TIMEOUT = 300
console = Console()
DEFAULT_RESP_SERDE = TextSerde()
DEFAULT_RETRY = 3


# class ModelzAuth:
#     def __init__(self, key: str | None = None) -> None:
#         self.key: str = key if key else config.api_key
#         if not self.key:
#             raise RuntimeError("cannot find the API key")

#     async def auth_request(self, request: aiohttp.ClientRequest):
#         request.headers[hdrs.X_API_KEY] = self.key
#         return request


class ModelzAuth:
    def __init__(self, key: str | None = None) -> None:
        config = EnvConfig()
        self.key: str = key if key else config.api_key
        if not self.key:
            raise RuntimeError("cannot find the API key")

    async def auth_request(self, request: aiohttp.ClientRequest):
        request.headers["X-API-Key"] = self.key
        return request


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


class ModelzClient:
    def __init__(
        self,
        deployment: str | None = None,
        key: str | None = None,
        host: str | None = None,
        timeout: float = TIMEOUT,
    ) -> None:
        # ...
        self.host = host if host else config.host
        self.deployment = deployment
        self.auth = ModelzAuth(key)
        self.timeout = timeout

    async def _post(self, url, content, timeout):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=content, headers=self.auth.auth_request, timeout=timeout) as response:
                return response

    async def _get(self, url, timeout):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.auth.auth_request, timeout=timeout) as response:
                return response

    async def inference(
        self,
        params: Any,
        deployment: str | None = None,
        serde: str = "json",
    ) -> ModelzResponse:
        # ...
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
        # ...
        deploy = deployment if deployment else self.deployment
        assert deploy, "deployment is required"

        with console.status(f"[bold green]Modelz {deploy} metrics..."):
            resp = await self._get(
                urljoin(self.host.format(deploy), "/metrics"),
                self.timeout,
            )

        return ModelzResponse(resp)

    async def build(self, repo: str):
        # ...
        with console.status(f"[bold green]Modelz build {repo}..."):
            resp = await self._post(
                urljoin(self.host.format("api"), "/build"),
                None,
                self.timeout,
            )

        ModelzResponse(resp)
        console.print(f"created the build job for repo [bold cyan]{repo}[/bold cyan]")
