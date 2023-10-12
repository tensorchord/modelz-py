from __future__ import annotations

from http import HTTPStatus
from typing import Any, Generator
from urllib.parse import urljoin

import httpx

from modelz.console import console
from modelz.serde import Serde, SerdeEnum, TextSerde

TIMEOUT = httpx.Timeout(5, read=300, write=300)
DEFAULT_RESP_SERDE = TextSerde()
DEFAULT_RETRY = 3


class ModelzAuth(httpx.Auth):
    def __init__(self, key: str) -> None:
        self.key: str = key
        if not self.key:
            raise RuntimeError("cannot find the API key")

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["X-API-Key"] = self.key
        yield request


class ModelzResponse:
    """Modelz internal response.

    The initialization will raise an error if the response status code is not 200.
    """

    def __init__(self, resp: httpx.Response, serde: Serde = DEFAULT_RESP_SERDE):
        if resp.status_code != HTTPStatus.OK:
            console.print(f"[bold red]err[{resp.status_code}][/bold red]: {resp.text}")
            raise ValueError(f"inference err with code {resp.status_code}")
        self.resp = resp
        self.serde = serde
        self._data = None

    def save_to_file(self, file: str):
        """Save the response data to a file in binary format."""
        with open(file, "wb") as f:
            f.write(self.data)

    @property
    def data(self) -> Any:
        """Access the response data.

        It will be decoded by the serde method provided.
        """
        if not self._data:
            self._data = self.serde.decode(self.resp.content)
        return self._data

    def show(self):
        """Display the response data in the console with color."""
        console.print(self.data)


class ModelzClient:
    """Create a Modelz Client for standalone commands.

    Args:
        endpoint: endpoint URL
        key: API key
        timeout: request timeout (second)
    """

    def __init__(
        self,
        key: str,
        endpoint: str | None = None,
        timeout: float | httpx.Timeout = TIMEOUT,
    ) -> None:
        self.endpoint = endpoint
        auth = ModelzAuth(key)
        transport = httpx.HTTPTransport(retries=DEFAULT_RETRY)
        self.client = httpx.Client(auth=auth, transport=transport)
        self.serde: Serde
        self.timeout = timeout

    def inference(
        self,
        params: Any,
        serde: str = "json",
    ) -> ModelzResponse:
        """Get the inference result.

        Args:
            params: request params, will be serialized by ``serde``
            serde: serialize/deserialize method, choose from ("json", "msgpack", "raw")
        """
        self.serde = SerdeEnum[serde.lower()].value()

        with console.status(f"[bold green]Modelz {self.endpoint} inference..."):
            resp = self.client.post(
                urljoin(self.endpoint, "/inference"),
                content=self.serde.encode(params),
                timeout=self.timeout,
            )

        return ModelzResponse(resp, self.serde)

    def metrics(self, deployment: str | None = None) -> ModelzResponse:
        """Get deployment metrics.

        Args:
            deployment: deployment ID
        """
        deploy = deployment if deployment else self.deployment
        assert deploy, "deployment is required"

        with console.status(f"[bold green]Modelz {deploy} metrics..."):
            resp = self.client.get(
                urljoin(self.host.format(deploy), "/metrics"),
                timeout=self.timeout,
            )

        return ModelzResponse(resp)

    def build(self, repo: str):
        """Build a Docker image and push it to the registry.

        Args:
            repo: git repo url
        """
        with console.status(f"[bold green]Modelz build {repo}..."):
            resp = self.client.post(
                urljoin(self.host.format("api"), "/build"),
                timeout=self.timeout,
            )

        ModelzResponse(resp)
        console.print(f"created the build job for repo [bold cyan]{repo}[/bold cyan]")
