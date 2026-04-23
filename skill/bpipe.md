---
name: bpipe
category: hpc
description: A tool for running and managing bioinformatics pipelines
tags: [bpipe, pipeline, workflow, hpc, automation]
author: oxo-call-community
source_url: "https://github.com/ssadedin/bpipe"
---

## Concepts

- **Tool Overview**: Bpipe is a pipeline framework for running and managing bioinformatics workflows.
- **Core Function**: Defines, executes, and monitors multi-step bioinformatics pipelines.
- **Pipeline Definition**: Uses Groovy-based DSL for defining pipeline stages and dependencies.
- **Features**: Automatic file tracking, retry on failure, parallel execution, and logging.
- **Input**: Pipeline definition file (pipeline.groovy) and input data files.
- **Installation**: Install via bioconda: `conda install -c bioconda bpipe`

## Pitfalls

- **Java Required**: Requires Java runtime environment.
- **Pipeline Syntax**: Groovy syntax can be confusing; refer to documentation for examples.
- **File Naming**: Bpipe tracks files by naming convention; avoid manual file manipulation.
- **Resource Limits**: Set appropriate memory and CPU limits for each stage.

## Examples

### Run a pipeline
**Args:** `bpipe run pipeline.groovy input.fq`
**Explanation:** Executes the pipeline defined in pipeline.groovy with input data.

### Test pipeline without running
**Args:** `bpipe test pipeline.groovy`
**Explanation:** Validates pipeline definition without executing commands.

### Run with specific stages
**Args:** `bpipe run -p stage1,stage2 pipeline.groovy input.fq`
**Explanation:** Runs only specified stages of the pipeline.

### Retry failed pipeline
**Args:** `bpipe retry`
**Explanation:** Retries the last failed pipeline from the point of failure.

### Check pipeline status
**Args:** `bpipe query`
**Explanation:** Shows current pipeline execution status and progress.

### Stop running pipeline
**Args:** `bpipe stop`
**Explanation:** Gracefully stops the currently running pipeline.

### Cleanup intermediate files
**Args:** `bpipe cleanup`
**Explanation:** Removes intermediate files from previous pipeline runs.
