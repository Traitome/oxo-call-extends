---
name: chewiesnake
category: variant-calling
description: ChewieSnake is a snakemake workflow that performs cgMLST allele calling for a set of assembled genomes using chewBBACA.
tags: [chewiesnake, variant-calling]
author: oxo-call-community
source_url: "https://gitlab.com/bfr_bioinformatics/chewieSnake"
---

## Concepts

- **Tool Overview**: chewiesnake (v3.0.0) - ChewieSnake is a snakemake workflow that performs cgMLST allele calling for a set of assembled genomes using chewBBACA.
- **Core Function**: ChewieSnake is a snakemake workflow that performs cgMLST allele calling for a set of assembled genomes using chewBBACA.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda chewiesnake`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
