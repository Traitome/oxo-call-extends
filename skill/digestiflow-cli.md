---
name: digestiflow-cli
category: utility
description: Command-line interface for Digestiflow workflow management.
tags: [digestiflow-cli, utility, workflow, cli]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: digestiflow-cli - CLI tool for managing Digestiflow sequencing data processing workflows.
- **Core Function**: Manages and executes sequencing data processing workflows through a command-line interface.
- **Input/Output**: Expects workflow configuration; outputs processed results.
- **Installation**: `conda install -c bioconda digestiflow-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires proper workflow configuration.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `digestiflow-cli --config workflow.yaml --run`
**Explanation:** Executes Digestiflow workflow from configuration.
