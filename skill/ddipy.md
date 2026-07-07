---
name: ddipy
category: programming
description: Python client for OmicsDI Restful API for accessing multi-omics datasets.
tags: [ddipy, programming, OmicsDI, API-client, multi-omics]
author: oxo-call-community
source_url: "https://github.com/OmicsDI/ddipy"
---

## Concepts

- **Tool Overview**: ddipy (v0.0.5+) is a Python client for the OmicsDI (Omics Discovery Index) Restful API, enabling programmatic access to multi-omics datasets from public repositories.
- **Core Function**: Provides a Python interface to search, retrieve, and download multi-omics datasets from the OmicsDI platform, which aggregates data from multiple repositories.
- **Input/Output**: Input: API queries, dataset identifiers. Output: Dataset metadata, download links, search results.
- **Algorithm**: Implements RESTful API calls to OmicsDI endpoints for dataset discovery and retrieval.
- **Key Features**: Dataset search, metadata retrieval, download facilitation, multi-repository access.
- **Installation**: `conda install -c bioconda ddipy`

## Pitfalls

- **API Availability**: Requires OmicsDI API service to be available.
- **Network Connection**: Needs internet connection for API calls.
- **Rate Limiting**: API may have rate limits for requests.
- **Dataset Access**: Some datasets may require additional authentication.
- **Data Formats**: Retrieved data may be in various formats depending on source repository.

## Examples

### Search datasets
**Args:** `python -c "from ddipy import client; c = client.Client(); results = c.search('cancer')"`
**Explanation:** Search OmicsDI for datasets related to cancer.

### Get dataset details
**Args:** `python -c "from ddipy import client; c = client.Client(); dataset = c.get_dataset('PXD000001')"`
**Explanation:** Retrieve details for a specific dataset by accession.

### Download dataset
**Args:** `python -c "from ddipy import client; c = client.Client(); c.download('PXD000001', 'output/')"`
**Explanation:** Download dataset files to specified directory.