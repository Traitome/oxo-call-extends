---
name: bttoxin_scanner
category: annotation
description: Toxin exploration tool for Bacillus thuringiensis
tags: [bttoxin, bacillus, toxin, annotation, scanner]
author: oxo-call-community
source_url: "https://github.com/liaochenlanruo/BtToxin_scanner"
---

## Concepts

- **Tool Overview**: BtToxin_scanner explores toxin genes in Bacillus thuringiensis genomes.
- **Core Function**: Scans genomes for known and novel toxin genes.
- **Input**: Assembled genome FASTA file.
- **Output**: Toxin gene scan results with annotations.
- **Application**: Comprehensive toxin gene discovery in B. thuringiensis.
- **Installation**: Install via bioconda: `conda install -c bioconda bttoxin_scanner`

## Pitfalls

- **Bacillus Specific**: Designed for Bacillus thuringiensis genomes.
- **Assembly Required**: Requires assembled genome.
- **Database Updates**: Toxin database should be current.

## Examples

### Scan for toxin genes
**Args:** `bttoxin_scanner -i genome.fa -o scan_results/`
**Explanation:** Scans Bacillus thuringiensis genome for toxin genes.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
