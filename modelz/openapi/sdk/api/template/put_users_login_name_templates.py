from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_tensorchord_modelz_apiserver_pkg_query_template import (
    GithubComTensorchordModelzApiserverPkgQueryTemplate,
)
from ...models.template_update_request import TemplateUpdateRequest
from ...types import Response


def _get_kwargs(
    login_name: str,
    *,
    json_body: TemplateUpdateRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/users/{login_name}/templates".format(
            login_name=login_name,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GithubComTensorchordModelzApiserverPkgQueryTemplate.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
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
    json_body: TemplateUpdateRequest,
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Update the template.

     Update the template.

    Args:
        login_name (str):
        json_body (TemplateUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: TemplateUpdateRequest,
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Update the template.

     Update the template.

    Args:
        login_name (str):
        json_body (TemplateUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverPkgQueryTemplate
    """

    return sync_detailed(
        login_name=login_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: TemplateUpdateRequest,
) -> Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Update the template.

     Update the template.

    Args:
        login_name (str):
        json_body (TemplateUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GithubComTensorchordModelzApiserverPkgQueryTemplate]
    """

    kwargs = _get_kwargs(
        login_name=login_name,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    login_name: str,
    *,
    client: AuthenticatedClient,
    json_body: TemplateUpdateRequest,
) -> Optional[GithubComTensorchordModelzApiserverPkgQueryTemplate]:
    """Update the template.

     Update the template.

    Args:
        login_name (str):
        json_body (TemplateUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GithubComTensorchordModelzApiserverPkgQueryTemplate
    """

    return (
        await asyncio_detailed(
            login_name=login_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
