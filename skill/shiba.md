---
name: shiba
category: expression
description: A versatile method for systematic identification of differential RNA splicing across platforms
tags: [shiba, expression]
author: oxo-call-community
source_url: "https://sika-zheng-lab.github.io/Shiba"
---

## Concepts

- **Tool Overview**: shiba (v0.8.2) - A versatile method for systematic identification of differential RNA splicing across platforms
- **Core Function**: A versatile method for systematic identification of differential RNA splicing across platforms
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shiba`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shiba -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run shiba with typical input and output options.
