from . import EndpointDef, Param, REALM

ID = Param("id", "ID of the initial access token")

ENDPOINTS: list[EndpointDef] = [
    EndpointDef(
        name="list_client_initial_access_tokens",
        description="List all client initial access tokens for the realm.",
        method="GET",
        path="/admin/realms/{realm}/clients-initial-access",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="delete_client_initial_access_token",
        description="Delete a client initial access token.",
        method="DELETE",
        path="/admin/realms/{realm}/clients-initial-access/{id}",
        path_params=[REALM, ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_client_initial_access_token",
        description="Create a new client initial access token.",
        method="POST",
        path="/admin/realms/{realm}/clients-initial-access",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "token_config", "Initial access token configuration", param_type="object"
        ),
    ),
]
