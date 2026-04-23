---
name: pgcgap
category: population-genomics
description: A prokaryotic genomics and comparative genomics analysis pipeline
tags: [pgcgap, population-genomics]
author: oxo-call-community
source_url: "https://github.com/liaochenlanruo/pgcgap/blob/master/README.md"
---

## Concepts
- **Tool Overview**: PGCGAP is a pipeline for prokaryotic comparative genomics analysis. It can take the pair-end reads, ONT reads or PacBio reads as input. In addition to genome assembly, gene prediction and annotation, it can also get common comparative genomics analysis results such as phylogenetic trees of single-core proteins and core SNPs, pan-genome, whole-genome Average Nucleotide Identity (ANI), orthogroups and orthologs, COG annotations, substitutions (SNPs) and insertions/deletions (indels), and antimicrobial and virulence genes mining with only one line of commands.
- **Core Function**: A prokaryotic genomics and comparative genomics analysis pipeline
- **Input/Output**: FASTQ/VCF/GFF/GTF
- **Installation**: `conda install -c bioconda pgcgap`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
