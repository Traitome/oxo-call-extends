---
name: bttcmp
category: annotation
description: Toxin mining tool for Bacillus thuringiensis
tags: [bttcmp, bacillus, toxin, annotation]
author: oxo-call-community
source_url: "https://github.com/liaochenlanruo/BTTCMP"
---

## Concepts

- **Tool Overview**: BTTCMP mines toxin genes from Bacillus thuringiensis genomes.
- **Core Function**: Identifies and characterizes toxin genes in B. thuringiensis.
- **Input**: Assembled genome FASTA file.
- **Output**: Toxin gene predictions and comparisons.
- **Application**: Comparative toxin gene analysis in B. thuringiensis.
- **Installation**: Install via bioconda: `conda install -c bioconda bttcmp`

## Pitfalls

- **Bacillus Specific**: Designed for Bacillus thuringiensis.
- **Assembly Required**: Requires assembled genome.
- **Python Dependency**: Requires Python runtime.

## Examples

### Run toxin mining
**Args:** `bttcmp -i genome.fa -o toxin_output/`
**Explanation:** Mines toxin genes from Bacillus thuringiensis genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
