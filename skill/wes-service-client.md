---
name: wes-service-client
category: bioinformatics
description: WES-Service-Client - Workflow Execution Service client.
tags: [wes-service-client, workflow, bioinformatics, api]
author: oxo-call-community
source_url: "https://github.com/ga4gh/wes-service"
---

## Concepts

- **Tool Overview**: WES-Service-Client - GA4GH WES API client.
- **Core Function**: Interacts with Workflow Execution Service.
- **Input**: Workflow files.
- **Output**: Execution results.
- **Installation**: Install via pip
- **Use Case**: Workflow execution, bioinformatics.

## Pitfalls

- **Network**: Requires network connectivity.
- **Complexity**: May have steep learning curve.

## Examples

### Submit workflow
**Args:** `wes-client submit -u https://wes.example.com -w workflow.wdl`
**Explanation:** Submit workflow to WES server.

### With options
**Args:** `wes-client status -u https://wes.example.com -r run_id`
**Explanation:** Check workflow status.
