---
name: gencove
category: data-management
description: Gencove CLI - Command-line interface for accessing the Gencove API for genome sequencing and analysis.
tags: [gencove, api-client, genome-sequencing, data-management]
author: oxo-call-community
source_url: "https://docs.gencove.com"
---

## Concepts
- **API Access**: Accesses Gencove sequencing platform via API.
- **Data Management**: Manages sequencing data on Gencove platform.
- **Sample Tracking**: Tracks sequencing samples and workflows.
- **Result Retrieval**: Retrieves analysis results from the cloud.
- **Project Management**: Manages sequencing projects and batches.

## Pitfalls
- **API Authentication**: Requires valid API credentials.
- **Network Dependency**: Requires internet connection.
- **Rate Limiting**: Subject to API rate limits.
- **Data Transfer Costs**: Large data transfers may incur costs.
- **Service Availability**: Dependent on Gencove service availability.

## Examples
### Authenticate with API
**Args:** `gencove login --api-key your_api_key`
**Explanation:** Authenticates with Gencove API using API key.

### Upload sequencing data
**Args:** `gencove upload --project-id project_id --fastq-file sample.fastq`
**Explanation:** Uploads sequencing data to a specific project.

### List projects
**Args:** `gencove projects list`
**Explanation:** Lists all accessible projects.

### Get sample status
**Args:** `gencove samples get --sample-id sample_id`
**Explanation:** Retrieves status and metadata for a specific sample.

### Download results
**Args:** `gencove results download --result-id result_id -o output_dir/`
**Explanation:** Downloads analysis results to local directory.