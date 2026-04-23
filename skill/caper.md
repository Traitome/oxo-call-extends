---
name: caper
category: hpc
description: Cromwell Assisted Pipeline ExecutoR for running WDL workflows
tags: [caper, cromwell, wdl, workflow, pipeline]
author: oxo-call-community
source_url: "https://github.com/ENCODE-DCC/caper"
---

## Concepts

- **Tool Overview**: Caper is a Python wrapper for running WDL workflows on Cromwell.
- **Core Function**: Simplifies running WDL pipelines on local, cloud, and HPC backends.
- **Backends**: Supports Local, Google Cloud, AWS, and SLURM backends.
- **Input**: WDL workflow file and JSON input file.
- **Output**: Workflow execution results and metadata.
- **Application**: Running ENCODE and other WDL pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda caper`

## Pitfalls

- **Cromwell Required**: Requires Cromwell JAR file.
- **Backend Configuration**: Must configure backend before running.
- **Docker/Singularity**: Containers recommended for reproducibility.
- **Input JSON**: Input format must match WDL expectations.

## Examples

### Run WDL workflow locally
**Args:** `caper run pipeline.wdl -i inputs.json`
**Explanation:** Runs WDL workflow locally using Cromwell.

### Run on SLURM
**Args:** `caper run pipeline.wdl -i inputs.json --backend slurm`
**Explanation:** Submits WDL workflow to SLURM cluster.

### Run with Docker
**Args:** `caper run pipeline.wdl -i inputs.json --docker`
**Explanation:** Runs workflow using Docker containers.

### Display help
**Args:** `caper --help`
**Explanation:** Shows all available options and usage information.
