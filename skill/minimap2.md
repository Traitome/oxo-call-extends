---
name: minimap2
category: alignment
description: A versatile pairwise aligner for genomic and spliced nucleotide sequences.
tags: [minimap2, alignment]
author: oxo-call-community
source_url: "https://github.com/lh3/minimap2"
---

## Concepts

- **Tool Overview**: minimap2 v2.30 - A versatile pairwise aligner for genomic and spliced nucleotide sequences..
- **Core Function**: A versatile pairwise aligner for genomic and spliced nucleotide sequences.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda minimap2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Map long reads
**Args:** `-ax map-ont reference.fa reads.fq > alignment.sam`
**Explanation:** Maps Oxford Nanopore reads to reference genome.

### Map short reads
**Args:** `-ax sr reference.fa R1.fq R2.fq > alignment.sam`
**Explanation:** Maps short paired-end reads to reference.

