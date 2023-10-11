from typing import Optional

import httpx

from modelz.env import EnvConfig
from openapi.sdk.api.deployment import (
    delete_users_login_name_clusters_cluster_id_deployments_name,
    get_users_login_name_clusters_cluster_id_deployments,
    post_users_login_name_clusters_cluster_id_deployments,
    put_users_login_name_clusters_cluster_id_deployments_name,
)
from openapi.sdk.client import AuthenticatedClient
from openapi.sdk.models import DeploymentCreateRequest
from openapi.sdk.models.deployment_list_response import DeploymentListResponse
from openapi.sdk.models.deployment_response import DeploymentResponse
from openapi.sdk.models.deployment_update_request import DeploymentUpdateRequest
from openapi.sdk.types import Response

TIMEOUT = httpx.Timeout(5, read=300, write=300)
config = EnvConfig()


class DeploymentClient:
    def __init__(
        self,
        login_name: str,
        key: str,
        host: Optional[str] = None,
        cluster_id: str = "modelz",
    ):
        """Create a Modelz Client for deployments.

        Args:
            login_name: UUID for operated user
            key: API key
            host: endpoint URL
            cluster_id: cluster UUID for operated agent
        """
        self.host = host if host else config.host
        self.client = (
            AuthenticatedClient(base_url=self.host.format("cloud"), token=key)
            .with_timeout(TIMEOUT)
            .with_headers({"X-API-Key": key})
        )
        self.login_name = login_name
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

    def update(
        self, name: str, req: DeploymentUpdateRequest
    ) -> Response[DeploymentResponse]:
        """Update editable spec of any exist deployments.


        Args:
            name: deployment id
            req: spec of request body
        """
        return put_users_login_name_clusters_cluster_id_deployments_name.sync_detailed(
            login_name=self.login_name,
            cluster_id=self.cluster_id,
            name=name,
            client=self.client,
            json_body=req,
        )

    def delete(self, name: str) -> Response[None]:
        """Delete any exist deployments.


        Args:
            name: deployment id
        """
        return (
            delete_users_login_name_clusters_cluster_id_deployments_name.sync_detailed(
                login_name=self.login_name,
                cluster_id=self.cluster_id,
                name=name,
                client=self.client,
            )
        )
