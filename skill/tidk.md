---
name: tidk
category: utility
description: TIDK - Tandem repeat Identity and Density Kit for genomic analysis.
tags: [tidk, tandem-repeat, identity, density, genomics, repeat-analysis]
author: oxo-call-community
source_url: "https://github.com/genome-tools/tidk"
---

## Concepts

- **Tool Overview**: TIDK (Tandem repeat Identity and Density Kit) - A toolkit for analyzing tandem repeat identity and density across genomic regions.
- **Core Function**: Calculates tandem repeat identity scores and density metrics for genomic regions or comparisons.
- **Input**: Genomic sequences, repeat annotations, or genome comparison data.
- **Output**: Repeat identity statistics, density plots, and comparison tables.
- **Installation**: `pip install tidk` or `conda install -c bioconda tidk`
- **Use Case**: Comparing repeat evolution between species, studying repeat turnover.

## Pitfalls

- **Annotation Required**: Requires accurate repeat annotations for analysis.
- **Comparison Context**: Meaningful comparisons require evolutionarily relevant contexts.

## Examples

### Calculate repeat density
**Args:** `tidk density -i genome.fasta -o density_results/`
**Explanation:** Calculate tandem repeat density across the genome.

### Compare two genomes
**Args:** `tidk compare -g1 genome1.fasta -g2 genome2.fasta -o comparison/`
**Explanation:** Compare tandem repeat identity and density between two genomes.
