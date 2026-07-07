---
name: funnel
category: programming
description: Funnel is a toolkit for distributed task execution via a simple, standard API.
tags: [funnel, distributed computing, task execution, workflow]
author: oxo-call-community
source_url: "https://ohsu-comp-bio.github.io/funnel/"
---

## Concepts
- **Distributed Execution**: Executes tasks across distributed computing resources.
- **Task Scheduling**: Schedules and manages computational tasks.
- **Standard API**: Provides simple, standard API for task submission.
- **Resource Management**: Manages computational resources efficiently.
- **Workflow Orchestration**: Orchestrates complex workflows.

## Pitfalls
- **Cluster Setup**: Requires cluster infrastructure setup.
- **Configuration Complexity**: Complex configuration for distributed environments.
- **Network Dependencies**: Requires stable network connections.
- **Monitoring**: Requires monitoring infrastructure for task tracking.
- **Fault Tolerance**: Needs proper fault tolerance configuration.

## Examples
### Submit task
**Args:** `funnel tasks submit --config task.yaml`
**Explanation:** Submits a task using YAML configuration.

### Start server
**Args:** `funnel server run`
**Explanation:** Starts the Funnel server.

### List tasks
**Args:** `funnel tasks list`
**Explanation:** Lists all submitted tasks.

### Get task status
**Args:** `funnel tasks get <task-id>`
**Explanation:** Gets status of a specific task.

### Cancel task
**Args:** `funnel tasks cancel <task-id>`
**Explanation:** Cancels a running task.