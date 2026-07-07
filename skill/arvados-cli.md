---
name: arvados-cli
category: utility
description: Arvados CLI - Command-line interface for Arvados data management platform
tags: [arvados-cli, utility, data-management, workflow, cloud-computing]
author: oxo-call-community
source_url: "https://arvados.org/"
---

## Concepts

- **Tool Overview**: Arvados CLI is the command-line interface for Arvados, an open-source platform for managing and analyzing biomedical and genomic data. Version 0.1.20151207150126.
- **Core Function**: Provides command-line access to Arvados platform for data storage, workflow execution, and resource management.
- **Data Management**: Manages data collections, datasets, and metadata in cloud-based storage.
- **Workflow Execution**: Submits and monitors computational workflows on Arvados compute clusters.
- **User Authentication**: Handles authentication and authorization for Arvados platform access.
- **Resource Monitoring**: Tracks job status, resource usage, and workflow progress.
- **Installation**: `conda install -c bioconda arvados-cli` or install from Arvados website.

## Pitfalls

- **Authentication**: Requires valid Arvados API token and endpoint. Incorrect credentials cause access failures.
- **Platform Dependency**: Designed specifically for Arvados platform. Cannot be used independently.
- **Network Connectivity**: Requires internet connection to Arvados server. Network issues affect all operations.
- **Data Transfer**: Large data transfers may be slow. Consider data locality and bandwidth.
- **Workflow Compatibility**: Workflows must be in Arvados-compatible formats (CWL, WDL).
- **Version Mismatch**: CLI version must match Arvados server version for full compatibility.

## Examples

### Display help
**Args:** `arv --help`
**Explanation:** Shows all available command-line options and subcommands.

### List collections
**Args:** `arv collection list`
**Explanation:** Lists all data collections available in current Arvados project.

### Upload data
**Args:** `arv collection create --name my_collection; arv keep put --collection my_collection data/`
**Explanation:** Creates new collection and uploads local data directory to Arvados storage.

### Run workflow
**Args:** `arv pipeline run --pipeline workflow.cwl --input input_data.txt`
**Explanation:** Submits CWL workflow for execution on Arvados compute cluster.

### Check job status
**Args:** `arv job list --status running`
**Explanation:** Lists currently running jobs with status information.

### Download data
**Args:** `arv keep get --output local_dir/ collection_uuid`
**Explanation:** Downloads data collection from Arvados to local directory.

### List users
**Args:** `arv user list`
**Explanation:** Lists all users in current Arvados instance with permissions.

### Get collection metadata
**Args:** `arv collection get collection_uuid`
**Explanation:** Retrieves detailed metadata and properties for specified collection.