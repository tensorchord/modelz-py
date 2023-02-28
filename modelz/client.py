from __future__ import annotations
from typing import Any, Generator
import json
import logging
from abc import ABC, abstractmethod
from http import HTTPStatus

import httpx
import msgpack  # type: ignore


logger = logging.getLogger(__name__)
TIMEOUT = httpx.Timeout(5, read=30, write=30)


class Serde(ABC):
    """Serilization and deserilization."""

    @abstractmethod
    def encode(self, data: Any) -> str | bytes:
        raise NotImplementedError

    @abstractmethod
    def decode(self, data: str | bytes) -> Any:
        raise NotImplementedError


class JSONSerde(Serde):
    def encode(self, data: Any) -> str | bytes:
        return json.dumps(data)

    def decode(self, data: str | bytes) -> Any:
        return json.loads(data)


class MsgPackSerde(Serde):
    def encode(self, data: Any) -> str | bytes:
        return msgpack.packb(data)

    def decode(self, data: str | bytes) -> Any:
        return msgpack.unpackb(data)


SERDE = {
    "json": JSONSerde,
    "msgpack": MsgPackSerde,
}


class ModelzAuth(httpx.Auth):
    def __init__(self, token) -> None:
        self.token = token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["X-API-Key"] = self.token
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

    def save_as_img(self, file: str):
        with open(file, "wb") as f:
            f.write(self.data)

    @property
    def data(self) -> Any:
        return self._decode()


class ModelzClient:
    URL = "https://api.modelz.ai/"

    def __init__(
        self, token: str, project: str, host: str | None = None, serde: str = "json"
    ) -> None:
        auth = ModelzAuth(token)
        self.project = project
        self.client = httpx.Client(auth=auth, base_url=host if host else self.URL)
        self.serde: Serde = SERDE[serde.lower()]()

    def inference(
        self, params: Any, timeout: float | httpx.Timeout = TIMEOUT
    ) -> InferenceResponse:
        resp = self.client.post(
            f"/api/v1/mosec/{self.project}/inference",
            content=self.serde.encode(params),
            timeout=timeout,
        )

        return InferenceResponse(resp, self.serde)

    def metrics(self, timeout: float | httpx.Timeout = TIMEOUT) -> str:
        resp = self.client.get(
            f"/api/v1/mosec/{self.project}/metrics",
            timeout=timeout,
        )
        if resp.status_code != HTTPStatus.OK:
            logger.warn("err[%d]: %s", resp.status_code, resp.text)
            raise RuntimeError(f"fetch metrics error: {resp.text}")
        return resp.text
