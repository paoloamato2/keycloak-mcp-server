from . import EndpointDef, Param, REALM

ALIAS = Param("alias", "Identity provider alias")
MAPPER_ID = Param("mapper_id", "Mapper ID")
PROVIDER_ID = Param("provider_id", "Provider ID")

ENDPOINTS: list[EndpointDef] = [
    # ── Identity Provider Instances ──────────────────────────────────────
    EndpointDef(
        name="list_identity_providers",
        description="List all identity providers for the realm.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances",
        path_params=[REALM],
        query_params=[
            Param("search", "Search filter", required=False),
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param("max", "Maximum results size", required=False, param_type="integer"),
            Param(
                "briefRepresentation",
                "If true, return only basic information",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="create_identity_provider",
        description="Create a new identity provider.",
        method="POST",
        path="/admin/realms/{realm}/identity-provider/instances",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "provider_data", "Identity provider representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_identity_provider",
        description="Get an identity provider by alias.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_identity_provider",
        description="Update an identity provider.",
        method="PUT",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=Param(
            "provider_data", "Identity provider representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_identity_provider",
        description="Delete an identity provider by alias.",
        method="DELETE",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    # ── Identity Provider Export ─────────────────────────────────────────
    EndpointDef(
        name="export_identity_provider_broker_config",
        description="Export the broker configuration for an identity provider.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/export",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    # ── Identity Provider Permissions ────────────────────────────────────
    EndpointDef(
        name="get_identity_provider_permissions",
        description="Get the management permissions for an identity provider.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/management/permissions",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_identity_provider_permissions",
        description="Update the management permissions for an identity provider.",
        method="PUT",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/management/permissions",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=Param(
            "permissions_data",
            "Management permissions representation",
            param_type="object",
        ),
    ),
    # ── Identity Provider Mappers ────────────────────────────────────────
    EndpointDef(
        name="list_identity_provider_mappers",
        description="List all mappers for an identity provider.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mappers",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_identity_provider_mapper",
        description="Create a new mapper for an identity provider.",
        method="POST",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mappers",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=Param(
            "mapper_data",
            "Identity provider mapper representation",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="get_identity_provider_mapper",
        description="Get a mapper for an identity provider by mapper ID.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{mapper_id}",
        path_params=[REALM, ALIAS, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_identity_provider_mapper",
        description="Update a mapper for an identity provider.",
        method="PUT",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{mapper_id}",
        path_params=[REALM, ALIAS, MAPPER_ID],
        query_params=[],
        body_param=Param(
            "mapper_data",
            "Identity provider mapper representation",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="delete_identity_provider_mapper",
        description="Delete a mapper for an identity provider.",
        method="DELETE",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mappers/{mapper_id}",
        path_params=[REALM, ALIAS, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Identity Provider Mapper Types ───────────────────────────────────
    EndpointDef(
        name="list_identity_provider_mapper_types",
        description="List available mapper types for an identity provider.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/instances/{alias}/mapper-types",
        path_params=[REALM, ALIAS],
        query_params=[],
        body_param=None,
    ),
    # ── Identity Provider by Provider ID ─────────────────────────────────
    EndpointDef(
        name="get_identity_provider_by_provider_id",
        description="Get an identity provider by provider ID.",
        method="GET",
        path="/admin/realms/{realm}/identity-provider/providers/{provider_id}",
        path_params=[REALM, PROVIDER_ID],
        query_params=[],
        body_param=None,
    ),
]
