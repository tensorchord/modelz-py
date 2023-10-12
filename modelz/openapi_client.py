import httpx

from modelz.openapi.sdk.api.deployment import (
    delete_users_login_name_clusters_cluster_id_deployments_name,
    get_users_login_name_clusters_cluster_id_deployments,
    get_users_login_name_clusters_cluster_id_deployments_name,
    post_users_login_name_clusters_cluster_id_deployments,
    put_users_login_name_clusters_cluster_id_deployments_name,
)
from modelz.openapi.sdk.client import AuthenticatedClient
from modelz.openapi.sdk.models import (
    DeploymentCreateRequest,
    DeploymentListResponse,
    DeploymentResponse,
    DeploymentUpdateRequest,
)
from modelz.openapi.sdk.types import Response

TIMEOUT = httpx.Timeout(5, read=300, write=300)


class DeploymentClient:
    def __init__(
        self,
        login_name: str,
        key: str,
        host: str = "https://cloud.modelz.ai/api/v1",
        cluster_id: str = "modelz",
    ):
        """Create a Modelz Client for deployments.

        Args:
            login_name: UUID for operated user
            key: API key
            host: ModelZ apiserver base URL
            cluster_id: cluster UUID for operated agent
        """
        self.client = (
            AuthenticatedClient(base_url=host, token=key)
            .with_timeout(TIMEOUT)
            .with_headers({"X-API-Key": key})
        )
        self.login_name = login_name
        self.host = host
        self.cluster_id = cluster_id

    def create(self, req: DeploymentCreateRequest) -> Response[DeploymentResponse]:
        """Create a new deployment.

        Args:
            req: spec of request body
        """
        return post_users_login_name_clusters_cluster_id_deployments.sync_detailed(
            login_name=self.login_name,
            cluster_id=self.cluster_id,
            client=self.client,
            json_body=req,
        )

    def list(self) -> Response[DeploymentListResponse]:
        """Create all exist deployments."""
        return get_users_login_name_clusters_cluster_id_deployments.sync_detailed(
            login_name=self.login_name, cluster_id=self.cluster_id, client=self.client
        )

    def get(self, deployment_id: str) -> Response[DeploymentResponse]:
        """Get exist deployment by id

        Args:
            deployment_id: deployment id
        """
        return get_users_login_name_clusters_cluster_id_deployments_name.sync_detailed(
            login_name=self.login_name,
            cluster_id=self.cluster_id,
            name=deployment_id,
            client=self.client,
        )

    def update(
        self, deployment_id: str, req: DeploymentUpdateRequest
    ) -> Response[DeploymentResponse]:
        """Update editable spec of any exist deployments.


        Args:
            deployment_id: deployment id
            req: spec of request body
        """
        return put_users_login_name_clusters_cluster_id_deployments_name.sync_detailed(
            login_name=self.login_name,
            cluster_id=self.cluster_id,
            name=deployment_id,
            client=self.client,
            json_body=req,
        )

    def delete(self, deployment_id: str) -> Response[None]:
        """Delete any exist deployments.


        Args:
            deployment_id: deployment id
        """
        return (
            delete_users_login_name_clusters_cluster_id_deployments_name.sync_detailed(
                login_name=self.login_name,
                cluster_id=self.cluster_id,
                name=deployment_id,
                client=self.client,
            )
        )
