from . import EndpointDef, Param, REALM

CLIENT_UUID = Param("client_uuid", "Client UUID")
ATTR = Param("attr", "Certificate attribute name")

ENDPOINTS: list[EndpointDef] = [
    EndpointDef(
        name="download_client_keystore",
        description="Download the keystore file for a client certificate, using the provided keystore configuration.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}/download",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=Param("config", "Keystore configuration", param_type="object"),
    ),
    EndpointDef(
        name="generate_and_download_client_keypair",
        description="Generate a new keypair and certificate for the client, and download the resulting keystore.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}/generate-and-download",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=Param("config", "Keystore configuration", param_type="object"),
    ),
    EndpointDef(
        name="generate_client_certificate",
        description="Generate a new certificate and keypair for a client attribute.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}/generate",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="get_client_key_info",
        description="Get key information for a client certificate attribute, including certificate and key metadata.",
        method="GET",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=None,
    ),
    EndpointDef(
        name="upload_client_certificate_only",
        description="Upload only a certificate for a client attribute, without updating the private key.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}/upload-certificate",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=Param("certificate", "Certificate to upload", param_type="object"),
    ),
    EndpointDef(
        name="upload_client_certificate_and_key",
        description="Upload a certificate and its private key for a client attribute.",
        method="POST",
        path="/admin/realms/{realm}/clients/{client_uuid}/certificates/{attr}/upload",
        path_params=[REALM, CLIENT_UUID, ATTR],
        query_params=[],
        body_param=Param(
            "keystore", "Certificate and key to upload", param_type="object"
        ),
    ),
]
