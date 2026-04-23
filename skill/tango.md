---
name: tango
category: metagenomics
description: Assign taxonomy to metagenomic contigs
tags: [tango, metagenomics]
author: oxo-call-community
source_url: "https://github.com/johnne/tango"
---

## Concepts

- **Tool Overview**: tango (v0.5.7) - Assign taxonomy to metagenomic contigs
- **Core Function**: Assign taxonomy to metagenomic contigs
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tango`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tango -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run tango with typical input and output options.
