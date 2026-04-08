from . import EndpointDef, Param, REALM

COMPONENT_ID = Param("component_id", "Component ID")

ENDPOINTS: list[EndpointDef] = [
    # ── Components ───────────────────────────────────────────────────
    EndpointDef(
        name="list_components",
        description="List all components for the realm, optionally filtered by name, parent, or type.",
        method="GET",
        path="/admin/realms/{realm}/components",
        path_params=[REALM],
        query_params=[
            Param("name", "Component name filter", required=False),
            Param("parent", "Parent component ID filter", required=False),
            Param("type", "Component type filter", required=False),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="create_component",
        description="Create a new component.",
        method="POST",
        path="/admin/realms/{realm}/components",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "component_data", "Component representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="get_component",
        description="Get a component by ID.",
        method="GET",
        path="/admin/realms/{realm}/components/{component_id}",
        path_params=[REALM, COMPONENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_component",
        description="Update a component.",
        method="PUT",
        path="/admin/realms/{realm}/components/{component_id}",
        path_params=[REALM, COMPONENT_ID],
        query_params=[],
        body_param=Param(
            "component_data", "Component representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="delete_component",
        description="Delete a component.",
        method="DELETE",
        path="/admin/realms/{realm}/components/{component_id}",
        path_params=[REALM, COMPONENT_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="list_sub_component_types",
        description="List sub-component types available for a component.",
        method="GET",
        path="/admin/realms/{realm}/components/{component_id}/sub-component-types",
        path_params=[REALM, COMPONENT_ID],
        query_params=[
            Param("type", "Component type filter", required=False),
        ],
        body_param=None,
    ),
]
