---
name: ucsc-bigwigcluster
category: analysis
description: UCSC bigWigCluster - Tool for clustering BigWig signals.
tags: [ucsc-bigwigcluster, ucsc, bigwig, clustering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigCluster - A tool for clustering regions based on BigWig signal.
- **Core Function**: Identifies clusters of high signal regions.
- **Input**: BigWig file, optional BED regions.
- **Output**: Clustered regions in BED format.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak calling, signal clustering, region identification.

## Pitfalls

- **Parameter Sensitivity**: Results depend on clustering parameters.
- **Memory**: May require significant memory for large datasets.

## Examples

### Cluster signals
**Args:** `bigWigCluster -input signal.bw -output clusters.bed`
**Explanation:** Identify clusters of high signal regions.

### With threshold
**Args:** `bigWigCluster -threshold=5 -input signal.bw -output clusters.bed`
**Explanation:** Cluster with minimum signal threshold.
