from gradio_client import Client


class GradioClient:
    """Create a Gradio Client with Modelz endpoints.
    Args:
        endpoint: endpoint URL
    """

    def __init__(
        self,
        endpoint: str = None,
    ) -> None:
        self._client = Client(endpoint)

    def __getattr__(self, attr):
        """Delegate access to implement the composition."""
        return getattr(self._client, attr)
