from . import EndpointDef, Param, REALM

CLIENT_SCOPE_ID = Param("client_scope_id", "Client scope ID")
CLIENT_UUID = Param("client_uuid", "Client UUID")
MAPPER_ID = Param("mapper_id", "Protocol mapper ID")
PROTOCOL = Param("protocol", "Protocol name (e.g. openid-connect, saml)")

ENDPOINTS: list[EndpointDef] = [
    # ── Client Scope Protocol Mappers ──────────────────────────────────
    EndpointDef(
        name="list_client_scope_protocol_mappers",
        description="List all protocol mappers for a client scope.",
        method="GET",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/models",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_client_scope_protocol_mapper",
        description="Create a protocol mapper for a client scope.",
        method="POST",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/models",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=Param(
            "mapper_data", "Protocol mapper representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_client_scope_protocol_mapper",
        description="Get a protocol mapper for a client scope by ID.",
        method="GET",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_SCOPE_ID, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_client_scope_protocol_mapper",
        description="Update a protocol mapper for a client scope.",
        method="PUT",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_SCOPE_ID, MAPPER_ID],
        query_params=[],
        body_param=Param(
            "mapper_data", "Protocol mapper representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_client_scope_protocol_mapper",
        description="Delete a protocol mapper from a client scope.",
        method="DELETE",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_SCOPE_ID, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_client_scope_protocol_mappers_batch",
        description="Add multiple protocol mappers to a client scope in batch.",
        method="POST",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/add-models",
        path_params=[REALM, CLIENT_SCOPE_ID],
        query_params=[],
        body_param=Param(
            "mappers_data",
            "List of protocol mapper representations",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="list_client_scope_mappers_by_protocol",
        description="List protocol mappers for a client scope filtered by protocol.",
        method="GET",
        path="/admin/realms/{realm}/client-scopes/{client_scope_id}/protocol-mappers/protocol/{protocol}",
        path_params=[REALM, CLIENT_SCOPE_ID, PROTOCOL],
        query_params=[],
        body_param=None,
    ),
    # ── Client Protocol Mappers ────────────────────────────────────────
    EndpointDef(
        name="list_client_protocol_mappers",
        description="List all protocol mappers for a client.",
        method="GET",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/models",
        path_params=[REALM, CLIENT_UUID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="create_client_protocol_mapper",
        description="Create a protocol mapper for a client.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/models",
        path_params=[REALM, CLIENT_UUID],
        query_params=[],
        body_param=Param(
            "mapper_data", "Protocol mapper representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_client_protocol_mapper",
        description="Get a protocol mapper for a client by ID.",
        method="GET",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_UUID, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_client_protocol_mapper",
        description="Update a protocol mapper for a client.",
        method="PUT",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_UUID, MAPPER_ID],
        query_params=[],
        body_param=Param(
            "mapper_data", "Protocol mapper representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_client_protocol_mapper",
        description="Delete a protocol mapper from a client.",
        method="DELETE",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/models/{mapper_id}",
        path_params=[REALM, CLIENT_UUID, MAPPER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_client_protocol_mappers_batch",
        description="Add multiple protocol mappers to a client in batch.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/add-models",
        path_params=[REALM, CLIENT_UUID],
        query_params=[],
        body_param=Param(
            "mappers_data",
            "List of protocol mapper representations",
            param_type="object",
        ),
    ),
    EndpointDef(
        name="list_client_mappers_by_protocol",
        description="List protocol mappers for a client filtered by protocol.",
        method="GET",
        path="/admin/realms/{realm}/clients/{client_uuid}/protocol-mappers/protocol/{protocol}",
        path_params=[REALM, CLIENT_UUID, PROTOCOL],
        query_params=[],
        body_param=None,
    ),
]
