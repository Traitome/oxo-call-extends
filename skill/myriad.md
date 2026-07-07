---
name: myriad
category: hpc
description: Myriad - Simple distributed computing framework for bioinformatics
tags: [myriad, hpc, distributed-computing, parallel, bioinformatics, pipeline]
author: oxo-call-community
source_url: "https://github.com/cjw85/myriad"
---

## Concepts

- **Tool Overview**: Myriad v0.1.4 is a lightweight distributed computing framework designed for running bioinformatics workflows across multiple compute nodes. It provides a simple approach to parallelizing tasks that can be independently processed.
- **Core Function**: Distributes tasks defined in a task file across available compute nodes in a cluster or grid environment. Handles task scheduling, result collection, and failure recovery.
- **Architecture**: Uses a master-worker model where the master node distributes tasks and workers execute them. Supports dynamic task allocation based on node availability.
- **Input Format**: Takes task definition files (typically one task per line) and a configuration file specifying resources, output locations, and execution parameters.
- **Output**: Collects results from completed tasks into a designated output directory, with logging and error tracking for failed tasks.
- **Use Case**: Large-scale bioinformatics analyses that can be parallelized, such as processing multiple samples, running sequence alignments in batch, or executing workflows across a bioinformatics dataset.

## Pitfalls

- **Network Configuration**: Requires proper network setup between nodes. Firewalls and network restrictions can prevent inter-node communication.
- **Shared Filesystem**: Benefits from a shared filesystem (NFS, Lustre) across nodes. Without shared storage, result transfer becomes complex.
- **Task Independence**: Tasks must be truly independent. Shared resources or files between tasks can cause race conditions.
- **Resource Estimation**: Poor estimation of task resources may lead to node failures or resource contention.
- **Error Handling**: Partial failures require manual recovery. Ensure task scripts are robust and idempotent.
- **Configuration Complexity**: Initial setup requires understanding of cluster architecture and resource managers (SLURM, PBS, etc.).

## Examples

### Display help
**Args:** `myriad --help`
**Explanation:** Shows available command-line options and usage information.

### Run with configuration file
**Args:** `-c config.yaml -t tasks.txt`
**Explanation:** Standard Myriad workflow. Reads configuration and task list, then distributes tasks across available nodes.

### Dry run to validate configuration
**Args:** `-c config.yaml -t tasks.txt --dry-run`
**Explanation:** Validates configuration and task definitions without actually executing tasks. Useful for debugging.

### Specify output directory
**Args:** `-c config.yaml -t tasks.txt -o results/`
**Explanation:** Sets the output directory for task results. Each task typically creates a subdirectory or output file in this location.

### Run with verbose output
**Args:** `-c config.yaml -t tasks.txt -v`
**Explanation:** Enables verbose logging showing task distribution, node assignments, and progress updates.
