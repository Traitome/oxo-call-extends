---
name: starcatpy
category: expression
description: Implements *CellAnnotator (aka *CAT/starCAT), annotating scRNA-Seq with predefined gene expression programs.
tags: [starcatpy, expression]
author: oxo-call-community
source_url: "https://github.com/immunogenomics/starCAT"
---

## Concepts

- **Tool Overview**: starcatpy (v1.0.10) - Implements *CellAnnotator (aka *CAT/starCAT), annotating scRNA-Seq with predefined gene expression programs.
- **Core Function**: Implements *CellAnnotator (aka *CAT/starCAT), annotating scRNA-Seq with predefined gene expression programs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda starcatpy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `starcatpy -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run starcatpy with typical input and output options.
