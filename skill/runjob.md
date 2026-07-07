---
name: runjob
category: workflow_management
description: Manage jobs or pipeline of bioinformatics analysis.
tags: ["runjob", "workflow", "pipeline", "job", "management"]
author: oxo-call-community
source_url: "https://runjob.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: runjob (v2.10.9) is a bioinformatics workflow management tool for orchestrating and managing computational jobs and pipelines. It provides a flexible framework for defining, scheduling, and monitoring bioinformatics analyses.
- **Core Function**: Manages job submission, dependency resolution, resource allocation, and workflow execution across local and cluster environments.
- **Architecture**: Supports job queues, task dependencies, and parallel execution. Integrates with various schedulers like SGE, SLURM, and PBS.
- **Input Format**: Workflow definition files in YAML or JSON format, specifying tasks, dependencies, and resource requirements.
- **Output Format**: Execution logs, task status reports, and workflow outputs. Supports integration with logging and monitoring systems.
- **Use Case**: Managing multi-step bioinformatics pipelines, automating repetitive analyses, coordinating distributed computing resources.

## Pitfalls

- **Scheduler compatibility**: Requires proper configuration for different cluster schedulers.
- **Resource estimation**: Incorrect resource allocation can lead to job failures or wasted resources.
- **Dependency management**: Complex dependencies require careful workflow design.
- **Error handling**: Failure propagation may require manual intervention.
- **Configuration complexity**: Setting up environments and paths can be challenging.
- **Scalability**: Very large workflows may encounter performance issues.

## Examples

### Run a workflow
**Args:** `runjob execute workflow.yaml`
**Explanation:** Executes a workflow defined in YAML format.

### Check job status
**Args:** `runjob status <job_id>`
**Explanation:** Checks the status of a running or completed job.

### Submit a single job
**Args:** `runjob submit --command "fastqc input.fastq" --name fastqc_job`
**Explanation:** Submits a single command as a job.

### Define workflow in YAML
**Args:** `runjob validate workflow.yaml`
**Explanation:** Validates a workflow definition file for syntax errors.

### Monitor running jobs
**Args:** `runjob monitor`
**Explanation:** Starts a monitoring interface for running jobs.

### Cancel a job
**Args:** `runjob cancel <job_id>`
**Explanation:** Cancels a running job.

### List all jobs
**Args:** `runjob list`
**Explanation:** Lists all jobs with their statuses.
