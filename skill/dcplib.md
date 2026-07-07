---
name: dcplib
category: programming
description: Modules shared among multiple Data Coordination Platform components for Human Cell Atlas.
tags: [dcplib, programming, Human-Cell-Atlas, data-platform, Python]
author: oxo-call-community
source_url: "http://github.com/HumanCellAtlas/dcplib"
---

## Concepts

- **Tool Overview**: dcplib (v3.12.0+) provides shared Python modules for the Data Coordination Platform (DCP) that supports the Human Cell Atlas (HCA). It includes utilities for data management, validation, and platform operations.
- **Core Function**: Provides common functionality for DCP components including the HCA command line interface, data ingest, and metadata management.
- **Input/Output**: Input: HCA metadata files, configuration files. Output: Validated metadata, formatted outputs, API responses.
- **Algorithm**: Implements data validation schemas, file format handling, and API interaction patterns for the HCA platform.
- **Key Features**: Metadata validation, file format support, API client utilities, logging and monitoring tools.
- **Installation**: `conda install -c bioconda dcplib`

## Pitfalls

- **Python Version**: Requires specific Python versions for compatibility.
- **API Changes**: May need updates when HCA platform API changes.
- **Network Requirements**: Some functions require access to HCA platform services.
- **Schema Updates**: Metadata schemas may change between versions.
- **Dependency Conflicts**: May have conflicts with other Python packages.

## Examples

### Validate metadata
**Args:** `python -c "from dcplib import validate; validate('metadata.json')"`
**Explanation:** Validate HCA metadata file against schema.

### Access HCA API
**Args:** `python -c "from dcplib import hca_api; client = hca_api.Client()"`
**Explanation:** Create HCA API client for platform access.

### Format metadata
**Args:** `python -c "from dcplib import format_metadata; format_metadata('input.json', 'output.json')"`
**Explanation:** Format metadata file according to HCA standards.