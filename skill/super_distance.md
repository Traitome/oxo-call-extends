---
name: super_distance
category: population-genomics
description: Supertree method with distances for phylogenetic analysis.
tags: [super_distance, supertree, phylogenetics, distance-matrix]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/super_distance"
---

## Concepts

- **Tool Overview**: super_distance (v1.1.0) implements supertree methods with distance matrices.
- **Core Function**: Constructs supertrees from multiple phylogenetic trees using distance methods.
- **Algorithm**: Uses distance-based supertree construction algorithms.
- **Input/Output**: Input: Phylogenetic trees or distance matrices; Output: Supertree.
- **Applications**: Phylogenetics, evolutionary biology, species tree reconstruction.
- **Installation**: `conda install -c bioconda super_distance` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific tree or matrix format.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Supertree construction can be slow.
- **Parameter Tuning**: Incorrect parameters affect tree topology.
- **Tree Quality**: Poor quality input trees affect results.
- **Distance Metrics**: Choice of distance metric affects outcomes.

## Examples

### Display help
**Args:** `super_distance --help`
**Explanation:** Shows available options and usage information.

### Basic supertree construction
**Args:** `super_distance -i trees.tre -o supertree.tre`
**Explanation:** Construct supertree from multiple input trees.

### With distance matrix
**Args:** `super_distance -i distances.txt -o supertree.tre --matrix`
**Explanation:** Use distance matrix as input.

### Verbose mode
**Args:** `super_distance -i trees.tre -o supertree.tre -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `super_distance -i trees.tre -o supertree.tre --stats`
**Explanation:** Generate statistics about supertree.

### Batch processing
**Args:** `super_distance -i trees/ -o results/`
**Explanation:** Process multiple tree files together.

### Filter by support
**Args:** `super_distance -i trees.tre -o supertree.tre -s 0.8`
**Explanation:** Filter trees by support threshold.

### Include bootstrap
**Args:** `super_distance -i trees.tre -o supertree.tre --bootstrap`
**Explanation:** Include bootstrap values in output.

### Generate report
**Args:** `super_distance -i trees.tre -o supertree.tre --report`
**Explanation:** Generate comprehensive HTML report.
