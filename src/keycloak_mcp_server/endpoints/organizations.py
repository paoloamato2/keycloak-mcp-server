from . import EndpointDef, Param, REALM

ORG_ID = Param("org_id", "Organization ID")
USER_ID = Param("user_id", "User ID")
ALIAS = Param("alias", "Identity provider alias")

ENDPOINTS: list[EndpointDef] = [
    # ── Organizations ───────────────────────────────────────────────
    EndpointDef(
        name="list_organizations",
        description="List organizations for the realm, optionally filtered by search criteria.",
        method="GET",
        path="/admin/realms/{realm}/organizations",
        path_params=[REALM],
        query_params=[
            Param("search", "Search string filter", required=False),
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param(
                "max", "Maximum results to return", required=False, param_type="integer"
            ),
            Param(
                "exact", "Exact match for search", required=False, param_type="boolean"
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="create_organization",
        description="Create a new organization.",
        method="POST",
        path="/admin/realms/{realm}/organizations",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "org_data", "Organization representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_organization",
        description="Get an organization by ID.",
        method="GET",
        path="/admin/realms/{realm}/organizations/{org_id}",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_organization",
        description="Update an organization.",
        method="PUT",
        path="/admin/realms/{realm}/organizations/{org_id}",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=Param(
            "org_data", "Organization representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_organization",
        description="Delete an organization.",
        method="DELETE",
        path="/admin/realms/{realm}/organizations/{org_id}",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Organization Members ────────────────────────────────────────
    EndpointDef(
        name="list_organization_members",
        description="List members of an organization.",
        method="GET",
        path="/admin/realms/{realm}/organizations/{org_id}/members",
        path_params=[REALM, ORG_ID],
        query_params=[
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param(
                "max", "Maximum results to return", required=False, param_type="integer"
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="add_organization_member",
        description="Add a member to an organization.",
        method="POST",
        path="/admin/realms/{realm}/organizations/{org_id}/members",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=Param("member_data", "Member representation", param_type="object"),
    ),
    EndpointDef(
        name="get_organization_member",
        description="Get a specific member of an organization.",
        method="GET",
        path="/admin/realms/{realm}/organizations/{org_id}/members/{user_id}",
        path_params=[REALM, ORG_ID, USER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="remove_organization_member",
        description="Remove a member from an organization.",
        method="DELETE",
        path="/admin/realms/{realm}/organizations/{org_id}/members/{user_id}",
        path_params=[REALM, ORG_ID, USER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Organization Identity Providers ─────────────────────────────
    EndpointDef(
        name="list_organization_identity_providers",
        description="List identity providers linked to an organization.",
        method="GET",
        path="/admin/realms/{realm}/organizations/{org_id}/identity-providers",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="link_organization_identity_provider",
        description="Link an identity provider to an organization.",
        method="POST",
        path="/admin/realms/{realm}/organizations/{org_id}/identity-providers",
        path_params=[REALM, ORG_ID],
        query_params=[],
        body_param=Param(
            "idp_data", "Identity provider link representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_organization_identity_provider",
        description="Get an identity provider linked to an organization by alias.",
        method="GET",
        path="/admin/realms/{realm}/organizations/{org_id}/identity-providers/{alias}",
        path_params=[REALM, ORG_ID, ALIAS],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="unlink_organization_identity_provider",
        description="Unlink an identity provider from an organization.",
        method="DELETE",
        path="/admin/realms/{realm}/organizations/{org_id}/identity-providers/{alias}",
        path_params=[REALM, ORG_ID, ALIAS],
        query_params=[],
        body_param=None,
    ),
]
