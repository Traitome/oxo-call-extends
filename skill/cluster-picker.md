---
name: cluster-picker
category: formatting
description: Identifies clusters in Newick-formatted phylogenetic trees with user-defined cut-offs
tags: [cluster-picker, phylogenetics, tree-analysis, clustering, bioinformatics]
author: oxo-call-community
source_url: "http://hiv.bio.ed.ac.uk/software.html"
---

## Concepts

- **Tool Overview**: Cluster Picker is a tool for identifying clusters in Newick-formatted phylogenetic trees, capable of handling thousands of sequences efficiently.
- **Core Function**: Identifies clusters based on user-defined cut-offs for within-cluster genetic distance and bootstrap support.
- **Algorithm**: Traverses phylogenetic trees to find monophyletic groups meeting user-defined criteria.
- **Input**: Newick-formatted phylogenetic tree with optional bootstrap values.
- **Output**: Cluster assignments with sequence membership information.
- **Application**: Phylogenetic analysis, outbreak investigation, and population structure analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cluster-picker`

## Pitfalls

- **Tree Format**: Requires properly formatted Newick trees.
- **Bootstrap Values**: Needs bootstrap support values for certain cut-offs.
- **Parameter Tuning**: May require adjustment of distance and bootstrap cut-offs.
- **Large Trees**: May require significant memory for very large trees.
- **Monophyly**: Assumes clusters are monophyletic groups.

## Examples

### Identify clusters
**Args:** `cluster-picker -i tree.nwk -o clusters.txt`
**Explanation:** Identifies clusters in phylogenetic tree with default parameters.

### With distance cut-off
**Args:** `cluster-picker -i tree.nwk -d 0.05 -o clusters.txt`
**Explanation:** Sets maximum within-cluster genetic distance to 0.05.

### With bootstrap cut-off
**Args:** `cluster-picker -i tree.nwk -b 70 -o clusters.txt`
**Explanation:** Requires minimum bootstrap support of 70% for clusters.

### Combined cut-offs
**Args:** `cluster-picker -i tree.nwk -d 0.05 -b 70 -o clusters.txt`
**Explanation:** Uses both distance and bootstrap cut-offs.

### Display help
**Args:** `cluster-picker --help`
**Explanation:** Shows all available options and usage information.