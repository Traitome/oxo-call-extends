---
name: cromwell
category: hpc
description: Workflow Management System for scientific workflows described in WDL
tags: [cromwell, wdl, workflow, pipeline, hpc, cloud]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/cromwell"
---

## Concepts

- **Tool Overview**: Cromwell is a Workflow Management System that executes workflows written in the Workflow Description Language (WDL), supporting local, HPC, and cloud execution.
- **Core Function**: Orchestrates complex bioinformatics pipelines defined in WDL, handling task dependencies, parallelization, and resource management.
- **Input/Output**: Input: WDL workflow file and JSON input file. Output: Execution logs, output files, and metadata.
- **Execution Backends**: Supports multiple backends: Local, Google Cloud, AWS, Azure, and HPC schedulers (SLURM, SGE, LSF).
- **Call Caching**: Automatically caches completed tasks, skipping re-execution if inputs unchanged, saving time and resources.
- **Scalability**: Can run workflows from single tasks to thousands of parallel jobs across distributed systems.

## Pitfalls

- **WDL Version**: Ensure WDL syntax matches Cromwell version. WDL 1.0+ requires newer Cromwell versions.
- **Backend Configuration**: Must configure backend (local/cloud/HPC) before running. Default is local execution.
- **Input JSON**: Input JSON must match WDL input declarations exactly. Missing or extra inputs cause errors.
- **Memory/CPU**: Specify appropriate resources per task. Underestimating causes failures, overestimating wastes resources.
- **File Localization**: Cromwell localizes input files. Large files may cause delays. Use `localization_optional` for local files.

## Examples

### Run workflow locally
**Args:** `run workflow.wdl -i inputs.json`
**Explanation:** Executes the WDL workflow using local execution with inputs from JSON file.

### Run with specific backend
**Args:** `run workflow.wdl -i inputs.json -b google`
**Explanation:** Executes workflow on Google Cloud backend instead of local execution.

### Submit workflow to server
**Args:** `submit workflow.wdl -i inputs.json -H workflow_options.json`
**Explanation:** Submits workflow to running Cromwell server for asynchronous execution.

### Validate WDL syntax
**Args:** `validate workflow.wdl`
**Explanation:** Checks WDL file for syntax errors without executing the workflow.

### Check workflow status
**Args:** `status workflow_id`
**Explanation:** Queries the status of a running or completed workflow by its ID.

### Abort running workflow
**Args:** `abort workflow_id`
**Explanation:** Terminates a running workflow, useful for stopping hung or incorrect runs.

### Run with workflow options
**Args:** `run workflow.wdl -i inputs.json -o workflow_options.json`
**Explanation:** Uses workflow options file to specify execution parameters like memory, CPU, and call caching.

### Query workflow outputs
**Args:** `outputs workflow_id`
**Explanation:** Retrieves the output file paths for a completed workflow.
