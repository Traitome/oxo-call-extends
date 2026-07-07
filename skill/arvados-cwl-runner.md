---
name: arvados-cwl-runner
category: hpc
description: Arvados CWL Runner - Execute Common Workflow Language workflows on Arvados platform
tags: [arvados-cwl-runner, hpc, cwl, workflow, arvados, cloud-computing]
author: oxo-call-community
source_url: "https://doc.arvados.org"
---

## Concepts

- **Tool Overview**: Arvados CWL Runner executes Common Workflow Language (CWL) workflows on the Arvados platform for distributed computing. Version 3.1.2.
- **Core Function**: Submits and manages CWL workflows on Arvados compute clusters with automatic resource allocation and job tracking.
- **CWL Support**: Implements CWL v1.0 specification for workflow portability across platforms.
- **Arvados Integration**: Leverages Arvados data management and compute resources for workflow execution.
- **Resource Management**: Automatically allocates compute resources based on workflow requirements.
- **Job Tracking**: Monitors workflow progress and provides status updates and logs.
- **Input/Output**: Accepts CWL workflow definitions and input data, outputs results to Arvados collections.
- **Installation**: `conda install -c bioconda arvados-cwl-runner` or install from Arvados documentation.

## Pitfalls

- **CWL Validation**: Workflows must be valid CWL v1.0. Use cwltool for validation before submission.
- **Arvados Authentication**: Requires valid API token and endpoint configuration.
- **Data References**: Input data must be accessible from Arvados (collections or Keep storage).
- **Resource Limits**: Workflow resource requests must match cluster capabilities. Excessive requests cause job failures.
- **Network Dependency**: Requires network connection to Arvados server for workflow monitoring.
- **Version Compatibility**: CWL runner version should match Arvados server version for full feature support.

## Examples

### Display help
**Args:** `arvados-cwl-runner --help`
**Explanation:** Shows all available command-line options and usage information.

### Run CWL workflow
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml`
**Explanation:** Executes CWL workflow with specified input parameters on Arvados compute cluster.

### Specify output collection
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml --output output_collection`
**Explanation:** Runs workflow and saves results to specified Arvados collection.

### Set resource requirements
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml --ram 8G --cores 4`
**Explanation:** Allocates 8GB RAM and 4 CPU cores for workflow execution.

### Enable debug mode
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml --debug`
**Explanation:** Enables debug mode with verbose logging for troubleshooting workflow issues.

### Specify project UUID
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml --project project_uuid`
**Explanation:** Runs workflow in specified Arvados project instead of default project.

### Dry run without execution
**Args:** `arvados-cwl-runner --workflow workflow.cwl --input inputs.yml --dry-run`
**Explanation:** Validates workflow and inputs without actual execution. Useful for testing.

### Resume failed workflow
**Args:** `arvados-cwl-runner --resume workflow_uuid --input inputs.yml`
**Explanation:** Resumes execution of previously failed workflow from checkpoint.