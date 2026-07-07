---
name: catnip-seq
category: sequence-analysis
description: Explore nucleotide divergence and sequence resolution across user-defined categories
tags: [catnip-seq, sequence-analysis, divergence, resolution, population-genetics]
author: oxo-call-community
source_url: "https://github.com/CIBIO-BU/catnip"
---

## Concepts

- **Tool Overview**: catnip-seq explores nucleotide divergence and sequence resolution across user-defined categories.
- **Core Function**: Analyzes sequence variation and divergence patterns within and between groups.
- **Algorithm**: Computes nucleotide diversity, divergence metrics, and sequence resolution statistics.
- **Input**: FASTA sequence alignments and category metadata.
- **Output**: Statistical summaries and visualizations of sequence divergence.
- **Application**: Population genetics, evolutionary biology, and sequence comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda catnip-seq`

## Pitfalls

- **Alignment Required**: Input sequences must be aligned.
- **Category Labels**: Requires proper category assignment for comparison.
- **Sample Size**: Small datasets may yield unreliable statistics.
- **Missing Data**: Handle gaps and missing data appropriately.

## Examples

### Analyze sequence divergence
**Args:** `catnip analyze -i alignment.fa -c categories.tsv -o results/`
**Explanation:** Analyzes nucleotide divergence across user-defined categories.

### Compute resolution statistics
**Args:** `catnip resolution -i alignment.fa -o resolution_stats.txt`
**Explanation:** Computes sequence resolution metrics.

### Generate visualization
**Args:** `catnip plot -i results/ -o figures/`
**Explanation:** Generates visualizations of divergence patterns.

### Display help
**Args:** `catnip --help`
**Explanation:** Shows all available options and usage information.