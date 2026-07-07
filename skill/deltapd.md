---
name: deltapd
category: population-genomics
description: DeltaPD - detecting outliers in gene trees compared against a reference tree.
tags: [deltapd, population-genomics, phylogenetics, outlier-detection]
author: oxo-call-community
source_url: "https://github.com/Ecogenomics/DeltaPD"
---

## Concepts

- **Tool Overview**: deltapd (v0.1.5+) is a tool for detecting outlier genes in phylogenetic analyses by comparing gene trees against a reference species tree. It identifies genes with unusual evolutionary patterns.
- **Core Function**: Measures phylogenetic distance between individual gene trees and a reference species tree to identify genes with significantly different evolutionary histories.
- **Input/Output**: Input: Newick tree files (reference species tree, gene trees). Output: Outlier gene classifications, distance metrics, statistical significance.
- **Algorithm**: Uses tree distance metrics (e.g., Robinson-Foulds distance) to quantify differences between gene and species trees, identifying outliers with extreme distances.
- **Key Features**: Tree distance calculation, statistical outlier detection, supports large phylogenomic datasets, batch processing, visualization support.
- **Installation**: `conda install -c bioconda deltapd`

## Pitfalls

- **Input Requirements**: Requires properly rooted Newick tree files.
- **Tree Quality**: Poorly resolved trees may affect results.
- **Reference Tree**: Results depend on reference tree quality and topology.
- **Normalization**: Requires appropriate normalization for comparing trees.
- **Multiple Testing**: May require multiple testing correction for large datasets.

## Examples

### Identify outlier gene trees
**Args:** `deltapd --reference species.nwk --input genes/ --output outliers.tsv`
**Explanation:** Identifies outlier gene trees compared to reference tree.

### With statistical filtering
**Args:** `deltapd --reference species.nwk --input genes/ --output outliers.tsv --pvalue 0.05`
**Explanation:** Filter outliers by p-value threshold.

### Generate visualization
**Args:** `deltapd --reference species.nwk --input genes/ --output outliers.tsv --plot tree_distances.png`
**Explanation:** Generate plot of tree distance distribution.