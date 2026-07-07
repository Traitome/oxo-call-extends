---
name: kiwidist
category: gene-expression
description: Combining gene-set analysis with network properties
tags: [kiwidist, gene-expression, gene-set-analysis, network, bioinformatics]
author: oxo-call-community
source_url: "https://pypi.org/project/KiwiDist/"
---

## Concepts

- **Gene-Set Analysis**: Analyzes groups of functionally related genes
- **Network Integration**: Integrates gene expression data with biological networks
- **Pathway Analysis**: Identifies enriched pathways from gene expression data
- **Network Properties**: Analyzes topological properties of gene networks
- **Functional Enrichment**: Detects statistically significant gene sets
- **Multi-omics Integration**: Combines multiple omics data types

## Pitfalls

- **Network Quality**: Results depend on network data quality
- **Multiple Testing**: Requires proper correction for multiple hypothesis testing
- **Gene Annotation**: Incomplete annotation affects analysis
- **Network Size**: Large networks require computational resources
- **Data Normalization**: Proper normalization is critical for expression data
- **Biological Relevance**: Statistical significance doesn't guarantee biological relevance

## Examples

### Perform gene-set analysis
**Args:** `kiwidist -i expression.csv -g gene_sets.gmt -o results.csv`
**Explanation:** Performs gene-set enrichment analysis on expression data.

### Analyze network properties
**Args:** `kiwidist -i network.graphml -o properties.csv --network`
**Explanation:** Analyzes topological properties of a gene network.

### Integrate expression and network
**Args:** `kiwidist -i expression.csv -n network.graphml -o integrated.csv`
**Explanation:** Integrates gene expression data with biological network.

### Pathway enrichment
**Args:** `kiwidist -i expression.csv -p pathways.gmt -o pathways.csv --pathway`
**Explanation:** Identifies enriched biological pathways.

### Compare conditions
**Args:** `kiwidist -i control.csv treated.csv -o comparison.csv --compare`
**Explanation:** Compares gene-set enrichment between conditions.

### Visualize results
**Args:** `kiwidist -i results.csv -o plot.pdf --visualize`
**Explanation:** Generates visualization of gene-set analysis results.