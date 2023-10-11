from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metric_response import MetricResponse
from ...types import UNSET, Response


def _get_kwargs(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    start: str,
    end: str,
    step: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["start"] = start

    params["end"] = end

    params["step"] = step

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/users/{login_name}/clusters/{cluster_id}/deployments/{name}/metrics/available_replicas".format(
            login_name=login_name,
            cluster_id=cluster_id,
            name=name,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MetricResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MetricResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MetricResponse]:
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
    start: str,
    end: str,
    step: str,
) -> Response[MetricResponse]:
    """Get the deployment replicas metrics.

     Get the deployment replicas metrics with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        start=start,
        end=end,
        step=step,
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
    start: str,
    end: str,
    step: str,
) -> Optional[MetricResponse]:
    """Get the deployment replicas metrics.

     Get the deployment replicas metrics with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricResponse
    """

    return sync_detailed(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        client=client,
        start=start,
        end=end,
        step=step,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
    step: str,
) -> Response[MetricResponse]:
    """Get the deployment replicas metrics.

     Get the deployment replicas metrics with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricResponse]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        cluster_id=cluster_id,
        name=name,
        start=start,
        end=end,
        step=step,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    cluster_id: str,
    name: str,
    *,
    client: AuthenticatedClient,
    start: str,
    end: str,
    step: str,
) -> Optional[MetricResponse]:
    """Get the deployment replicas metrics.

     Get the deployment replicas metrics with the given deployment name.

    Args:
        login_name (str):
        cluster_id (str):
        name (str):
        start (str):
        end (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricResponse
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            cluster_id=cluster_id,
            name=name,
            client=client,
            start=start,
            end=end,
            step=step,
        )
    ).parsed
