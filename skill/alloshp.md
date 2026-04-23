---
name: alloshp
category: alignment
description: From mapped reads to Single Homeologous Polymorphisms (SHPs): pipeline for phylogenetic studies of allopolyploids
tags: [alloshp, alignment, FASTA, VCF]
author: oxo-call-community
source_url: "https://github.com/eead-csic-compbio/AlloSHP"
---

## Concepts

- **Tool Overview**: alloshp (v2025.09.12) - From mapped reads to Single Homeologous Polymorphisms (SHPs): pipeline for phylogenetic studies of allopolyploids
- **Core Function**: This 3-step protocol computes Whole Genome Alignments (WGA) to discover Single Homeologous Polymorphisms (SHPs) out of reads mapped to concatenated genome sequeces. It requires FASTA and VCF input fil...
- **Input/Output**: VCF variant input/output
- **Installation**: `conda install -c bioconda alloshp`

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
