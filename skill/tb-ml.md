---
name: tb-ml
category: containerization
description: A simple tool for creating machine learning antimicrobial resistance prediction pipelines using Docker containers for M. tuberculosis.
tags: [tb-ml, containerization]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/tb-ml"
---

## Concepts

- **Tool Overview**: tb-ml (v0.1.1) - A simple tool for creating machine learning antimicrobial resistance prediction pipelines using Docker containers for M. tuberculosis.
- **Core Function**: A simple tool for creating machine learning antimicrobial resistance prediction pipelines using Docker containers for M. tuberculosis.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tb-ml`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tb-ml -i <input_file> -o <output_file>`
**Explanation:** Run tb-ml with typical input and output options.
