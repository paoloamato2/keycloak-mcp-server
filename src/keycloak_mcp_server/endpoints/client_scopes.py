from . import EndpointDef, Param, REALM

CLIENT_SCOPE_ID = Param("client_scope_id", "Client scope ID")

ENDPOINTS: list[EndpointDef] = [
    # ── Client Scopes ────────────────────────────────────────────────
    EndpointDef(
        name="list_client_scopes",
        description="List all client scopes for the realm.",
        method="GET",
        path="/admin/realms/{realm}/client-scopes",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_client_scope",
        description="Create a new client scope.",
        method="POST",
        path="/admin/realms/{realm}/client-scopes",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "scope_data", "Client scope representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_client_scope",
        description="Get a client scope by ID.",
        method="GET",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_client_scope",
        description="Update a client scope.",
        method="PUT",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=Param(
            "scope_data", "Client scope representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_client_scope",
        description="Delete a client scope.",
        method="DELETE",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Client Templates (legacy) ────────────────────────────────────
    EndpointDef(
        name="list_client_templates",
        description="List all client templates for the realm (legacy).",
        method="GET",
        path="/admin/realms/{realm}/client-templates",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_client_template",
        description="Create a new client template (legacy).",
        method="POST",
        path="/admin/realms/{realm}/client-templates",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "template_data", "Client template representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_client_template",
        description="Get a client template by ID (legacy).",
        method="GET",
        path="/admin/realms/{realm}/client-templates/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_client_template",
        description="Update a client template (legacy).",
        method="PUT",
        path="/admin/realms/{realm}/client-templates/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=Param(
            "template_data", "Client template representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_client_template",
        description="Delete a client template (legacy).",
        method="DELETE",
        path="/admin/realms/{realm}/client-templates/{client_scope_id}",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=None,
    ),
]
