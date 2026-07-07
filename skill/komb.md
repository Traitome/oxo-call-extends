---
name: komb
category: metagenomics
description: Characterizing metagenomes using K-Core decomposition
tags: [komb, metagenomics, k-core, graph-analysis, network-analysis]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/komb"
---

## Concepts

- **K-Core Decomposition**: Applies graph-theoretic k-core decomposition to metagenomes
- **Network Analysis**: Analyzes microbial interaction networks
- **Connectivity Analysis**: Identifies highly connected components in metagenomes
- **Community Structure**: Reveals community structure in microbial networks
- **Hierarchical Analysis**: Provides hierarchical view of network organization
- **Metagenome Characterization**: Characterizes metagenome properties through graph analysis

## Pitfalls

- **Network Construction**: Results depend on how the network is constructed
- **Threshold Selection**: Edge weight thresholds affect k-core identification
- **Data Quality**: Noisy data produces unreliable network structures
- **Computational Complexity**: Large networks require significant resources
- **Interpretation**: K-core values require careful biological interpretation
- **Sparse Networks**: Sparse networks may have few or no k-cores

## Examples

### K-core decomposition
**Args:** `komb decompose -i network.tsv -o kcores.tsv`
**Explanation:** Performs k-core decomposition on microbial network.

### Build network first
**Args:** `komb network -i abundance.tsv -o network.gml`
**Explanation:** Builds microbial co-occurrence network from abundance data.

### Identify core taxa
**Args:** `komb identify-core -i network.tsv -k 5 -o core_taxa.txt`
**Explanation:** Identifies taxa in k-core of 5.

### Visualize k-cores
**Args:** `komb visualize -i kcores.tsv -o visualization.pdf`
**Explanation:** Creates visualization of k-core decomposition.

### Compare conditions
**Args:** `komb compare -i network1.tsv -i network2.tsv -o comparison.txt`
**Explanation:** Compares k-core structures between conditions.

### Batch processing
**Args:** `komb batch -d networks/ -o results/`
**Explanation:** Processes multiple networks in batch mode.