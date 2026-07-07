---
name: tardis
category: hpc
description: Pre-processor for bioinformatics cluster job submission.
tags: [tardis, hpc, job-scheduler, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/AgResearch/tardis"
---

## Concepts

- **Tool Overview**: tardis (v1.0.19) pre-processes jobs for cluster submission.
- **Core Function**: Manages and preprocesses bioinformatics workflows for HPC.
- **Algorithm**: Analyzes dependencies and prepares job scripts.
- **Input/Output**: Input: Workflow definitions; Output: Job scripts.
- **Applications**: Bioinformatics pipelines, HPC job management.
- **Installation**: `conda install -c bioconda tardis` or download from GitHub.

## Pitfalls

- **Cluster Configuration**: Requires proper cluster setup.
- **Job Dependencies**: Complex dependencies need careful configuration.
- **Resource Estimation**: May underestimate required resources.
- **File Permissions**: Requires proper file permissions.
- **Network Issues**: Cluster connectivity affects performance.
- **Version Compatibility**: Cluster software version compatibility.

## Examples

### Display help
**Args:** `tardis --help`
**Explanation:** Shows available options and usage information.

### Basic job submission
**Args:** `tardis -i workflow.yaml -o jobs/`
**Explanation:** Preprocess workflow for cluster submission.

### With resource limits
**Args:** `tardis -i workflow.yaml -o jobs/ -t 24:00:00 -m 32G`
**Explanation:** Specify time and memory limits.

### Verbose mode
**Args:** `tardis -i workflow.yaml -o jobs/ -v`
**Explanation:** Run with detailed logging for debugging.

### Dry run
**Args:** `tardis -i workflow.yaml -o jobs/ --dry-run`
**Explanation:** Test without actual job submission.

### Batch processing
**Args:** `for f in workflows/*.yaml; do tardis -i $f -o jobs/; done`
**Explanation:** Process multiple workflow files.

### Include dependencies
**Args:** `tardis -i workflow.yaml -o jobs/ --deps`
**Explanation:** Resolve job dependencies.

### Generate script only
**Args:** `tardis -i workflow.yaml -o script.sh --script-only`
**Explanation:** Generate shell script without submission.

### Submit jobs
**Args:** `tardis -i workflow.yaml -o jobs/ --submit`
**Explanation:** Preprocess and submit jobs to cluster.
