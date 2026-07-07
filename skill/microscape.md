---
name: microscape
category: qc
description: Downstream analysis tools for amplicon sequencing — filtering, ordination, phylogeny, networks
tags: [microscape, qc, amplicon]
author: oxo-call-community
source_url: "https://github.com/rec3141/microscape"
---

## Concepts

- **Tool Overview**: microscape v0.1.0 provides downstream analysis tools for amplicon sequencing data.
- **Core Function**: Analyzes amplicon sequencing data with filtering, ordination, phylogeny, and networks.
- **Sequence Filtering**: Filters and quality controls sequence data.
- **Ordination Analysis**: Performs t-SNE/PCA ordination for community analysis.
- **Phylogenetic Tree**: Constructs phylogenetic trees using MAFFT + NJ.
- **Network Analysis**: Generates SparCC-style correlation networks.

## Pitfalls

- **Amplicon Specific**: Designed for amplicon sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Analysis accuracy depends on input data quality.
- **Reference Database**: Requires appropriate reference sequences.

## Examples

### Analyze amplicon data
**Args:** `microscape -i sequences.fasta -o analysis/`
**Explanation:** Performs downstream analysis on amplicon sequencing data.

### Filter sequences
**Args:** `microscape filter -i sequences.fasta -o filtered.fasta`
**Explanation:** Filters sequence data based on quality criteria.

### Generate ordination
**Args:** `microscape ordinate -i sequences.fasta -o ordination.txt`
**Explanation:** Performs t-SNE/PCA ordination analysis.

### Build phylogenetic tree
**Args:** `microscape phylogeny -i sequences.fasta -o tree.nwk`
**Explanation:** Constructs phylogenetic tree.

### Generate network
**Args:** `microscape network -i sequences.fasta -o network.json`
**Explanation:** Generates correlation network for visualization.