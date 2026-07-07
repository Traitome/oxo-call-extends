---
name: cromwell
category: hpc
description: Workflow Management System for scientific workflows described in WDL supporting local, HPC, and cloud execution
tags: [cromwell, wdl, workflow, pipeline, hpc, cloud, bioinformatics, cromwell]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/cromwell"
---

## Concepts

- **Tool Overview**: Cromwell (v29+) - A Workflow Management System that executes workflows written in the Workflow Description Language (WDL).
- **Core Function**: Orchestrates complex bioinformatics pipelines defined in WDL, handling task dependencies, parallelization via scatter/gather, and resource management across distributed systems.
- **Execution Modes**: Run mode (single workflow, for local prototyping), Server mode (web server for production, supports REST API and Swagger docs).
- **Execution Backends**: Local, Google Cloud (GCP), Amazon Web Services (AWS), Azure, HPC schedulers (SLURM, SGE, LSF, PBS).
- **Input/Output**: Input: WDL workflow file, JSON inputs file, optional workflow options and labels. Output: Execution logs, output files, metadata JSON.
- **Call Caching**: Automatically caches completed tasks; skips re-execution if inputs unchanged, saving time and resources.
- **Application**: Bioinformatics pipelines (GATK, ENCODE), bulk RNA-seq, variant calling, image processing workflows.
- **Installation**: Download JAR from GitHub releases, requires Java 17+. `conda install -c bioconda cromwell`

## Pitfalls

- **WDL Version**: Ensure WDL syntax matches Cromwell version; WDL 1.0+ requires Cromwell 29+.
- **Java Version**: Requires Java 17 or higher; older Java versions cause UnsupportedClassVersionError.
- **Backend Configuration**: Must configure backend (local/cloud/HPC) before running; default is local execution.
- **Input JSON**: Input JSON must match WDL input declarations exactly; missing or extra inputs cause errors.
- **Memory/CPU**: Specify appropriate resources per task in WDL; underestimating causes failures, overestimating wastes resources.
- **File Localization**: Cromwell localizes input files from remote URLs; large files may cause delays. Use `localization_optional` for local files.
- **Metadata Output**: By default metadata is not written; use `--metadata-output` to save workflow metadata.

## Examples

### Run workflow locally
**Args:** `java -jar cromwell.jar run workflow.wdl -i inputs.json`
**Explanation:** Executes the WDL workflow locally using inputs from JSON file; suitable for testing and prototyping.

### Start Cromwell server
**Args:** `java -jar cromwell.jar server`
**Explanation:** Starts Cromwell as a web server on port 8000; enables REST API access and Swagger documentation at http://localhost:8000.

### Validate WDL syntax
**Args:** `java -jar womtool.jar validate workflow.wdl`
**Explanation:** Check WDL file for syntax errors without executing; use womtool JAR for validation.

### Generate inputs template
**Args:** `java -jar womtool.jar inputs workflow.wdl > inputs.json`
**Explanation:** Auto-generate JSON template with all required input declarations; fill in actual values before running.

### Run with workflow options
**Args:** `java -jar cromwell.jar run workflow.wdl -i inputs.json -o options.json`
**Explanation:** Execute with additional workflow options like backend, docker credentials, or retry settings.

### Submit workflow to server
**Args:** `curl -X POST http://localhost:8000/api/workflows/v1 -F workflowSource=@workflow.wdl -F inputs=@inputs.json`
**Explanation:** Submit workflow via REST API to running Cromwell server for asynchronous execution.

### Check workflow status
**Args:** `curl http://localhost:8000/api/workflows/v1/<workflow_id>/status`
**Explanation:** Query the status of a running or completed workflow by its ID.

### Get workflow outputs
**Args:** `curl http://localhost:8000/api/workflows/v1/<workflow_id>/outputs`
**Explanation:** Retrieve output file paths and values from completed workflow.

### Abort running workflow
**Args:** `curl -X POST http://localhost:8000/api/workflows/v1/<workflow_id>/abort`
**Explanation:** Stop a running workflow immediately; may leave partial outputs.
