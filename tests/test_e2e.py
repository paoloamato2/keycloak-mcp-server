import os
import pytest
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from keycloak_mcp_server.config import KeycloakConfig
from keycloak_mcp_server.client import KeycloakClient


@pytest.fixture(scope="module")
def keycloak_url():
    container = DockerContainer("quay.io/keycloak/keycloak:26.0.4")
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
async def test_keycloak_client_connection(keycloak_url):
    config = KeycloakConfig()
    client = KeycloakClient(config)

    try:
        result = await client.request("GET", "/admin/realms")
        assert isinstance(result, list)
        assert len(result) > 0
        assert result[0]["realm"] == "master"
    finally:
        await client.close()
