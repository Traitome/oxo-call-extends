---
name: strainy
category: assembly
description: Assembly-based metagenomic strain phasing using long reads.
tags: [strainy, assembly]
author: oxo-call-community
source_url: "https://github.com/katerinakazantseva/strainy"
---

## Concepts

- **Tool Overview**: strainy (v1.2) - Assembly-based metagenomic strain phasing using long reads.
- **Core Function**: Assembly-based metagenomic strain phasing using long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strainy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strainy -i <reads.fastq> -o <output_dir>`
**Explanation:** Run strainy with typical input and output options.
