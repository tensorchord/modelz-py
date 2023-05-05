from __future__ import annotations
import asyncio
from typing import Any
from modelz.aioclient import ModelzResponse, ModelzClient as AioModelzClient
from modelz.aioclient import TIMEOUT


class ModelzClient:
    def __init__(
        self,
        deployment: str | None = None,
        key: str | None = None,
        host: str | None = None,
        timeout: float = TIMEOUT,
    ) -> None:
        """Create a Modelz Client.

        Args:
            deployment: deployment ID
            key: API key
            host: Modelz host address
            timeout: request timeout (second)
        """
        self.client = AioModelzClient(
            deployment=deployment,
            key=key,
            host=host,
            timeout=timeout,
        )

    def inference(
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
        return asyncio.run(self.client.inference(params, deployment, serde))

    def metrics(self, deployment: str | None = None) -> ModelzResponse:
        """Get deployment metrics.

        Args:
            deployment: deployment ID
        """
        return asyncio.run(self.client.metrics(deployment))

    def build(self, repo: str):
        """Build a Docker image and push it to the registry."""

        return asyncio.run(self.client.build(repo))

    async def ainference(
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
        return await self.client.inference(params, deployment, serde)

    async def ametrics(self, deployment: str | None = None) -> ModelzResponse:
        """Get deployment metrics.

        Args:
            deployment: deployment ID
        """
        return await self.client.metrics(deployment)

    async def abuild(self, repo: str):
        """Build a Docker image and push it to the registry."""

        return await self.client.build(repo)
