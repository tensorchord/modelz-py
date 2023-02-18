from typing import Any, Generator

from httpx import Client, Auth, Request, Response


class ModelzAuth(Auth):
    def __init__(self, token) -> None:
        self.token = token

    def auth_flow(self, request: Request) -> Generator[Request, Response, None]:
        request.headers["X-API-Key"] = self.token
        yield request


class ModelzClient:
    URL = "https://api.modelz.ai/"

    def __init__(self, token: str, project: str) -> None:
        auth = ModelzAuth(token)
        self.project = project
        self.client = Client(auth=auth, base_url=f"{self.URL}/{project}/")

