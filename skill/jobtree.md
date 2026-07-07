---
name: jobtree
category: programming
description: Python based pipeline management software for clusters that makes running recursive and dynamically scheduled computations straightforward.
tags: [jobtree, programming, pipeline, cluster, workflow]
author: oxo-call-community
source_url: "https://github.com/benedictpaten/jobTree"
---

## Concepts

- **Tool Overview**: jobtree (v09.04.2017) - Python-based pipeline management software for running recursive and dynamically scheduled computations on clusters.
- **Task Scheduling**: Dynamically schedules tasks across cluster nodes.
- **Recursive Workflows**: Supports recursive task definitions.
- **Fault Tolerance**: Handles job failures and retries automatically.
- **Cluster Integration**: Works with various cluster schedulers (SGE, SLURM, etc.).
- **Resource Management**: Manages computational resources efficiently.

## Pitfalls

- **Cluster Configuration**: Requires proper cluster scheduler configuration.
- **Memory Management**: Poor memory estimation can cause job failures.
- **Task Dependencies**: Incorrect dependency specification can break workflows.
- **Logging**: Insufficient logging can make debugging difficult.
- **Scalability**: Very large workflows may encounter scalability issues.
- **Python Version**: Requires specific Python version compatibility.

## Examples

### Run pipeline
**Args:** `jobTree --jobTree jobtree/ --command "python my_pipeline.py"`
**Explanation:** Runs a pipeline using jobTree.

### Specify resources
**Args:** `jobTree --jobTree jobtree/ --mem 4G --cpu 2 --command "python task.py"`
**Explanation:** Runs task with specified memory and CPU resources.

### Resume failed pipeline
**Args:** `jobTree --jobTree jobtree/ --resume`
**Explanation:** Resumes a previously failed pipeline from checkpoint.

### Local testing
**Args:** `jobTree --jobTree jobtree/ --local --command "python test.py"`
**Explanation:** Runs pipeline locally for testing.

### Set log level
**Args:** `jobTree --jobTree jobtree/ --logLevel DEBUG --command "python pipeline.py"`
**Explanation:** Runs pipeline with debug logging.

### Clean up job tree
**Args:** `jobTree --jobTree jobtree/ --cleanup`
**Explanation:** Cleans up job tree directory after completion.