from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.server_list import ServerList
from ...types import Response


def _get_kwargs(
    login_name: str,
    cluster_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/users/{login_name}/clusters/{cluster_id}/servers".format(
            login_name=login_name,
            cluster_id=cluster_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ServerList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ServerList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ServerList]:
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
) -> Response[ServerList]:
    """List servers

     List servers

    Args:
        login_name (str):
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerList]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
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
) -> Optional[ServerList]:
    """List servers

     List servers

    Args:
        login_name (str):
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerList
    """

    return sync_detailed(
        login_name=login_name,
        cluster_id=cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ServerList]:
    """List servers

     List servers

    Args:
        login_name (str):
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerList]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    cluster_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ServerList]:
    """List servers

     List servers

    Args:
        login_name (str):
        cluster_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerList
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            cluster_id=cluster_id,
            client=client,
        )
    ).parsed
