---
name: sodar-cli
category: utility
description: SODAR CLI - Command line interface to SODAR via REST API
tags: [sodar-cli, utility, rest-api, sodar, command-line]
author: oxo-call-community
source_url: "https://github.com/bihealth/sodar-cli"
---

## Concepts

- **Tool Overview**: sodar-cli (v0.1.0) - A CLI for SODAR bioinformatics platform
- **Core Function**: Provides command-line access to SODAR REST API
- **Input/Output**: API commands; outputs SODAR data and responses
- **Algorithm**: Communicates with SODAR via REST API endpoints
- **Installation**: `conda install -c bioconda sodar-cli`
- **Key Features**: REST API, SODAR integration, command-line access

## Pitfalls

- **API Configuration**: Requires proper API configuration and credentials
- **Network Connectivity**: Requires network access to SODAR server
- **Authentication**: Requires valid authentication tokens
- **API Version**: Must use compatible API version
- **Rate Limits**: May be subject to API rate limits
- **Error Handling**: Requires proper error handling for API responses

## Examples

### Display help
**Args:** `sodar-cli --help`
**Explanation:** Shows available options and usage information.

### Configure connection
**Args:** `sodar-cli config --url https://sodar.server --token API_TOKEN`
**Explanation:** Configure SODAR connection.

### List projects
**Args:** `sodar-cli project list`
**Explanation:** List available projects.

### Get project info
**Args:** `sodar-cli project get PROJECT_UUID`
**Explanation:** Get project information.

### Upload file
**Args:** `sodar-cli file upload --project PROJECT_UUID --file data.txt`
**Explanation:** Upload file to SODAR.

### Download file
**Args:** `sodar-cli file download --file FILE_UUID --output data.txt`
**Explanation:** Download file from SODAR.

### Create assay
**Args:** `sodar-cli assay create --project PROJECT_UUID --name "Assay1"`
**Explanation:** Create new assay.

### List samples
**Args:** `sodar-cli sample list --project PROJECT_UUID`
**Explanation:** List project samples.