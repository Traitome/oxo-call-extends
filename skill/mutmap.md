---
name: mutmap
category: variant-calling
description: MutMap: pipeline to identify causative mutations responsible for a phenotype.
tags: [mutmap, variant-calling, mutation, phenotype, causative]
author: oxo-call-community
source_url: "https://github.com/YuSugihara/MutMap"
---

## Concepts

- **Tool Overview**: MutMap v2.4.0 - pipeline to identify causative mutations responsible for a phenotype.
- **Core Function**: Identifies causative mutations by combining bulked segregant analysis with whole-genome sequencing.
- **Input/Output**: Takes FASTQ files from mutant and reference pools; outputs SNP index plots and candidate mutations.
- **Installation**: `conda install -c bioconda mutmap`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure proper FASTQ input and reference genome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-1 mutant_R1.fastq -2 mutant_R2.fastq -r reference.fasta -o output_dir`
**Explanation:** Runs MutMap pipeline to identify causative mutations.
