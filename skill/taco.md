---
name: taco
category: expression
description: A tool for multi-sample transcriptome assembly from RNA-Seq
tags: [taco, expression, sam]
author: oxo-call-community
source_url: "https://github.com/tacorna/taco"
---

## Concepts

- **Tool Overview**: taco (v0.7.3) - A tool for multi-sample transcriptome assembly from RNA-Seq
- **Core Function**: A tool for multi-sample transcriptome assembly from RNA-Seq
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taco`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taco -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run taco with typical input and output options.
