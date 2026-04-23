---
name: count_constant_sites
category: alignment
description: Compute the count of cases in constant sites in a (FASTA) multiple sequence alignment
tags: [count_constant_sites, alignment, FASTA]
author: oxo-call-community
source_url: "https://github.com/pvanheus/count_constant_sites"
---

## Concepts

- **Tool Overview**: count_constant_sites (v0.1.1) - Compute the count of cases in constant sites in a (FASTA) multiple sequence alignment
- **Core Function**: Given a FASTA file with a multiple sequence alignment of nucleotides, this tool counts the sites in the alignment that are constant. The output is a line suitable for use in IQTREE's `-fconst`, thus 4...
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda count_constant_sites`

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
