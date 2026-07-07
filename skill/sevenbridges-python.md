---
name: sevenbridges-python
category: programming
description: sevenbridges-python - Seven Bridges API Python client bindings
tags: ["sevenbridges-python", "programming", "API", "cloud"]
author: oxo-call-community
source_url: "https://github.com/sbg/sevenbridges-python"
---

## Concepts

- **Tool Overview**: sevenbridges-python (v2.11.2) provides Python bindings for the Seven Bridges API.
- **Core Function**: Enables programmatic access to Seven Bridges cloud computing platform.
- **Algorithm**: Implements REST API client for cloud workflow management.
- **Input/Output**: Accepts API calls and produces cloud resources.
- **Cloud Integration**: Focuses on bioinformatics workflow management.
- **Applications**: Cloud computing, workflow orchestration, and data management.

## Pitfalls

- **API Credentials**: Requires proper API key configuration.
- **Network Requirements**: Requires internet connectivity.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Rate Limiting**: API rate limits may affect performance.

## Examples

### Initialize client
**Args:** `from sevenbridges import Api; api = Api(url='https://api.sbgenomics.com/v2', token='your_token')`
**Explanation:** Initializes API client.

### List projects
**Args:** `projects = api.projects.query()`
**Explanation:** Lists available projects.

### Upload file
**Args:** `api.files.upload(project='my_project', local_path='local_file.txt', name='remote_file.txt')`
**Explanation:** Uploads file to project.

### Run task
**Args:** `task = api.tasks.create(name='my_task', app='my_app', project='my_project', inputs={...})`
**Explanation:** Creates and runs analysis task.

### Help command
**Args:** `python -c "from sevenbridges import Api; help(Api)"`
**Explanation:** Shows available methods.

### Version check
**Args:** `python -c "import sevenbridges; print(sevenbridges.__version__)"`
**Explanation:** Shows current version.

### List files
**Args:** `files = api.files.query(project='my_project')`
**Explanation:** Lists files in project.