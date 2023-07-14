from gradio_client import Client

from modelz.env import EnvConfig

config = EnvConfig()


class GradioClient:
    """Create a Gradio Client with Modelz endpoints.
    Args:
        host: Modelz host address
    """

    def __init__(
        self,
        host: str = None,
    ) -> None:
        self.host = host if host else config.host
        self._client = Client(self.host)

    def __getattr__(self, attr):
        """Delegate access to implement the composition."""
        return getattr(self._client, attr)
