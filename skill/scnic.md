---
name: scnic
category: statistics
description: SCNIC - Sparse Cooccurence Network Investigation for Compositional data
tags: ["scnic", "statistics", "network-analysis", "compositional-data"]
author: oxo-call-community
source_url: "https://github.com/lozuponelab/SCNIC"
---

## Concepts

- **Tool Overview**: SCNIC (v0.6.6) is a tool for Sparse Cooccurence Network Investigation for Compositional data.
- **Core Function**: Identifies co-occurring features in compositional data using network analysis.
- **Algorithm**: Uses sparse co-occurrence network analysis for microbial community data.
- **Input/Output**: Accepts feature tables and produces network analysis results.
- **Compositional Data**: Specifically designed for compositional data like microbiome datasets.
- **Applications**: Microbiome analysis, co-occurrence network analysis, and feature correlation detection.

## Pitfalls

- **Data Normalization**: Requires proper normalization of compositional data.
- **Sparsity**: May struggle with highly sparse datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Network Complexity**: May produce complex networks that require interpretation.

## Examples

### Basic network analysis
**Args:** `scnic network -i features.tsv -o network.tsv`
**Explanation:** `-i` input feature table; `-o` network output.

### Module detection
**Args:** `scnic modules -i features.tsv -o modules.tsv`
**Explanation:** Detects modules in co-occurrence network.

### Correlation analysis
**Args:** `scnic correlate -i features.tsv -o correlations.tsv`
**Explanation:** Computes correlations between features.

### Visualization
**Args:** `scnic plot -i network.tsv -o network.png`
**Explanation:** Generates visualization of co-occurrence network.

### Verbose logging
**Args:** `scnic network -i features.tsv -v -o network.tsv`
**Explanation:** `-v` enables verbose output for debugging.

### Filter low-abundance
**Args:** `scnic filter -i features.tsv -m 0.1 -o filtered.tsv`
**Explanation:** `-m 0.1` filters features with abundance < 0.1.

### Multiple datasets
**Args:** `scnic merge -i dataset1.tsv dataset2.tsv -o merged.tsv`
**Explanation:** Merges multiple feature tables.