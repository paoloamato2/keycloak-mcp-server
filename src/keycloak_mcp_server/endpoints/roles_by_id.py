from . import EndpointDef, Param, REALM

ROLE_ID = Param("role_id", "Role ID")
CLIENT_UUID = Param("client_uuid", "Client UUID")

ENDPOINTS: list[EndpointDef] = [
    # ── Roles by ID CRUD ────────────────────────────────────────────────
    EndpointDef(
        name="get_role_by_id",
        description="Get a role by ID.",
        method="GET",
        path="/admin/realms/{realm}/roles-by-id/{role_id}",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_role_by_id",
        description="Update a role by ID.",
        method="PUT",
        path="/admin/realms/{realm}/roles-by-id/{role_id}",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=Param("role_data", "Role representation", param_type="object"),
    ),
    EndpointDef(
        name="delete_role_by_id",
        description="Delete a role by ID.",
        method="DELETE",
        path="/admin/realms/{realm}/roles-by-id/{role_id}",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Role by ID Composites ───────────────────────────────────────────
    EndpointDef(
        name="get_role_by_id_composites",
        description="Get composites of a role by ID.",
        method="GET",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/composites",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_role_by_id_composites",
        description="Add composites to a role by ID.",
        method="POST",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/composites",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=Param(
            "roles",
            "List of role representations to add as composites",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="remove_role_by_id_composites",
        description="Remove composites from a role by ID.",
        method="DELETE",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/composites",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=Param(
            "roles",
            "List of role representations to remove from composites",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="get_role_by_id_realm_composites",
        description="Get realm-level composites of a role by ID.",
        method="GET",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/composites/realm",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_role_by_id_client_composites",
        description="Get client-level composites of a role by ID for a specific client.",
        method="GET",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/composites/clients/{client_uuid}",
        path_params=[REALM, ROLE_ID, CLIENT_UUID],
        query_params=[],
        body_param=None,
    ),
    # ── Role by ID Management Permissions ───────────────────────────────
    EndpointDef(
        name="get_role_by_id_permissions",
        description="Get management permissions for a role by ID.",
        method="GET",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/management/permissions",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_role_by_id_permissions",
        description="Update management permissions for a role by ID.",
        method="PUT",
        path="/admin/realms/{realm}/roles-by-id/{role_id}/management/permissions",
        path_params=[REALM, ROLE_ID],
        query_params=[],
        body_param=Param(
            "permissions_data",
            "Management permissions representation",
            param_type="object",
        ),
    ),
]
