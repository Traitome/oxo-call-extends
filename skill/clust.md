---
name: clust
category: hpc
description: Optimised consensus clustering of multiple heterogeneous datasets
tags: [clust, consensus-clustering, heterogeneous-data, bioinformatics, data-analysis]
author: oxo-call-community
source_url: "https://github.com/baselabujamous/clust"
---

## Concepts

- **Tool Overview**: clust is an optimized tool for consensus clustering of multiple heterogeneous datasets, combining results from different clustering methods.
- **Core Function**: Generates consensus clustering across multiple datasets and clustering algorithms to improve robustness.
- **Algorithm**: Uses ensemble methods to combine clustering results from different approaches.
- **Input**: Multiple clustering results or datasets from different sources.
- **Output**: Consensus clustering with improved stability and robustness.
- **Application**: Multi-omics data integration, consensus analysis, and data integration studies.
- **Installation**: Install via bioconda: `conda install -c bioconda clust`

## Pitfalls

- **Data Heterogeneity**: Requires careful handling of different data types.
- **Computational Resources**: May require significant resources for large datasets.
- **Parameter Tuning**: May require adjustment of consensus parameters.
- **Memory Usage**: May require significant memory for complex analyses.
- **Result Interpretation**: Consensus clustering requires careful interpretation.

## Examples

### Perform consensus clustering
**Args:** `clust -i dataset1.txt dataset2.txt -o consensus.txt`
**Explanation:** Generates consensus clustering from multiple datasets.

### With custom parameters
**Args:** `clust -i datasets.txt -o consensus.txt -k 5`
**Explanation:** Specifies number of clusters (k=5) for consensus clustering.

### Include weights
**Args:** `clust -i datasets.txt -w weights.txt -o consensus.txt`
**Explanation:** Uses weighted consensus with specified weights for each dataset.

### Display help
**Args:** `clust --help`
**Explanation:** Shows all available options and usage information.