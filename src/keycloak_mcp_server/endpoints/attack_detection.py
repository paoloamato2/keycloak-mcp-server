from . import EndpointDef, Param, REALM

USER_ID = Param("user_id", "ID of the user")

ENDPOINTS: list[EndpointDef] = [
    EndpointDef(
        name="clear_all_brute_force_failures",
        description="Clear all user login failures for the realm, allowing all users to attempt login again.",
        method="DELETE",
        path="/admin/realms/{realm}/attack-detection/brute-force/users",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="clear_user_brute_force_failures",
        description="Clear login failures for a specific user, allowing them to attempt login again.",
        method="DELETE",
        path="/admin/realms/{realm}/attack-detection/brute-force/users/{user_id}",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_user_brute_force_status",
        description="Get the brute force detection status for a specific user, including number of failures and disabled state.",
        method="GET",
        path="/admin/realms/{realm}/attack-detection/brute-force/users/{user_id}",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
]
