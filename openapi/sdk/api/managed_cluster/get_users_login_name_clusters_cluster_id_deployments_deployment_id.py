from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    login_name: str,
    cluster_id: str,
    deployment_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/users/{login_name}/clusters/{cluster_id}/deployments/{deployment_id}".format(
            login_name=login_name,
            cluster_id=cluster_id,
            deployment_id=deployment_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[str]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    cluster_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[str]:
    """Get managed cluster user by deployment id

     Get managed cluster user by deployment id

    Args:
        login_name (str):
        cluster_id (str):
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        deployment_id=deployment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    cluster_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[str]:
    """Get managed cluster user by deployment id

     Get managed cluster user by deployment id

    Args:
        login_name (str):
        cluster_id (str):
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        login_name=login_name,
        cluster_id=cluster_id,
        deployment_id=deployment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    cluster_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[str]:
    """Get managed cluster user by deployment id

     Get managed cluster user by deployment id

    Args:
        login_name (str):
        cluster_id (str):
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        deployment_id=deployment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    cluster_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[str]:
    """Get managed cluster user by deployment id

     Get managed cluster user by deployment id

    Args:
        login_name (str):
        cluster_id (str):
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            cluster_id=cluster_id,
            deployment_id=deployment_id,
            client=client,
        )
    ).parsed
