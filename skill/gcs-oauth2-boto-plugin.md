---
name: gcs-oauth2-boto-plugin
category: programming
description: Auth plugin for boto library enabling OAuth 2.0 credentials for Google Cloud Storage access
tags: [gcs-oauth2-boto-plugin, Google Cloud Storage, OAuth2, boto, authentication, Python, cloud]
author: oxo-call-community
source_url: "https://github.com/GoogleCloudPlatform/gcs-oauth2-boto-plugin"
---

## Concepts

- **Tool Overview**: gcs-oauth2-boto-plugin is an authentication plugin for the boto library that enables OAuth 2.0 credentials to authenticate with Google Cloud Storage (GCS). It is a wrapper around oauth2client with automatic token caching.
- **Core Function**: Provides secure OAuth 2.0 authentication for boto-based tools (like gsutil) accessing Google Cloud Storage resources. Supports both user accounts and service accounts.
- **Authentication Types**: Supports OAuth 2.0 User Account credentials (for individual user access) and OAuth 2.0 Service Account credentials (for automated/server applications).
- **Token Caching**: Automatically caches refresh tokens in a thread-safe and process-safe manner, eliminating repeated OAuth authorization prompts.
- **Compatibility**: Works with boto auth plugin framework. Essential for gsutil when configured for OAuth 2.0 authentication. Compatible with Python 2.7 and Python 3.4+.
- **Installation**: `pip install gcs-oauth2-boto-plugin` or `conda install -c bioconda gcs-oauth2-boto-plugin`. Requires boto and oauth2client.
- **Configuration**: Authentication is configured via boto configuration file (~/.boto). Use `gsutil config` to generate configuration automatically, or manually add credentials.
- **OAuth2 Flow**: The plugin handles the full OAuth 2.0 flow including token refresh, automatic retry on 401 errors, and credential validation.

## Pitfalls

- **Inactive development**: The project has development status "7 - Inactive" according to PyPI. Consider using google-auth-library instead for new projects.
- **boto vs boto3**: This plugin works with legacy boto library, not boto3. For new Google Cloud projects, use google-cloud-storage Python client with google-auth instead.
- **Python 2 deprecation**: While the package claims Python 2.7 support, Python 2 is deprecated. Use Python 3.x for new deployments.
- **Credential security**: Refresh tokens stored in cache have filesystem permissions. Ensure ~/.boto and cache directory are properly protected (chmod 600).
- **Token expiration**: OAuth refresh tokens expire after a period (typically 1 hour of access token validity, refresh tokens can last weeks). The plugin handles refresh automatically but requires network connectivity.
- **Multiple credentials**: When using JSON API (default), only one set of OAuth2 credentials can be configured per boto config file.
- **Service account permissions**: Service accounts have "Editor" role by default, not "Owner". This affects canned ACL behavior. Add service account email as project Owner for full control.
- **gsutil dependency**: This plugin is primarily used by gsutil. Installing gsutil automatically includes this plugin.

## Examples

### Configure gsutil with OAuth2
**Args:** `gsutil config -e`
**Explanation:** The `-e` flag configures gsutil to use OAuth 2.0 service account credentials. Prompts for the path to the service account private key JSON file. This automatically installs gcs-oauth2-boto-plugin and configures boto authentication.

### Configure gsutil with user account
**Args:** `gsutil config`
**Explanation:** Running config without flags sets up OAuth 2.0 for a user account. Opens browser for Google authentication and stores credentials in ~/.boto. Suitable for personal workstation configuration.

### Using boto config file manually
**Args:** `[Credentials] gs_service_key_file = /path/to/key.json [OAuth2] provider_authorization_url = https://accounts.google.com/o/oauth2/auth provider_token_uri = https://oauth2.googleapis.com/token`
**Explanation:** Manual boto configuration for OAuth2 service account authentication. The gs_service_key_file points to the JSON key downloaded from Google Cloud Console. The plugin reads these sections to authenticate.

### Verify authentication
**Args:** `gsutil ls gs://bucket-name/`
**Explanation:** Lists objects in a GCS bucket to verify OAuth2 authentication is working. If authentication fails, gsutil returns an error. Token refresh happens automatically on 401 responses.

### Upload file with OAuth2
**Args:** `gsutil cp localfile.txt gs://bucket-name/remote/path/`
**Explanation:** Copies a local file to GCS using OAuth2 authentication. The plugin handles authentication header management and token refresh as needed during the multipart upload process.

### Set default project
**Args:** `gsutil config set project my-project-id`
**Explanation:** Configures the default Google Cloud project for gsutil operations. This is stored in the boto config file and used for all subsequent gsutil commands.

### Refresh credentials
**Args:** `gcloud auth application-default login`
**Explanation:** For Google Cloud SDK integration, use gcloud to refresh Application Default Credentials. These credentials are then available to boto-based tools through the plugin.

### Check plugin version
**Args:** `pip show gcs-oauth2-boto-plugin`
**Explanation:** Displays the installed version of the OAuth2 plugin. Version information is useful when troubleshooting authentication issues or verifying installation.

### HMAC vs OAuth2
**Args:** `gsutil config -a`
**Explanation:** The `-a` flag configures HMAC authentication instead of OAuth2. HMAC uses access key and secret key similar to AWS S3. OAuth2 is preferred for Google Cloud due to better security and automatic token management.
