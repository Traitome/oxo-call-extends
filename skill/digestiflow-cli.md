---
name: digestiflow-cli
category: utility
description: digestiflow-cli - Command-line interface for Digestiflow workflow management.
tags: [digestiflow-cli, utility, workflow, cli]
author: oxo-call-community
source_url: "https://github.com/bihealth/digestiflow-cli"
---

## Concepts

- **Tool Overview**: digestiflow-cli is a command-line interface for managing Digestiflow sequencing data processing workflows.
- **Core Function**: Manages and executes sequencing data processing workflows through a command-line interface, integrating with the Digestiflow ecosystem.
- **Input/Output**: Input: Workflow configuration files, sequencing data. Output: Processed results, workflow logs, status reports.
- **Algorithm**: Orchestrates workflow execution, job submission, and result aggregation.
- **Key Features**: Workflow management, job submission, status monitoring, result aggregation, integration with cluster environments.
- **Installation**: `conda install -c bioconda digestiflow-cli`

## Pitfalls

- **Configuration Requirements**: Requires proper workflow configuration in YAML format.
- **Cluster Access**: Requires access to computing cluster for job execution.
- **Dependency Management**: Dependencies must be properly configured in the environment.
- **Network Access**: Requires network access for workflow orchestration.
- **File Paths**: Must use absolute paths for input/output files.

## Examples

### Run workflow from configuration
**Args:** `digestiflow-cli --config workflow.yaml --run`
**Explanation:** Executes Digestiflow workflow from YAML configuration file.

### Check workflow status
**Args:** `digestiflow-cli --config workflow.yaml --status`
**Explanation:** Check status of running or completed workflow.

### Submit to cluster
**Args:** `digestiflow-cli --config workflow.yaml --run --cluster slurm`
**Explanation:** Submit workflow jobs to Slurm cluster.

### Generate configuration template
**Args:** `digestiflow-cli --generate-config workflow.yaml`
**Explanation:** Generate template workflow configuration file.

### Resume failed workflow
**Args:** `digestiflow-cli --config workflow.yaml --resume`
**Explanation:** Resume previously failed workflow execution.