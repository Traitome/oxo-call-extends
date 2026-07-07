---
name: cromshell
category: hpc
description: Command-line interface to the Cromwell workflow manager for submitting, monitoring, and managing workflows
tags: [cromshell, cromwell, workflow, WDL, hpc, cli, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/cromshell"
---

## Concepts

- **Tool Overview**: cromshell (v2.1.1+) - Command-line interface to the Cromwell workflow manager.
- **Core Function**: Provides convenient CLI commands to interact with Cromwell server for workflow submission, status monitoring, output retrieval, and management.
- **Commands**: submit, wait, status, abort, release_hold, query, health - covering the full workflow lifecycle.
- **Authentication**: Supports multiple auth methods: HTTPBasicAuth (username/password), secrets JSON file, OAuth service account key, or no auth.
- **Input/Output**: Accepts WDL files, JSON inputs, workflow options; returns workflow IDs and status information.
- **Application**: Bioinformatics pipeline management, workflow automation, scripting Cromwell interactions.
- **Installation**: `conda install -c bioconda cromshell` or `pip install cromshell-tools`

## Pitfalls

- **Cromwell Server Required**: cromshell requires a running Cromwell server; cannot be used for local run mode workflows.
- **Authentication**: Ensure correct auth credentials are configured; misconfigured auth causes submission failures.
- **URL Configuration**: Default server URL may need adjustment; specify `--url` for remote Cromwell instances.
- **Secrets File**: If using secrets file for auth, ensure JSON format is correct with url, username, password fields.

## Examples

### Submit workflow
**Args:** `cromshell submit -w workflow.wdl -i inputs.json --url http://cromwell-server:8000`
**Explanation:** Submit WDL workflow to Cromwell server at specified URL with input JSON.

### Check workflow status
**Args:** `cromshell status <workflow_id> --url http://cromwell-server:8000`
**Explanation:** Query current status of submitted workflow by its ID.

### Wait for workflow completion
**Args:** `cromshell wait <workflow_id> --url http://cromwell-server:8000`
**Explanation:** Block until workflow completes (succeeds, fails, or aborts); useful in scripts.

### Abort workflow
**Args:** `cromshell abort <workflow_id> --url http://cromwell-server:8000`
**Explanation:** Stop a running or on-hold workflow immediately.

### Query workflow metadata
**Args:** `cromshell query --url http://cromwell-server:8000`
**Explanation:** List workflows matching criteria; useful for finding workflows by status or labels.

### Check Cromwell health
**Args:** `cromshell health --url http://cromwell-server:8000`
**Explanation:** Verify Cromwell server is responding; returns server status and version.

### Submit with dependencies
**Args:** `cromshell submit -w workflow.wdl -i inputs.json -d deps.zip --url http://cromwell-server:8000`
**Explanation:** Submit workflow with imported sub-workflows bundled in ZIP file.

### Submit with labels
**Args:** `cromshell submit -w workflow.wdl -i inputs.json -l labels.json --url http://cromwell-server:8000`
**Explanation:** Submit with JSON file containing key-value label pairs for organization.
