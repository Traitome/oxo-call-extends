---
name: cromwell-tools
category: hpc
description: Python library and CLI utilities for interacting with the Cromwell workflow engine via REST API
tags: [cromwell-tools, cromwell, workflow, WDL, python, cli, bioinformatics, hpc]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/cromwell-tools"
---

## Concepts

- **Tool Overview**: cromwell-tools (v2.4.1+) - Python library and command-line utilities for interacting with the Cromwell workflow engine via REST API.
- **Core Function**: Enables programmatic submission, monitoring, and management of WDL workflows on Cromwell servers; provides both Python API and CLI for workflow operations.
- **Commands**: submit, wait, status, abort, release_hold, query, health - covering full workflow lifecycle.
- **Authentication**: Supports 4 auth types: HTTPBasicAuth (username/password), secrets JSON file, OAuth (service account key), no auth.
- **Input/Output**: WDL files, JSON inputs, workflow options; returns workflow IDs, status, outputs.
- **Application**: Pipeline automation, workflow orchestration in Python scripts, batch workflow submission.
- **Installation**: `pip install cromwell-tools` or `conda install -c bioconda cromwell-tools`

## Pitfalls

- **Cromwell Server Required**: Requires running Cromwell server; cannot interact with local run mode.
- **Authentication**: Must configure correct auth combination (url + credentials); missing auth causes failures.
- **Secrets File Format**: JSON file must contain url, username, password fields for HTTPBasicAuth.
- **Service Account Key**: For OAuth, provide path to JSON key file from Google Cloud service account.

## Examples

### Submit workflow via CLI
**Args:** `cromwell-tools submit -w workflow.wdl -i inputs.json --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** Submit workflow using secrets JSON file for authentication to remote Cromwell server.

### Submit with Python API
**Args:** `cromwell-tools submit -w workflow.wdl -i input1.json input2.json -o options.json --url http://cromwell.example.com --username user --password pass`
**Explanation:** Submit with multiple input files and options using direct credentials.

### Check status with Python API
**Args:** `cromwell-tools status <workflow_id> --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** Query workflow status using secrets file for authentication.

### Wait for completion
**Args:** `cromwell-tools wait <workflow_id> --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** Block until workflow completes; useful for scripting sequential pipeline steps.

### Abort workflow
**Args:** `cromwell-tools abort <workflow_id> --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** Stop a running or on-hold workflow immediately.

### Query workflows
**Args:** `cromwell-tools query --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** List workflows; can filter by status, labels, or other metadata.

### Health check
**Args:** `cromwell-tools health --url http://cromwell.example.com`
**Explanation:** Verify Cromwell server is responding and get server version information.

### Submit with labels
**Args:** `cromwell-tools submit -w workflow.wdl -i inputs.json -l labels.json --url http://cromwell.example.com --secrets-file secrets.json`
**Explanation:** Submit with JSON file containing key-value label pairs for workflow organization.
