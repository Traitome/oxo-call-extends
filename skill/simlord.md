---
name: simlord
category: utility
description: SimLoRD is a read simulator for long reads from third generation sequencing. Currently, it supports the Pacific Biosciences SMRT error model.
tags: [simlord, utility]
author: oxo-call-community
source_url: "https://bitbucket.org/genomeinformatics/simlord/"
---

## Concepts

- **Tool Overview**: simlord (v1.0.4) - SimLoRD is a read simulator for long reads from third generation sequencing. Currently, it supports the Pacific Biosciences SMRT error model.
- **Core Function**: SimLoRD is a read simulator for long reads from third generation sequencing. Currently, it supports the Pacific Biosciences SMRT error model.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda simlord`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `simlord -i <input_file> -o <output_file>`
**Explanation:** Run simlord with typical input and output options.
