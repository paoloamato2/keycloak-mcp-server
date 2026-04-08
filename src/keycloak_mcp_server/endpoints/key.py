from . import EndpointDef, Param, REALM

ENDPOINTS: list[EndpointDef] = [
    EndpointDef(
        name="get_realm_keys",
        description="Get the keys for the realm, including active and passive keys and their details.",
        method="GET",
        path="/admin/realms/{realm}/keys",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_active_realm_key",
        description="Get the active key for the realm by key type.",
        method="GET",
        path="/admin/realms/{realm}/keys/active/{kty}",
        path_params=[REALM, Param("kty", "Key type (e.g. RSA, EC)")],
        query_params=[],
        body_param=None,
    ),
]
