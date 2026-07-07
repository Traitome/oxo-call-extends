---
name: arvados-python-client
category: programming
description: Arvados Python SDK - Python client library for Arvados platform
tags: [arvados-python-client, programming, python, arvados, api, data-management]
author: oxo-call-community
source_url: "https://github.com/curoverse/arvados/tree/main/sdk/python"
---

## Concepts

- **Tool Overview**: Arvados Python SDK is a Python client library for accessing Arvados platform APIs for biomedical data management. Version 3.2.1.
- **Core Function**: Provides Python interface to Arvados platform for data storage, workflow execution, and resource management.
- **API Access**: Wraps Arvados REST API with Python objects and methods for easier integration.
- **Data Collections**: Manages Arvados collections and Keep storage through Python code.
- **Workflow Management**: Submits and monitors CWL workflows programmatically.
- **Authentication**: Handles API authentication and session management automatically.
- **Python Integration**: Designed for Python scripts and applications requiring Arvados access.
- **Installation**: `conda install -c bioconda arvados-python-client` or `pip install arvados-python-client`.

## Pitfalls

- **API Version**: SDK version must match Arvados server version. Mismatched versions cause compatibility issues.
- **Authentication**: Requires valid API token and endpoint. Incorrect credentials prevent API access.
- **Network Dependency**: Requires network connection to Arvados server. Network failures affect all operations.
- **Rate Limiting**: API calls may be rate limited. Implement proper error handling and retries.
- **Large Data**: Uploading large datasets requires careful memory management. Use streaming for large files.
- **Python Version**: Requires Python 3.6+. Some features may need newer Python versions.

## Examples

### Initialize Arvados client
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='your_token')"`
**Explanation:** Creates Arvados API client with endpoint and authentication token.

### List collections
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); print(api.collections().list())"`
**Explanation:** Retrieves list of all collections in current Arvados project.

### Upload file to Keep
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); api.collections().create(name='my_collection', manifest_text='. d41d8cd98f00b204e9800998ecf8427e')"`
**Explanation:** Creates new collection in Arvados Keep storage.

### Submit workflow
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); api.container_requests().create(container_request={'command': ['workflow.cwl']})"`
**Explanation:** Submits CWL workflow for execution on Arvados compute cluster.

### Get job status
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); print(api.jobs().get(uuid='job_uuid'))"`
**Explanation:** Retrieves status and metadata for specified job UUID.

### Download collection
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); collection = api.collections().get(uuid='collection_uuid'); print(collection.manifest_text())"`
**Explanation:** Downloads collection manifest and data from Arvados.

### List users
**Args:** `python -c "import arvados; api = arvados.api('v1', 'https://arvados.example.com', token='token'); print(api.users().list())"`
**Explanation:** Retrieves list of users in current Arvados instance.