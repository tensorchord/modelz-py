from __future__ import annotations
from typing import Any, Generator
import logging
from http import HTTPStatus

import httpx

from .env import EnvConfig
from .serde import Serde, SerdeEnum


TIMEOUT = httpx.Timeout(5, read=30, write=30)
logger = logging.getLogger(__name__)
config = EnvConfig()


class ModelzAuth(httpx.Auth):
    def __init__(self, key: str | None = None) -> None:
        self.key: str = key if key else config.api_key
        if not self.key:
            raise RuntimeError("cannot find the API key")

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["X-API-Key"] = self.key
        yield request


class InferenceResponse:
    def __init__(self, resp: httpx.Response, serde: Serde):
        if resp.status_code != HTTPStatus.OK:
            logger.warn("err[%d]: %s", resp.status_code, resp.text)
            raise ValueError(f"inference err: {resp.text}")
        self.resp = resp
        self.serde = serde
        self._data = None

    def _decode(self) -> Any:
        self._data = self.serde.decode(self.resp.content)
        return self._data

    def save_to_file(self, file: str):
        with open(file, "wb") as f:
            f.write(self.data)

    @property
    def data(self) -> Any:
        return self._decode()


class ModelzClient:
    def __init__(
        self, key: str, project: str, host: str | None = None, serde: str = "json"
    ) -> None:
        """Create a Modelz Client.

        Args:
            key: API key
            project: Project ID
            host: Modelz host address
            serde: serialize/deserialize method, choose from ("json", "msg", "raw")
        """
        self.host = host if host else config.host
        auth = ModelzAuth(key)
        self.project = project
        self.client = httpx.Client(auth=auth, base_url=self.host)
        self.serde: Serde = SerdeEnum[serde.lower()].value()

    def inference(
        self, params: Any, timeout: float | httpx.Timeout = TIMEOUT
    ) -> InferenceResponse:
        """Get the inference result."""
        resp = self.client.post(
            f"/api/v1/mosec/{self.project}/inference",
            content=self.serde.encode(params),
            timeout=timeout,
        )

        return InferenceResponse(resp, self.serde)

    def metrics(self, timeout: float | httpx.Timeout = TIMEOUT) -> str:
        """Get deployment metrics."""
        resp = self.client.get(
            f"/api/v1/mosec/{self.project}/metrics",
            timeout=timeout,
        )
        if resp.status_code != HTTPStatus.OK:
            logger.warn("err[%d]: %s", resp.status_code, resp.text)
            raise RuntimeError(f"fetch metrics error: {resp.text}")
        return resp.text
