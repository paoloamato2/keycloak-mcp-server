import asyncio, mcp.types as t
from keycloak_mcp_server.server import create_server


async def main():
    s, c = create_server()
    handler = s.request_handlers[t.CallToolRequest]
    req = t.CallToolRequest(
        method="tools/call",
        params=t.CallToolRequestParams(name="list_realms", arguments={}),
    )
    res = await handler(req)
    print(type(res))
    print(dir(res))


asyncio.run(main())
