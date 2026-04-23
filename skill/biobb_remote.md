---
name: biobb_remote
category: utility
description: BioBB module for remote execution via SSL
tags: [bioexcel, remote-execution, ssl, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_remote"
---

## Concepts
- **Tool Overview**: biobb_remote provides BioExcel Building Blocks for remote execution of BioBB components via SSL connections.
- **Remote Execution**: Submits and monitors BioBB jobs on remote HPC systems.
- **Applications**: Cloud computing, HPC cluster utilization, distributed workflows.

## Pitfalls
- **Network Configuration**: Requires proper SSL configuration and remote system access.
- **Authentication**: Requires credentials for remote system access.

## Examples
### Submit remote job
**Args:** `biobb_remote.submit --host hpc.example.com --job workflow.yml --output job_status.json`
**Explanation:** Submits a BioBB workflow to a remote HPC system.
