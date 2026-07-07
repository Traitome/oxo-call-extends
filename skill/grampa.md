---
name: grampa
category: bioinformatics
description: GRAMPA identifies and places polyploidy events on a phylogeny and counts duplications and losses in the presence of polyploidy.
tags: [grampa, phylogenetics, polyploidy, gene-duplication, bioinformatics]
author: oxo-call-community
source_url: "https://gwct.github.io/grampa"
---

## Concepts

- **Polyploidy Detection**: GRAMPA identifies polyploidy events in phylogenetic trees and places them on the tree.

- **Gene Tree Analysis**: Analyzes gene trees to detect duplication and loss events in the presence of polyploidy.

- **Phylogenetic Placement**: Places polyploidy events at appropriate positions on the species tree.

- **Duplication/Loss Counting**: Counts gene duplications and losses while accounting for polyploidy events.

- **Synteny Analysis**: Incorporates synteny information to improve polyploidy detection accuracy.

- **Visualization**: Generates visualizations of polyploidy events and gene family evolution.

## Pitfalls

- **Gene Tree Quality**: Results depend on the quality of input gene trees. Poorly resolved trees can produce incorrect results.

- **Species Tree**: Requires a well-supported species tree as input. Incorrect species trees will affect placement.

- **Polyploidy Complexity**: Very complex polyploidy histories may be difficult to resolve.

- **Computational Resources**: Analyzing large gene families or many species may require significant memory.

- **Parameter Tuning**: Adjust parameters based on your specific dataset characteristics.

## Examples

### Basic polyploidy analysis
**Args:** `grampa analyze -g gene_trees/ -s species_tree.nwk -o results.txt`
**Explanation:** Identifies polyploidy events from gene trees and species tree.

### Include synteny information
**Args:** `grampa analyze -g gene_trees/ -s species_tree.nwk -y synteny.txt -o results.txt`
**Explanation:** Incorporates synteny information for improved polyploidy detection.

### Count duplications and losses
**Args:** `grampa count -g gene_trees/ -s species_tree.nwk -o counts.txt`
**Explanation:** Counts gene duplications and losses accounting for polyploidy.

### Generate visualization
**Args:** `grampa plot -i results.txt -o polyploidy_plot.png`
**Explanation:** Creates a visualization of polyploidy events on the phylogeny.

### Specify outgroup
**Args:** `grampa analyze -g gene_trees/ -s species_tree.nwk -r outgroup -o results.txt`
**Explanation:** Specifies an outgroup for rooting the analysis.

### Batch processing
**Args:** `grampa batch -g gene_trees_dir/ -s species_tree.nwk -o results/`
**Explanation:** Processes multiple gene tree files in a directory.

### Detailed output
**Args:** `grampa analyze -g gene_trees/ -s species_tree.nwk -v -o results.txt`
**Explanation:** Provides verbose output with detailed analysis information.