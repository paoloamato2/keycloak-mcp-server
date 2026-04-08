from . import EndpointDef, Param, REALM

GROUP_ID = Param("group_id", "Group ID")

ENDPOINTS: list[EndpointDef] = [
    # ── Groups ───────────────────────────────────────────────────────
    EndpointDef(
        name="list_groups",
        description="List all groups for the realm.",
        method="GET",
        path="/admin/realms/{realm}/groups",
        path_params=[REALM],
        query_params=[
            Param("search", "Search string for group name", required=False),
            Param(
                "exact",
                "If true, search is exact match",
                required=False,
                param_type="boolean",
            ),
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param("max", "Maximum results size", required=False, param_type="integer"),
            Param(
                "briefRepresentation",
                "If true, return brief representation",
                required=False,
                param_type="boolean",
            ),
            Param("q", "Custom query for searching groups", required=False),
            Param(
                "populateHierarchy",
                "If true, populate group hierarchy",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="create_group",
        description="Create a new group in the realm.",
        method="POST",
        path="/admin/realms/{realm}/groups",
        path_params=[REALM],
        query_params=[],
        body_param=Param("group_data", "Group representation", param_type="object"),
    ),
    EndpointDef(
        name="get_group",
        description="Get a group by ID.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_group",
        description="Update a group.",
        method="PUT",
        path="/admin/realms/{realm}/groups/{group_id}",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=Param("group_data", "Group representation", param_type="object"),
    ),
    EndpointDef(
        name="delete_group",
        description="Delete a group.",
        method="DELETE",
        path="/admin/realms/{realm}/groups/{group_id}",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Group Children ───────────────────────────────────────────────
    EndpointDef(
        name="list_group_children",
        description="List children of a group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/children",
        path_params=[REALM, GROUP_ID],
        query_params=[
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param("max", "Maximum results size", required=False, param_type="integer"),
            Param(
                "briefRepresentation",
                "If true, return brief representation",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="create_group_child",
        description="Create a child group under a parent group.",
        method="POST",
        path="/admin/realms/{realm}/groups/{group_id}/children",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=Param("group_data", "Group representation", param_type="object"),
    ),
    # ── Group Members ────────────────────────────────────────────────
    EndpointDef(
        name="list_group_members",
        description="List members of a group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/members",
        path_params=[REALM, GROUP_ID],
        query_params=[
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param("max", "Maximum results size", required=False, param_type="integer"),
            Param(
                "briefRepresentation",
                "If true, return brief representation",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    # ── Group Count ──────────────────────────────────────────────────
    EndpointDef(
        name="count_groups",
        description="Get the number of groups in the realm.",
        method="GET",
        path="/admin/realms/{realm}/groups/count",
        path_params=[REALM],
        query_params=[
            Param("search", "Search string for group name", required=False),
            Param(
                "top",
                "If true, only count top-level groups",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    # ── Group Management Permissions ─────────────────────────────────
    EndpointDef(
        name="get_group_management_permissions",
        description="Get management permissions for a group.",
        method="GET",
        path="/admin/realms/{realm}/groups/{group_id}/management/permissions",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_group_management_permissions",
        description="Update management permissions for a group.",
        method="PUT",
        path="/admin/realms/{realm}/groups/{group_id}/management/permissions",
        path_params=[REALM, GROUP_ID],
        query_params=[],
        body_param=Param(
            "permissions_data",
            "Management permissions representation",
            param_type="object",
        ),
    ),
]
