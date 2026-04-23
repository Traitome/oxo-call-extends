---
name: breakfast
category: utility
description: Fast putative outbreak cluster and infection chain detection using SNPs
tags: [breakfast, outbreak, snp, cluster, epidemiology]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/breakfast"
---

## Concepts

- **Tool Overview**: Breakfast detects putative outbreak clusters and infection chains using SNP differences.
- **Core Function**: Identifies potential transmission clusters from SNP distance matrices.
- **Input**: SNP distance matrix or variant call files.
- **Output**: Cluster assignments and infection chain predictions.
- **Application**: Public health epidemiology and outbreak investigation.
- **Installation**: Install via bioconda: `conda install -c bioconda breakfast`

## Pitfalls

- **SNP Threshold**: Choose appropriate SNP threshold for cluster definition.
- **Sample Size**: Performance may vary with very large sample sets.
- **Temporal Data**: Including collection dates improves chain detection.
- **Distance Matrix**: Ensure correct format for input distance matrix.

## Examples

### Detect outbreak clusters
**Args:** `breakfast -i distances.tsv -o clusters.tsv`
**Explanation:** Identifies outbreak clusters from SNP distance matrix.

### Set SNP threshold
**Args:** `breakfast -i distances.tsv -t 10 -o clusters.tsv`
**Explanation:** Uses 10 SNP threshold for cluster definition.

### Include temporal data
**Args:** `breakfast -i distances.tsv -d dates.tsv -o chains.tsv`
**Explanation:** Uses collection dates for improved infection chain detection.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
