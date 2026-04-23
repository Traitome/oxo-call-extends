---
name: csem
category: alignment
description: ChIP-Seq multi-read allocation using Expectation-Maximization
tags: [csem, alignment, BAM]
author: oxo-call-community
source_url: "http://deweylab.biostat.wisc.edu/csem/"
---

## Concepts

- **Tool Overview**: csem (v2.4) - ChIP-Seq multi-read allocation using Expectation-Maximization
- **Core Function**: CSEM (Chung et al. 2011) uses an expectation-maximization algorithm to probabilistically reassign multi-mapping reads across the genome, producing a BAM in which multi-reads are allocated proportional...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda csem`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
