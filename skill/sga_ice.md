---
name: sga_ice
category: assembly
description: Iterative error correction of long 250 or 300 bp Illumina reads minimizes the total amount of erroneous reads, which improves contig assembly
tags: [sga_ice, assembly]
author: oxo-call-community
source_url: "https://github.com/hillerlab/IterativeErrorCorrection"
---

## Concepts

- **Tool Overview**: sga_ice (v1.01) - Iterative error correction of long 250 or 300 bp Illumina reads minimizes the total amount of erroneous reads, which improves contig assembly
- **Core Function**: Iterative error correction of long 250 or 300 bp Illumina reads minimizes the total amount of erroneous reads, which improves contig assembly
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sga_ice`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sga_ice -i <reads.fastq> -o <output_dir>`
**Explanation:** Run sga_ice with typical input and output options.
