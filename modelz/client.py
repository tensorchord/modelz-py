from __future__ import annotations
from typing import Any, Generator
import json
import logging
from abc import ABC, abstractmethod

import httpx
import msgpack  # type: ignore


logger = logging.getLogger(__name__)


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
        if resp.status_code != 200:
            logger.warn("err[%d]: %s", resp.status_code, resp.text)
            raise ValueError(f"Inference err: {resp.text}")
        self.resp = resp
        self.serde = serde
        self._data = None

    def decode(self) -> Any:
        self._data = self.serde.decode(self.resp.content)

    def save_as_img(self, file: str):
        with open(file, "wb") as f:
            f.write(self.data)

    @property
    def data(self) -> Any:
        return self.decode()


class ModelzClient:
    URL = "https://api.modelz.ai/"

    def __init__(self, token: str, project: str, serde: str = "json") -> None:
        auth = ModelzAuth(token)
        self.project = project
        self.client = httpx.Client(auth=auth, base_url=f"{self.URL}/{project}/")
        self.serde: Serde = SERDE[serde.lower()]()

    def query(self, params: Any, timeout: float | None = None) -> InferenceResponse:
        resp = self.client.post(
            "inference", content=self.serde.encode(params), timeout=timeout
        )

        return InferenceResponse(resp, self.serde)
