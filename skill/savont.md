---
name: savont
category: variant-calling
description: Amplicon sequencing variants (ASVs) and taxonomic profiling from modern long-read (nanopore + PacBio) amplicon sequencing with > 98% accuracy.
tags: ["savont", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/savont"
---

## Concepts

- **Tool Overview**: Amplicon sequencing variants (ASVs) and taxonomic profiling from modern long-read (nanopore + PacBio) amplicon sequencing with > 98% accuracy. (version 0.3.2)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda savont`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

