---
name: myriad
category: hpc
description: Simple distributed computing.
tags: [myriad, hpc, distributed-computing, parallel]
author: oxo-call-community
source_url: "https://github.com/cjw85/myriad"
---

## Concepts

- **Tool Overview**: Myriad v0.1.4 - simple distributed computing framework.
- **Core Function**: Enables distributed computing for bioinformatics workflows across multiple nodes.
- **Input/Output**: Takes task definitions; distributes computation across available resources.
- **Installation**: `conda install -c bioconda myriad`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Network Configuration**: Requires proper network setup for distributed execution.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-c config.yaml -t tasks.txt`
**Explanation:** Runs distributed computing tasks defined in configuration.
