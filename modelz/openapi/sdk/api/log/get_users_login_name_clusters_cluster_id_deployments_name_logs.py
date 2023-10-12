from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deployment_log_response import DeploymentLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    since: str,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["since"] = since

    params["end"] = end

    params["tail"] = tail

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/users/{login_name}/clusters/{cluster_id}/deployments/{name}/logs".format(
            login_name=login_name,
            cluster_id=cluster_id,
            name=name,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeploymentLogResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeploymentLogResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeploymentLogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: str,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[DeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        since (str):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        since=since,
        end=end,
        tail=tail,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: str,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Optional[DeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        since (str):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogResponse
    """

    return sync_detailed(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        client=client,
        since=since,
        end=end,
        tail=tail,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: str,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Response[DeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        since (str):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeploymentLogResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        since=since,
        end=end,
        tail=tail,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    since: str,
    end: Union[Unset, None, str] = UNSET,
    tail: Union[Unset, None, int] = UNSET,
) -> Optional[DeploymentLogResponse]:
    """Get the deployment log.

     Get the deployment log with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        since (str):
        end (Union[Unset, None, str]):
        tail (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeploymentLogResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            cluster_id=cluster_id,
            name=name,
            client=client,
            since=since,
            end=end,
            tail=tail,
        )
    ).parsed
