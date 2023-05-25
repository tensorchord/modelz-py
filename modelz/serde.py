from __future__ import annotations

import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

import msgpack  # type: ignore


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


class RawSerde(Serde):
    def encode(self, data: Any) -> str | bytes:
        return data

    def decode(self, data: str | bytes) -> Any:
        return data


class TextSerde(Serde):
    def encode(self, data: Any) -> str | bytes:
        return data.encode("utf-8")

    def decode(self, data: str | bytes) -> Any:
        return data.decode("utf-8")


class SerdeEnum(Enum):
    json = JSONSerde
    msgpack = MsgPackSerde
    raw = RawSerde
    text = TextSerde
