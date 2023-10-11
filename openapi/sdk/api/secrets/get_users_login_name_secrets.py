from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secret_list_response import SecretListResponse
from ...types import Response


def _get_kwargs(
    login_name: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/users/{login_name}/secrets".format(
            login_name=login_name,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SecretListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SecretListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SecretListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[SecretListResponse]:
    """List secrets

     List secrets

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretListResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SecretListResponse]:
    """List secrets

     List secrets

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretListResponse
    """

    return sync_detailed(
        login_name=login_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[SecretListResponse]:
    """List secrets

     List secrets

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretListResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SecretListResponse]:
    """List secrets

     List secrets

    Args:
        login_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretListResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            client=client,
        )
    ).parsed
