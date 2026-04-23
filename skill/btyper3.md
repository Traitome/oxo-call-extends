---
name: btyper3
category: annotation
description: In silico taxonomic classification of Bacillus cereus group isolates
tags: [btyper3, taxonomy, bacillus, classification, cereus-group]
author: oxo-call-community
source_url: "https://github.com/lmc297/BTyper3"
---

## Concepts

- **Tool Overview**: BTyper3 performs in silico taxonomic classification of Bacillus cereus group isolates.
- **Core Function**: Classifies Bacillus cereus group isolates using assembled genomes.
- **Features**: Species identification, toxin profiling, and virulence factor detection.
- **Input**: Assembled genome FASTA file.
- **Output**: Taxonomic classification and virulence profile.
- **Installation**: Install via bioconda: `conda install -c bioconda btyper3`

## Pitfalls

- **Bacillus Specific**: Designed for Bacillus cereus group only.
- **Assembly Required**: Requires assembled genome, not raw reads.
- **Database Updates**: Virulence databases should be updated periodically.

## Examples

### Classify Bacillus isolate
**Args:** `btyper3 -i assembly.fa -o btyper_results/`
**Explanation:** Classifies Bacillus cereus group isolate from assembled genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
