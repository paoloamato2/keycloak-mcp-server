from . import EndpointDef, REALM

ENDPOINTS: list[EndpointDef] = [
    EndpointDef(
        name="list_client_registration_policy_providers",
        description="List all client registration policy providers for the realm.",
        method="GET",
        path="/admin/realms/{realm}/client-registration-policy/providers",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
]
