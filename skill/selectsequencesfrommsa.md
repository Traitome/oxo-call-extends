---
name: selectsequencesfrommsa
category: alignment
description: Tool to select representative sequences from a multiple sequence alignment
tags: [selectsequencesfrommsa, alignment]
author: oxo-call-community
source_url: "https://github.com/eggzilla/SelectSequencesFromMSA"
---

## Concepts

- **Tool Overview**: selectsequencesfrommsa (v1.0.5) - Tool to select representative sequences from a multiple sequence alignment
- **Core Function**: Tool to select representative sequences from a multiple sequence alignment
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda selectsequencesfrommsa`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `selectsequencesfrommsa -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run selectsequencesfrommsa with typical input and output options.
