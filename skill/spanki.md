---
name: spanki
category: alignment
description: Spanki is a set of tools to facilitate analysis of alternative splicing from RNA-Seq data. Spanki compiles quantitative and qualitative information about junction alignments from input BAM files, and analyzes junction-level splicing along with pairwise-defined splicing events. A simulator is also included to evaluate junction detection performance.
tags: [spanki, alignment, bam]
author: oxo-call-community
source_url: "http://www.cbcb.umd.edu/software/spanki/"
---

## Concepts

- **Tool Overview**: spanki (v0.5.1) - Spanki is a set of tools to facilitate analysis of alternative splicing from RNA-Seq data. Spanki compiles quantitative and qualitative information about junction alignments from input BAM files, and analyzes junction-level splicing along with pairwise-defined splicing events. A simulator is also included to evaluate junction detection performance.
- **Core Function**: Spanki is a set of tools to facilitate analysis of alternative splicing from RNA-Seq data. Spanki compiles quantitative and qualitative information about junction alignments from input BAM files, and analyzes junction-level splicing along with pairwise-defined splicing events. A simulator is also included to evaluate junction detection performance.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spanki`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spanki -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run spanki with typical input and output options.
