from . import EndpointDef, Param, REALM

GROUP_ID = Param("group_id", "Group UUID")
USER_ID = Param("user_id", "User UUID")
CLIENT_ID = Param("client_id", "Client UUID")

ENDPOINTS: list[EndpointDef] = [
    # ── Group Client Role Mappings ──────────────────────────────────────
    EndpointDef(
        name="get_available_group_client_roles",
        description="Get available client-level roles that can be mapped to the group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/role-mappings/clients/{client_id}/available",
        path_params=[REALM, GROUP_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_effective_group_client_role_mappings",
        description="Get effective (composite) client-level role mappings for the group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/role-mappings/clients/{client_id}/composite",
        path_params=[REALM, GROUP_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="delete_group_client_role_mappings",
        description="Delete client-level role mappings from the group.",
        method="DELETE",
        path="/admin/realms/{realm}/groups/{group_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, GROUP_ID, CLIENT_ID],
        query_params=[],
        body_param=Param("roles", "List of role representations", param_type="object"),
    ),
    EndpointDef(
        name="get_group_client_role_mappings",
        description="Get client-level role mappings for the group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, GROUP_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_group_client_role_mappings",
        description="Add client-level role mappings to the group.",
        method="POST",
        path="/admin/realms/{realm}/groups/{group_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, GROUP_ID, CLIENT_ID],
        query_params=[],
        body_param=Param("roles", "List of role representations", param_type="object"),
    ),
    # ── User Client Role Mappings ───────────────────────────────────────
    EndpointDef(
        name="get_available_user_client_roles",
        description="Get available client-level roles that can be mapped to the user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/role-mappings/clients/{client_id}/available",
        path_params=[REALM, USER_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_effective_user_client_role_mappings",
        description="Get effective (composite) client-level role mappings for the user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/role-mappings/clients/{client_id}/composite",
        path_params=[REALM, USER_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="delete_user_client_role_mappings",
        description="Delete client-level role mappings from the user.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, USER_ID, CLIENT_ID],
        query_params=[],
        body_param=Param("roles", "List of role representations", param_type="object"),
    ),
    EndpointDef(
        name="get_user_client_role_mappings",
        description="Get client-level role mappings for the user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, USER_ID, CLIENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_user_client_role_mappings",
        description="Add client-level role mappings to the user.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/role-mappings/clients/{client_id}",
        path_params=[REALM, USER_ID, CLIENT_ID],
        query_params=[],
        body_param=Param("roles", "List of role representations", param_type="object"),
    ),
]
