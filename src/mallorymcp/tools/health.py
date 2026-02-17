"""MCP tool for health check and authentication verification."""

from typing import Any

from ..decorator.api import handle_api_errors
from ..server.server import get_client, mcp


@mcp.tool()
@handle_api_errors
async def health_check() -> dict[str, Any]:
    """Check API connectivity, verify authentication, and
    return the current user.

    Use for: verifying the MCP server is properly configured,
    confirming the API key is valid, and identifying which
    user account is active.

    Returns:
        A dict with 'api' (health status) and 'user' (current
        user info including uuid, email, first_name, last_name).
        If authentication fails the 'user' key will contain
        an error message instead.
    """
    client = get_client()

    api_status = await client.health()

    try:
        user_info = await client.whoami()
    except Exception as exc:
        user_info = {"error": str(exc)}

    return {
        "api": api_status,
        "user": user_info,
    }
