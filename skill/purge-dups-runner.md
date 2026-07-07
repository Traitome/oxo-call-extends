---
name: purge-dups-runner
category: hpc
description: purge-dups-runner is a high-performance cluster runner for executing purge_dups workflows.
tags: [purge-dups-runner, hpc, workflow-execution, cluster]
author: oxo-call-community
source_url: "https://github.com/dfguan/runner"
---

## Concepts

- **Tool Overview**: purge-dups-runner manages HPC workflows.
- **Core Function**: Workflow execution.
- **Algorithm**: Uses cluster scheduling.
- **Input Format**: Accepts workflow configs.
- **Output**: Produces workflow results.
- **Use Case**: HPC job management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Cluster Dependency**: Requires HPC environment.
- **Configuration**: Incorrect settings may fail.
- **Queue Limits**: May affect job submission.
- **Runtime**: Jobs may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `purge-dups-runner --help`
**Explanation:** Shows available options and usage instructions.

### Run workflow
**Args:** `purge-dups-runner run -c config.yaml -o output_dir`
**Explanation:** Executes purge_dups workflow on cluster.

### With parameters
**Args:** `purge-dups-runner run -c config.yaml -p params.yaml -o output_dir`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `purge-dups-runner -v run -c config.yaml -o output_dir`
**Explanation:** Runs with verbose output.

### Check status
**Args:** `purge-dups-runner status -j job_id`
**Explanation:** Checks job status.

### Stop job
**Args:** `purge-dups-runner stop -j job_id`
**Explanation:** Stops running job.

### Generate report
**Args:** `purge-dups-runner run -c config.yaml -o output_dir --report report.html`
**Explanation:** Generates HTML report.