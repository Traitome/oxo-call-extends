---
name: cwltool
category: hpc
description: Common Workflow Language reference implementation
tags: [cwltool, hpc, workflow, cwl, workflow-language, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/common-workflow-language/cwltool"
---

## Concepts

- **Tool Overview**: cwltool is the official reference implementation of the Common Workflow Language (CWL), a standard for describing analysis workflows and tools that are portable across different computing environments.
- **Core Function**: Executes CWL workflows and command line tools, providing a standardized way to define and run bioinformatics analyses.
- **Input/Output**: Input: CWL tool/workflow definition files (.cwl) and input parameter files (.yml/.yaml). Output: Workflow execution results in specified output directory.
- **CWL Standards**: Supports CWL v1.0, v1.1, and v1.2 standards for tool and workflow descriptions.
- **Container Support**: Built-in support for Docker and Singularity containers for reproducible execution.
- **Installation**: `conda install -c bioconda cwltool` or `pip install cwltool`

## Pitfalls

- **File Paths**: Input file paths in job YAML must be absolute or relative to the working directory where cwltool is run.
- **Docker Availability**: When using containerized tools, Docker must be available and running.
- **Validation Errors**: Always validate CWL files before execution to catch syntax errors early.
- **Output Directory**: Use `--outdir` to specify output location; otherwise outputs go to current directory.
- **Parallel Execution**: `--parallel` flag requires careful resource management to avoid overloading the system.

## Examples

### Validate a CWL workflow
**Args:** `--validate workflow.cwl`
**Explanation:** Validate the syntax and semantics of a CWL workflow file without executing it. Useful for catching errors before running.

### Run a workflow with input file
**Args:** `workflow.cwl inputs.yml`
**Explanation:** Execute a CWL workflow using input parameters specified in a YAML file. The simplest way to run a workflow.

### Run in parallel mode
**Args:** `--parallel workflow.cwl inputs.yml`
**Explanation:** Execute workflow steps in parallel where possible to improve performance for independent steps.

### Specify output directory
**Args:** `--outdir results/ workflow.cwl inputs.yml`
**Explanation:** Direct all output files to a specified directory for organized results.

### Generate provenance information
**Args:** `--write-summary workflow_summary.json workflow.cwl inputs.yml`
**Explanation:** Generate a JSON file with workflow execution provenance information including timing and resource usage.

### Generate template input file
**Args:** `--make-template tool.cwl > job.yml`
**Explanation:** Create a template YAML file with all required input parameters, which can be filled in manually.

### Run with Docker container
**Args:** `--docker workflow.cwl inputs.yml`
**Explanation:** Execute workflow steps in Docker containers for reproducible environments.

### Enable debug mode
**Args:** `--debug workflow.cwl inputs.yml`
**Explanation:** Enable verbose debugging output to troubleshoot workflow execution issues.
