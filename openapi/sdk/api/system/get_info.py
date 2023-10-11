from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.version import Version
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    with_agent: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["with-agent"] = with_agent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/info",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Version]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Version.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Version]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    with_agent: Union[Unset, None, bool] = UNSET,
) -> Response[Version]:
    """Get system info.

     Get system info.

    Args:
        with_agent (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Version]
    """

    kwargs = _get_kwargs(
        with_agent=with_agent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    with_agent: Union[Unset, None, bool] = UNSET,
) -> Optional[Version]:
    """Get system info.

     Get system info.

    Args:
        with_agent (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Version
    """

    return sync_detailed(
        client=client,
        with_agent=with_agent,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    with_agent: Union[Unset, None, bool] = UNSET,
) -> Response[Version]:
    """Get system info.

     Get system info.

    Args:
        with_agent (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Version]
    """

    kwargs = _get_kwargs(
        with_agent=with_agent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    with_agent: Union[Unset, None, bool] = UNSET,
) -> Optional[Version]:
    """Get system info.

     Get system info.

    Args:
        with_agent (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Version
    """

    return (
        await asyncio_detailed(
            client=client,
            with_agent=with_agent,
        )
    ).parsed
