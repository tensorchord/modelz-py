from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team_member_response import TeamMemberResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    sign: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sign"] = sign

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/teams/accept_invite",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TeamMemberResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TeamMemberResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TeamMemberResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sign: str,
) -> Response[TeamMemberResponse]:
    """Invite a user to the team.

     Invite a user to the team.

    Args:
        sign (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamMemberResponse]
    """

    kwargs = _get_kwargs(
        sign=sign,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    sign: str,
) -> Optional[TeamMemberResponse]:
    """Invite a user to the team.

     Invite a user to the team.

    Args:
        sign (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamMemberResponse
    """

    return sync_detailed(
        client=client,
        sign=sign,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    sign: str,
) -> Response[TeamMemberResponse]:
    """Invite a user to the team.

     Invite a user to the team.

    Args:
        sign (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamMemberResponse]
    """

    kwargs = _get_kwargs(
        sign=sign,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    sign: str,
) -> Optional[TeamMemberResponse]:
    """Invite a user to the team.

     Invite a user to the team.

    Args:
        sign (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamMemberResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            sign=sign,
        )
    ).parsed
