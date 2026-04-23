---
name: stoatydive
category: annotation
description: StoatyDive is a tool to evaluate and classify predicted peak profiles to assess the binding specificity of a protein to its targets.
tags: [stoatydive, annotation]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/StoatyDive"
---

## Concepts

- **Tool Overview**: stoatydive (v1.1.1) - StoatyDive is a tool to evaluate and classify predicted peak profiles to assess the binding specificity of a protein to its targets.
- **Core Function**: StoatyDive is a tool to evaluate and classify predicted peak profiles to assess the binding specificity of a protein to its targets.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stoatydive`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stoatydive -i <input.fasta> -o <output.gff>`
**Explanation:** Run stoatydive with typical input and output options.
