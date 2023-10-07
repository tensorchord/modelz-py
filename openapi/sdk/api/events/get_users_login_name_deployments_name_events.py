from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_event_list_response import DeploymentEventListResponse
from ...types import Response


def _get_kwargs(
    login_name: str,
    name: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/users/{login_name}/deployments/{name}/events".format(
            login_name=login_name,
            name=name,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeploymentEventListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeploymentEventListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeploymentEventListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeploymentEventListResponse]:
    """Get events by deployment id and user id

     Get events by deployment id and user id

    Args:
        login_name (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentEventListResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeploymentEventListResponse]:
    """Get events by deployment id and user id

     Get events by deployment id and user id

    Args:
        login_name (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentEventListResponse
    """

    return sync_detailed(
        login_name=login_name,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeploymentEventListResponse]:
    """Get events by deployment id and user id

     Get events by deployment id and user id

    Args:
        login_name (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentEventListResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeploymentEventListResponse]:
    """Get events by deployment id and user id

     Get events by deployment id and user id

    Args:
        login_name (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentEventListResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            name=name,
            client=client,
        )
    ).parsed
