---
name: json_collect_data_source
category: utility
description: Galaxy tool for collecting multiple datasets with metadata and handling archives.
tags: [json_collect_data_source, utility, Galaxy, JSON, data-management]
author: oxo-call-community
source_url: "https://github.com/fabio-cumbo/galaxy-json-collect-data-source"
---

## Concepts

- **Tool Overview**: json_collect_data_source (v1.0.1) - A Galaxy tool for receiving multiple datasets with metadata in a single query.
- **Data Collection**: Collects multiple datasets in a single operation.
- **Archive Handling**: Supports gz, bz2, tar, and zip archives.
- **Metadata Support**: Handles dataset metadata alongside data files.
- **Galaxy Integration**: Designed for use within Galaxy workflow systems.
- **Collection Organization**: Organizes archive contents into collections.

## Pitfalls

- **Archive Format**: Requires correct archive format.
- **File Size**: Very large archives may cause memory issues.
- **Metadata Format**: Metadata must be in correct JSON format.
- **Network Issues**: Remote data retrieval may fail.
- **Dependency Versions**: Requires specific dependency versions.
- **Collection Limits**: May have limits on number of files per collection.

## Examples

### Collect datasets from JSON
**Args:** `json_collect_data_source --input data.json --output collection`
**Explanation:** Collects datasets specified in JSON file.

### Handle gzipped archive
**Args:** `json_collect_data_source --input data.json --output collection --archive-type gz`
**Explanation:** Processes gzipped archive contents.

### Include metadata
**Args:** `json_collect_data_source --input data.json --metadata metadata.json --output collection`
**Explanation:** Includes custom metadata with collected datasets.

### Extract tar archive
**Args:** `json_collect_data_source --input data.json --output collection --archive-type tar`
**Explanation:** Extracts contents of tar archive.

### Recursive extraction
**Args:** `json_collect_data_source --input data.json --output collection --recursive`
**Explanation:** Recursively extracts nested archives.

### Validate input
**Args:** `json_collect_data_source --input data.json --validate`
**Explanation:** Validates input JSON without processing.