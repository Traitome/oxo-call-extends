---
name: rsrq
category: utility
description: A minimal Redis-backed queue system for managing background jobs.
tags: ["rsrq", "utility", "queue", "redis"]
author: oxo-call-community
source_url: "https://github.com/aaronmussig/rsrq"
---

## Concepts

- **Tool Overview**: rsrq (v1.1.0) is a lightweight Redis-backed queue system designed for managing asynchronous background jobs. It provides simple command-line interfaces for creating queues, submitting jobs, and monitoring job status.
- **Core Function**: Implements a job queue system using Redis as the backend, supporting job submission, prioritization, and result retrieval. Particularly useful for bioinformatics pipelines with multiple dependent tasks.
- **Architecture**: Uses Redis lists for queue management, with separate queues for pending, running, and completed jobs. Supports job priorities and worker concurrency.
- **Input/Output**: Job definitions as JSON payloads, results stored in Redis and retrievable via job ID.
- **Worker Model**: Supports multiple worker processes that poll queues for pending jobs, execute them, and store results.
- **Use Case**: Managing bioinformatics pipeline workflows, parallel processing of sequencing data, and coordinating distributed computing tasks.

## Pitfalls

- **Redis dependency**: Requires a running Redis server; jobs fail if Redis is unavailable.
- **Job persistence**: Jobs are stored in Redis memory by default; consider Redis persistence options for critical workflows.
- **Worker concurrency**: Too many workers can overwhelm Redis; monitor connection limits.
- **Job timeouts**: Long-running jobs may block workers; implement job timeouts or chunking.
- **Result size limits**: Large result payloads may exceed Redis string limits; use external storage for big results.
- **Queue management**: Orphaned jobs can accumulate; implement cleanup policies for stale jobs.

## Examples

### Create a new queue
**Args:** `rsrq queue create my_queue`
**Explanation:** Creates a new queue named 'my_queue' for job submission.

### Submit a job
**Args:** `rsrq job submit my_queue '{"command": "fastqc", "args": ["input.fastq"]}'`
**Explanation:** Submits a JSON-formatted job to the specified queue. The job payload contains the command and arguments to execute.

### List queues
**Args:** `rsrq queue list`
**Explanation:** Lists all available queues and their job counts (pending, running, completed).

### Start a worker
**Args:** `rsrq worker start my_queue --concurrency 4`
**Explanation:** Starts a worker process with 4 concurrent job handlers for the specified queue.

### Check job status
**Args:** `rsrq job status <job_id>`
**Explanation:** Retrieves the status of a specific job (pending, running, completed, failed).

### Retrieve job results
**Args:** `rsrq job result <job_id>`
**Explanation:** Fetches the output/results of a completed job.

### Delete a queue
**Args:** `rsrq queue delete my_queue`
**Explanation:** Deletes a queue and all associated jobs. Use with caution.
