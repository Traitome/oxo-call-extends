---
name: cansnper
category: annotation
description: Hierarchical genotype classifier of clonal pathogens using canonical SNPs
tags: [cansnper, snp, typing, pathogen, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/adrlar/CanSNPer/"
---

## Concepts

- **Tool Overview**: CanSNPer classifies clonal pathogens using hierarchical canonical SNP typing.
- **Core Function**: Assigns isolates to phylogenetic groups using canonical SNPs.
- **Input**: Assembled genome FASTA or VCF files.
- **Output**: Hierarchical genotype assignments.
- **Application**: Pathogen surveillance and outbreak investigation.
- **Installation**: Install via bioconda: `conda install -c bioconda cansnper`

## Pitfalls

- **Database Required**: Requires SNP database for target organism.
- **Assembly Quality**: Missing regions may lead to untyped SNPs.
- **Organism Specific**: Designed for specific clonal pathogens.

## Examples

### Classify pathogen genotype
**Args:** `CanSNPer -i genome.fa -d database/ -o classification.tsv`
**Explanation:** Classifies pathogen isolate using canonical SNP database.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
