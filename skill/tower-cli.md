---
name: tower-cli
category: utility
description: Tower CLI - Command-line interface for Nextflow Tower.
tags: [tower-cli, nextflow, tower, workflow, cli]
author: oxo-call-community
source_url: "https://github.com/seqeralabs/tower-cli"
---

## Concepts

- **Tool Overview**: Tower CLI - A command-line interface for interacting with Nextflow Tower platform.
- **Core Function**: Manages workflow execution, monitors pipelines, and interacts with Tower platform.
- **Input**: Tower credentials, workflow configurations.
- **Output**: Workflow status, execution logs, pipeline results.
- **Installation**: `pip install tower-cli`
- **Use Case**: Workflow management, pipeline monitoring, automation.

## Pitfalls

- **Credentials**: Requires Tower platform credentials and API access.
- **Network**: Requires network connectivity to Tower server.

## Examples

### Submit workflow
**Args:** `tw submission create --workflow my_workflow.nf --params params.json`
**Explanation:** Submit workflow to Tower for execution.

### Monitor workflow
**Args:** `tw submission logs --id 12345`
**Explanation:** View logs for running workflow.
