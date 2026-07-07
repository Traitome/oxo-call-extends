---
name: dxpy
category: programming
description: "DNAnexus Platform API bindings for Python."
tags: [dxpy, programming, DNAnexus, API, Python, cloud]
author: oxo-call-community
source_url: "http://autodoc.dnanexus.com/bindings/python/current"
---

## Concepts

- **Tool Overview**: dxpy is the official Python library for interacting with the DNAnexus platform.
- **Core Function**: Provides Python bindings for the DNAnexus API, enabling programmatic access to platform resources.
- **Input/Output**: Input: Python scripts using dxpy library. Output: API responses, file uploads/downloads, job submissions.
- **Algorithm**: Wraps DNAnexus REST API calls in Pythonic interfaces.
- **Key Features**: File management, job execution, workflow management, data querying, authentication handling.
- **Installation**: `conda install -c bioconda dxpy`

## Pitfalls

- **Authentication**: Requires valid DNAnexus authentication token.
- **API Limits**: Subject to DNAnexus API rate limits.
- **Version Compatibility**: API changes may require dxpy updates.
- **Error Handling**: Network issues can cause API call failures.
- **Resource Costs**: Cloud operations may incur compute and storage costs.

## Examples

### Upload file
**Args:** `dxpy upload file.txt --project project-xxxx`
**Explanation:** Uploads a file to DNAnexus project.

### Download file
**Args:** `dxpy download file-xxxx --output local_file.txt`
**Explanation:** Downloads a file from DNAnexus to local system.

### Run job
**Args:** `dxpy run app-xxxx --input input.json`
**Explanation:** Runs a DNAnexus app with specified inputs.

### List projects
**Args:** `dxpy find projects`
**Explanation:** Lists accessible DNAnexus projects.

### Query data
**Args:** `dxpy find data --project project-xxxx --type file`
**Explanation:** Finds all files in a specific project.