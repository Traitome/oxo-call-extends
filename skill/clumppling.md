---
name: clumppling
category: alignment
description: Cluster matching and permutation program with integer linear programming
tags: [clumppling, clustering, population-structure, bioinformatics, linear-programming]
author: oxo-call-community
source_url: "https://github.com/PopGenClustering/Clumppling/blob/master/Clumppling_Manual.pdf"
---

## Concepts

- **Tool Overview**: Clumppling is a framework for aligning clustering results from population structure analysis using integer linear programming.
- **Core Function**: Matches and permutes clustering results across different analyses or datasets to facilitate comparison.
- **Algorithm**: Uses integer linear programming to find optimal matching between clustering solutions.
- **Input**: Clustering results from population structure analysis (e.g., STRUCTURE, ADMIXTURE).
- **Output**: Aligned clustering results and similarity metrics.
- **Application**: Population genetics, comparative analysis of clustering results, and visualization.
- **Installation**: Install via bioconda: `conda install -c bioconda clumppling`

## Pitfalls

- **Clustering Format**: Requires specific input format from supported clustering tools.
- **Computational Resources**: May require significant resources for large datasets.
- **Parameter Tuning**: May require adjustment of matching parameters.
- **Memory Usage**: May require significant memory for complex matching problems.
- **Result Interpretation**: Matching results require careful interpretation.

## Examples

### Match clustering results
**Args:** `clumppling -i cluster1.txt cluster2.txt -o matched.txt`
**Explanation:** Matches clustering results from two different analyses.

### With permutation
**Args:** `clumppling -i clusters.txt -p -o permuted.txt`
**Explanation:** Performs permutation analysis on clustering results.

### Generate visualization
**Args:** `clumppling -i clusters.txt -v -o plot.pdf`
**Explanation:** Generates visualization of aligned clusters.

### Display help
**Args:** `clumppling --help`
**Explanation:** Shows all available options and usage information.