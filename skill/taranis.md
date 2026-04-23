---
name: taranis
category: assembly
description: Pipeline for wg/cgMLST allele calling
tags: [taranis, assembly]
author: oxo-call-community
source_url: "https://github.com/BU-ISCIII/taranis"
---

## Concepts

- **Tool Overview**: taranis (v2.0.1) - Pipeline for wg/cgMLST allele calling
- **Core Function**: Pipeline for wg/cgMLST allele calling
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taranis`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taranis -i <reads.fastq> -o <output_dir>`
**Explanation:** Run taranis with typical input and output options.
