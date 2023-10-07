from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.managed_cluster import ManagedCluster
from ...types import Response


def _get_kwargs(
    login_name: str,
    cluster_id: str,
    *,
    json_body: ManagedCluster,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/users/{login_name}/clusters/{cluster_id}".format(
            login_name=login_name,
            cluster_id=cluster_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ManagedCluster]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ManagedCluster.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ManagedCluster]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ManagedCluster,
) -> Response[ManagedCluster]:
    """Update a managed cluster

     Update a managed cluster

    Args:
        login_name (str):
        cluster_id (str):
        json_body (ManagedCluster):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagedCluster]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ManagedCluster,
) -> Optional[ManagedCluster]:
    """Update a managed cluster

     Update a managed cluster

    Args:
        login_name (str):
        cluster_id (str):
        json_body (ManagedCluster):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagedCluster
    """

    return sync_detailed(
        login_name=login_name,
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ManagedCluster,
) -> Response[ManagedCluster]:
    """Update a managed cluster

     Update a managed cluster

    Args:
        login_name (str):
        cluster_id (str):
        json_body (ManagedCluster):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagedCluster]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
    json_body: ManagedCluster,
) -> Optional[ManagedCluster]:
    """Update a managed cluster

     Update a managed cluster

    Args:
        login_name (str):
        cluster_id (str):
        json_body (ManagedCluster):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagedCluster
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
