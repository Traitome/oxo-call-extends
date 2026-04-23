---
name: bttoxin_digger
category: annotation
description: Toxin mining tool for Bacillus thuringiensis
tags: [bttoxin, bacillus, toxin, annotation, mining]
author: oxo-call-community
source_url: "https://github.com/liaochenlanruo/BtToxin_Digger"
---

## Concepts

- **Tool Overview**: BtToxin_Digger mines toxin genes from Bacillus thuringiensis genomes.
- **Core Function**: Identifies and annotates toxin genes in B. thuringiensis genomes.
- **Input**: Assembled genome FASTA file.
- **Output**: Toxin gene predictions and annotations.
- **Application**: Biopesticide development and B. thuringiensis characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda bttoxin_digger`

## Pitfalls

- **Bacillus Specific**: Designed for Bacillus thuringiensis genomes.
- **Assembly Required**: Requires assembled genome, not raw reads.
- **Database Dependency**: Uses toxin gene database for annotation.

## Examples

### Mine toxin genes
**Args:** `bttoxin_digger -i genome.fa -o toxin_results/`
**Explanation:** Identifies toxin genes in Bacillus thuringiensis genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
