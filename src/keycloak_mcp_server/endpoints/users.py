from . import EndpointDef, Param, REALM

USER_ID = Param("user_id", "User ID")
CREDENTIAL_ID = Param("credential_id", "Credential ID")
AFTER_CREDENTIAL_ID = Param("after_credential_id", "Credential ID to position after")
CLIENT_ID_PATH = Param("client_id", "Client ID")
PROVIDER = Param("provider", "Identity provider alias")
GROUP_ID = Param("group_id", "Group ID")
CLIENT_UUID = Param("client_uuid", "Client UUID")

ENDPOINTS: list[EndpointDef] = [
    # ── Users ───────────────────────────────────────────────────────────
    EndpointDef(
        name="list_users",
        description="List users in the realm, with optional filtering.",
        method="GET",
        path="/admin/realms/{realm}/users",
        path_params=[REALM],
        query_params=[
            Param("search", "Search string for users", required=False),
            Param("email", "Email filter", required=False),
            Param(
                "emailVerified",
                "Email verified filter",
                required=False,
                param_type="boolean",
            ),
            Param("enabled", "Enabled filter", required=False, param_type="boolean"),
            Param(
                "exact",
                "If true, search is exact match",
                required=False,
                param_type="boolean",
            ),
            Param("first", "Pagination offset", required=False, param_type="integer"),
            Param("firstName", "First name filter", required=False),
            Param("idpAlias", "Identity provider alias filter", required=False),
            Param("idpUserId", "Identity provider user ID filter", required=False),
            Param("lastName", "Last name filter", required=False),
            Param("max", "Maximum results size", required=False, param_type="integer"),
            Param("q", "Custom query for searching users", required=False),
            Param("username", "Username filter", required=False),
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
        name="create_user",
        description="Create a new user in the realm.",
        method="POST",
        path="/admin/realms/{realm}/users",
        path_params=[REALM],
        query_params=[],
        body_param=Param("user_data", "User representation", param_type="object"),
    ),
    EndpointDef(
        name="get_user",
        description="Get a user by ID.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}",
        path_params=[REALM, USER_ID],
        query_params=[
            Param(
                "userProfileMetadata",
                "Include user profile metadata",
                required=False,
                param_type="boolean",
            ),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="update_user",
        description="Update a user.",
        method="PUT",
        path="/admin/realms/{realm}/users/{user_id}",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=Param("user_data", "User representation", param_type="object"),
    ),
    EndpointDef(
        name="delete_user",
        description="Delete a user.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── User Count ──────────────────────────────────────────────────────
    EndpointDef(
        name="count_users",
        description="Get the number of users in the realm matching the given criteria.",
        method="GET",
        path="/admin/realms/{realm}/users/count",
        path_params=[REALM],
        query_params=[
            Param("search", "Search string for users", required=False),
            Param("email", "Email filter", required=False),
            Param(
                "emailVerified",
                "Email verified filter",
                required=False,
                param_type="boolean",
            ),
            Param("enabled", "Enabled filter", required=False, param_type="boolean"),
            Param("firstName", "First name filter", required=False),
            Param("lastName", "Last name filter", required=False),
            Param("username", "Username filter", required=False),
        ],
        body_param=None,
    ),
    # ── User Profile ────────────────────────────────────────────────────
    EndpointDef(
        name="get_user_profile",
        description="Get the user profile configuration for the realm.",
        method="GET",
        path="/admin/realms/{realm}/users/profile",
        path_params=[REALM],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_user_profile",
        description="Update the user profile configuration for the realm.",
        method="PUT",
        path="/admin/realms/{realm}/users/profile",
        path_params=[REALM],
        query_params=[],
        body_param=Param(
            "profile_data",
            "User profile configuration representation",
            param_type="object",
        ),
    ),
    # ── User Credentials ────────────────────────────────────────────────
    EndpointDef(
        name="list_user_credentials",
        description="List credentials for a user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/credentials",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="delete_user_credential",
        description="Delete a credential for a user.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}/credentials/{credential_id}",
        path_params=[REALM, USER_ID, CREDENTIAL_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="update_user_credential_label",
        description="Update the label of a user credential.",
        method="PUT",
        path="/admin/realms/{realm}/users/{user_id}/credentials/{credential_id}/userLabel",
        path_params=[REALM, USER_ID, CREDENTIAL_ID],
        query_params=[],
        body_param=Param("label_data", "Credential label data", param_type="object"),
    ),
    EndpointDef(
        name="move_user_credential_to_first",
        description="Move a user credential to the first position.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/credentials/{credential_id}/moveToFirst",
        path_params=[REALM, USER_ID, CREDENTIAL_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="move_user_credential_after",
        description="Move a user credential after another credential.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/credentials/{credential_id}/moveAfter/{after_credential_id}",
        path_params=[REALM, USER_ID, CREDENTIAL_ID, AFTER_CREDENTIAL_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Reset Password ──────────────────────────────────────────────────
    EndpointDef(
        name="reset_user_password",
        description="Reset a user's password.",
        method="PUT",
        path="/admin/realms/{realm}/users/{user_id}/reset-password",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=Param(
            "credential_data",
            "Credential representation (password)",
            param_type="object",
        ),
    ),
    # ── Execute Actions Email ───────────────────────────────────────────
    EndpointDef(
        name="send_user_actions_email",
        description="Send required actions email to a user.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/execute-actions-email",
        path_params=[REALM, USER_ID],
        query_params=[
            Param(
                "lifespan",
                "Lifespan in seconds for the action token",
                required=False,
                param_type="integer",
            ),
            Param(
                "redirect_uri",
                "Redirect URI after actions are completed",
                required=False,
            ),
            Param("client_id", "Client ID for the redirect", required=False),
        ],
        body_param=Param(
            "actions_data", "List of required actions", param_type="object"
        ),
    ),
    # ── User Consents ───────────────────────────────────────────────────
    EndpointDef(
        name="list_user_consents",
        description="List consents granted by a user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/consents",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="revoke_user_consent",
        description="Revoke consent and offline tokens for a particular client from a user.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}/consents/{client_id}",
        path_params=[REALM, USER_ID, CLIENT_ID_PATH],
        query_params=[],
        body_param=None,
    ),
    # ── Disable Credential Types ────────────────────────────────────────
    EndpointDef(
        name="disable_user_credential_types",
        description="Disable credential types for a user.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/disable-credential-types",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=Param(
            "credential_types",
            "List of credential types to disable",
            param_type="object",
        ),
    ),
    # ── Federated Identity ──────────────────────────────────────────────
    EndpointDef(
        name="list_user_federated_identities",
        description="List federated identities for a user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/federated-identity",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="add_user_federated_identity",
        description="Add a federated identity to a user.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/federated-identity/{provider}",
        path_params=[REALM, USER_ID, PROVIDER],
        query_params=[],
        body_param=Param(
            "identity_data", "Federated identity representation", param_type="object"
        ),
    ),
    EndpointDef(
        name="remove_user_federated_identity",
        description="Remove a federated identity from a user.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}/federated-identity/{provider}",
        path_params=[REALM, USER_ID, PROVIDER],
        query_params=[],
        body_param=None,
    ),
    # ── User Groups ─────────────────────────────────────────────────────
    EndpointDef(
        name="list_user_groups",
        description="List groups that a user belongs to.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/groups",
        path_params=[REALM, USER_ID],
        query_params=[
            Param("search", "Search string for group name", required=False),
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
        name="count_user_groups",
        description="Get the number of groups a user belongs to.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/groups/count",
        path_params=[REALM, USER_ID],
        query_params=[
            Param("search", "Search string for group name", required=False),
        ],
        body_param=None,
    ),
    EndpointDef(
        name="add_user_to_group",
        description="Add a user to a group.",
        method="PUT",
        path="/admin/realms/{realm}/users/{user_id}/groups/{group_id}",
        path_params=[REALM, USER_ID, GROUP_ID],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="remove_user_from_group",
        description="Remove a user from a group.",
        method="DELETE",
        path="/admin/realms/{realm}/users/{user_id}/groups/{group_id}",
        path_params=[REALM, USER_ID, GROUP_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Impersonation ───────────────────────────────────────────────────
    EndpointDef(
        name="impersonate_user",
        description="Impersonate a user.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/impersonation",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Logout ──────────────────────────────────────────────────────────
    EndpointDef(
        name="logout_user",
        description="Log out a user by revoking all sessions.",
        method="POST",
        path="/admin/realms/{realm}/users/{user_id}/logout",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Offline Sessions ────────────────────────────────────────────────
    EndpointDef(
        name="list_user_offline_sessions",
        description="List offline sessions for a user and client.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/offline-sessions/{client_uuid}",
        path_params=[REALM, USER_ID, CLIENT_UUID],
        query_params=[],
        body_param=None,
    ),
    # ── Sessions ────────────────────────────────────────────────────────
    EndpointDef(
        name="list_user_sessions",
        description="List sessions for a user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/sessions",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
    # ── Configured User Storage Credential Types ────────────────────────
    EndpointDef(
        name="list_user_configured_credential_types",
        description="List configured user storage credential types for a user.",
        method="GET",
        path="/admin/realms/{realm}/users/{user_id}/configured-user-storage-credential-types",
        path_params=[REALM, USER_ID],
        query_params=[],
        body_param=None,
    ),
]
