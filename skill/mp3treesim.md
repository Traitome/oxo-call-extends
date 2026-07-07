---
name: mp3treesim
category: utility
description: Triplet-based similarity score for multi-labeled trees with poly-occurring labels.
tags: [mp3treesim, utility, phylogenetics]
author: oxo-call-community
source_url: "https://algolab.github.io/mp3treesim/"
---

## Concepts

- **Tool Overview**: MP3TreeSim v1.0.6 calculates similarity between multi-labeled trees.
- **Core Function**: Computes triplet-based similarity scores.
- **Multi-labeled Trees**: Handles trees with poly-occurring labels.
- **Triplet Comparison**: Uses triplet-based tree comparison.
- **Phylogenetic Analysis**: Supports phylogenetic tree comparison.
- **Input/Output**: Accepts tree files; outputs similarity scores.

## Pitfalls

- **Tree Format**: Requires specific tree file formats.
- **Memory Requirements**: Memory usage depends on tree complexity.
- **Parameter Tuning**: May require parameter adjustment for scoring.
- **Tree Quality**: Results depend on input tree quality.
- **Computational Resources**: Large trees may require significant resources.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Compute tree similarity
**Args:** `mp3treesim -t1 tree1.newick -t2 tree2.newick -o score.txt`
**Explanation:** Calculates similarity between two trees.

### With multiple trees
**Args:** `mp3treesim -i trees/ -o scores.txt`
**Explanation:** Compares multiple trees.

### Generate distance matrix
**Args:** `mp3treesim -i trees/ -m -o distance_matrix.txt`
**Explanation:** Generates pairwise distance matrix.

### Verbose output
**Args:** `mp3treesim -t1 tree1.newick -t2 tree2.newick -v -o score.txt`
**Explanation:** Shows detailed comparison results.

### With custom parameters
**Args:** `mp3treesim -t1 tree1.newick -t2 tree2.newick -p params.yaml -o score.txt`
**Explanation:** Uses custom scoring parameters.