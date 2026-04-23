---
name: naibr-plus
category: variant-calling
description: Identify novel adjacencies created by structural variations using linked-read data
tags: [naibr-plus, variant-calling, structural-variation, linked-reads, novel-adjacency]
author: oxo-call-community
source_url: "https://github.com/pontushojer/NAIBR"
---

## Concepts

- **Tool Overview**: NAIBR+ v0.5.4 - identifies novel adjacencies from structural variations using linked-read data.
- **Core Function**: Detects structural variant breakpoints as novel adjacencies in linked-read sequencing data.
- **Input/Output**: Takes linked-read BAM files; outputs novel adjacency calls in VCF/TSV format.
- **Installation**: `conda install -c bioconda naibr-plus`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires linked-read (10x Genomics) BAM files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-b aligned.bam -r reference.fasta -o output_dir`
**Explanation:** Identifies novel adjacencies from linked-read data.
