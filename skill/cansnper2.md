---
name: cansnper2
category: annotation
description: Toolkit for SNP-typing bacterial genomes
tags: [cansnper2, snp, typing, bacterial, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/FOI-Bioinformatics/CanSNPer2"
---

## Concepts

- **Tool Overview**: CanSNPer2 is a toolkit for SNP-based typing of bacterial genomes.
- **Core Function**: Assigns isolates to phylogenetic lineages using canonical SNPs.
- **Input**: Assembled genome FASTA or VCF files.
- **Output**: Lineage assignments and SNP profiles.
- **Application**: Bacterial epidemiology and strain typing.
- **Installation**: Install via bioconda: `conda install -c bioconda cansnper2`

## Pitfalls

- **Database Required**: Requires SNP database for the target organism.
- **Assembly Quality**: Poor assemblies may have missing SNP calls.
- **Organism Specific**: Designed for specific bacterial pathogens.

## Examples

### Type bacterial genome
**Args:** `cansnper2 -i genome.fa -d snp_database.tsv -o typing_results.tsv`
**Explanation:** Assigns bacterial isolate to lineage using SNP database.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
