---
name: spagrn
category: expression
description: A comprehensive tool to infer TF-centered, spatial gene regulatory networks for the spatially resolved transcriptomics (SRT) data.
tags: [spagrn, expression]
author: oxo-call-community
source_url: "https://github.com/BGI-Qingdao/SpaGRN"
---

## Concepts

- **Tool Overview**: spagrn (v1.1.0) - A comprehensive tool to infer TF-centered, spatial gene regulatory networks for the spatially resolved transcriptomics (SRT) data.
- **Core Function**: A comprehensive tool to infer TF-centered, spatial gene regulatory networks for the spatially resolved transcriptomics (SRT) data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spagrn`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spagrn -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run spagrn with typical input and output options.
