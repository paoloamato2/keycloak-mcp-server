import os
import json
from typing import cast

import pytest
import mcp.types as t
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from keycloak_mcp_server.server import create_server


@pytest.fixture(scope="module")
def keycloak_url():
    container = DockerContainer("quay.io/keycloak/keycloak:26.5.3")
    container.with_command("start-dev")
    container.with_env("KC_BOOTSTRAP_ADMIN_USERNAME", "admin")
    container.with_env("KC_BOOTSTRAP_ADMIN_PASSWORD", "admin")
    container.with_exposed_ports(8080)

    with container as kc:
        wait_for_logs(kc, "Listening on:", timeout=120)  # type: ignore

        host = kc.get_container_host_ip()
        port = kc.get_exposed_port(8080)
        url = f"http://{host}:{port}"

        os.environ["KEYCLOAK_URL"] = url
        os.environ["KEYCLOAK_ADMIN_USERNAME"] = "admin"
        os.environ["KEYCLOAK_ADMIN_PASSWORD"] = "admin"
        os.environ["KEYCLOAK_ADMIN_REALM"] = "master"
        os.environ["KEYCLOAK_CLIENT_ID"] = "admin-cli"

        yield url


@pytest.mark.asyncio
async def test_mcp_server_tools(keycloak_url):
    s, c = create_server()

    try:
        handler = s.request_handlers[t.CallToolRequest]
        req = t.CallToolRequest(
            method="tools/call",
            params=t.CallToolRequestParams(name="list_realms", arguments={}),
        )

        res = await handler(req)

        # In MCP standard Python SDK SDK, the handler returns a RootModel
        tool_result = cast(t.CallToolResult, getattr(res, "root", res))

        assert tool_result.isError is False

        content = tool_result.content[0]
        # In Pydantic based MCP types, we access the fields directly
        assert content.type == "text"

        data = json.loads(content.text)

        # If it was an error caught by our server, the text would be {"error": ...}
        assert "error" not in data, f"Server returned error: {data}"

        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0]["realm"] == "master"

    finally:
        await c.close()
