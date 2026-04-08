# Keycloak MCP Server

<p align="center">
  <img src="https://img.shields.io/badge/Keycloak-REST_API-00B2B2?style=for-the-badge&logo=keycloak&logoColor=white" alt="Keycloak version">
  <img src="https://img.shields.io/badge/MCP-Model_Context_Protocol-5A67D8?style=for-the-badge" alt="MCP">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/license/paoloamato2/keycloak-mcp-server?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/paoloamato2/keycloak-mcp-server?style=for-the-badge" alt="Stars">
</p>

<p align="center">
  <strong>A comprehensive <a href="https://modelcontextprotocol.io">Model Context Protocol (MCP)</a> server that exposes the <a href="https://www.keycloak.org/docs-api/latest/rest-api/index.html">Keycloak Admin REST API</a> as typed MCP tools. 299 tools covering all API categories.</strong>
</p>

---

## Features

- **Complete API coverage**: All 299 Keycloak Admin REST API endpoints
- **Dual transport**: stdio (Claude Code) and SSE (GitHub Copilot, other MCP clients)
- **Auto-authentication**: Supports both password and client credentials flows with automatic token refresh
- **Zero configuration tools**: Each tool is self-describing with full input schemas

### API Categories

| Category | Tools |
|---|---|
| Attack Detection | 3 |
| Authentication Management | 38 |
| Client Certificates | 6 |
| Client Initial Access | 3 |
| Client Registration Policy | 1 |
| Client Role Mappings | 10 |
| Client Scopes | 10 |
| Clients | 33 |
| Components | 6 |
| Groups | 11 |
| Identity Providers | 15 |
| Keys | 2 |
| Organizations | 13 |
| Protocol Mappers | 14 |
| Realms Admin | 37 |
| Roles | 28 |
| Roles by ID | 10 |
| Scope Mappings | 29 |
| Users | 30 |
| **Total** | **299** |

## Installation

```bash
pip install -e .
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install -e .
```

## Configuration

Set environment variables (or create a `.env` file based on `.env.example`):

```bash
# Required
export KEYCLOAK_URL=http://localhost:8080

# Authentication - Option A: Password flow
export KEYCLOAK_ADMIN_USERNAME=admin
export KEYCLOAK_ADMIN_PASSWORD=admin

# Authentication - Option B: Client credentials flow
export KEYCLOAK_CLIENT_ID=my-client
export KEYCLOAK_CLIENT_SECRET=my-secret

# Optional
export KEYCLOAK_ADMIN_REALM=master    # default: master
export KEYCLOAK_VERIFY_SSL=true       # default: true
```

## Usage

### Claude Code (stdio)

Add to your Claude Code MCP configuration (`~/.claude/claude_desktop_config.json` or project-level):

```json
{
  "mcpServers": {
    "keycloak": {
      "command": "python",
      "args": ["-m", "keycloak_mcp_server"],
      "env": {
        "KEYCLOAK_URL": "http://localhost:8080",
        "KEYCLOAK_ADMIN_USERNAME": "admin",
        "KEYCLOAK_ADMIN_PASSWORD": "admin"
      }
    }
  }
}
```

Or if installed with uv:

```json
{
  "mcpServers": {
    "keycloak": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/keycloak-mcp-server", "python", "-m", "keycloak_mcp_server"],
      "env": {
        "KEYCLOAK_URL": "http://localhost:8080",
        "KEYCLOAK_ADMIN_USERNAME": "admin",
        "KEYCLOAK_ADMIN_PASSWORD": "admin"
      }
    }
  }
}
```

### GitHub Copilot (SSE)

Start the server with SSE transport:

```bash
python -m keycloak_mcp_server --transport sse --port 8080
```

Then configure in your GitHub Copilot MCP settings (VS Code `settings.json`):

```json
{
  "github.copilot.chat.mcpServers": {
    "keycloak": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

### Command Line

```bash
# stdio mode (default)
python -m keycloak_mcp_server

# SSE mode
python -m keycloak_mcp_server --transport sse --host 0.0.0.0 --port 8080

# Using the entry point
keycloak-mcp-server --transport sse --port 8080
```

## Examples

Once connected, you can use natural language to interact with Keycloak:

- *"List all realms"* → calls `list_realms`
- *"Create a user called john in the master realm"* → calls `create_user`
- *"Show me all clients in the production realm"* → calls `list_clients`
- *"What roles does user X have?"* → calls `get_user_role_mappings`
- *"Add the admin role to the developers group"* → calls `add_group_realm_role_mappings`

## Project Structure

```
src/keycloak_mcp_server/
├── __init__.py          # Package entry point
├── __main__.py          # CLI entry point
├── config.py            # Environment-based configuration
├── client.py            # Async HTTP client with auto-auth
├── server.py            # MCP server setup and tool registration
└── endpoints/           # Endpoint definitions by category
    ├── __init__.py      # Base classes (EndpointDef, Param)
    ├── attack_detection.py
    ├── authentication.py
    ├── certificates.py
    ├── client_initial_access.py
    ├── client_registration_policy.py
    ├── client_role_mappings.py
    ├── client_scopes.py
    ├── clients.py
    ├── component.py
    ├── groups.py
    ├── identity_providers.py
    ├── key.py
    ├── organizations.py
    ├── protocol_mappers.py
    ├── realms.py
    ├── roles.py
    ├── roles_by_id.py
    ├── scope_mappings.py
    └── users.py
```

## License

MIT
