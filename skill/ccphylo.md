---
name: ccphylo
category: phylogenetics
description: Phylogenetic analysis of samples based on nucleotide overlaps from KMA alignments
tags: [ccphylo, phylogenetics, kma, alignment, tree-building]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/ccphylo"
---

## Concepts

- **Tool Overview**: CCPhylo performs phylogenetic analysis using nucleotide overlap information from KMA alignments.
- **Core Function**: Builds phylogenetic trees from KMA-generated alignment data.
- **Algorithm**: Constructs trees based on SNP differences and overlaps between samples.
- **Input**: KMA alignment files (BAM/SAM format) or overlap matrices.
- **Output**: Phylogenetic tree in Newick format.
- **Application**: Comparative genomics and epidemiological studies.
- **Installation**: Install via bioconda: `conda install -c bioconda ccphylo`

## Pitfalls

- **KMA Required**: Designed to work with KMA alignment output.
- **Alignment Quality**: Tree quality depends on alignment accuracy.
- **SNP Calling**: Requires sufficient SNP density for meaningful trees.
- **Sample Size**: Too few samples may produce unreliable trees.

## Examples

### Build phylogenetic tree
**Args:** `ccphylo -i kma_results/ -o tree.nwk`
**Explanation:** Builds phylogenetic tree from KMA alignment results.

### With bootstrap support
**Args:** `ccphylo -i kma_results/ -b 100 -o tree_bootstrap.nwk`
**Explanation:** Performs 100 bootstrap replicates for branch support.

### Use distance matrix
**Args:** `ccphylo -d distance_matrix.tsv -o tree.nwk`
**Explanation:** Builds tree from pre-computed distance matrix.

### Display help
**Args:** `ccphylo --help`
**Explanation:** Shows all available options and usage information.