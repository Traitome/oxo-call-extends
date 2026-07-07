---
name: nwkit
category: phylogenetics
description: nwkit provides tools for processing and manipulating Newick-format phylogenetic trees.
tags: [nwkit, phylogenetics, tree-manipulation, newick]
author: oxo-call-community
source_url: "https://github.com/kfuku52/nwkit"
---

## Concepts

- **Tool Overview**: nwkit processes and manipulates phylogenetic trees in Newick format.
- **Core Function**: Provides utilities for tree operations and analysis.
- **Algorithm**: Parses and manipulates tree data structures.
- **Input Format**: Accepts Newick tree files.
- **Output**: Produces modified trees and tree statistics.
- **Use Case**: Phylogenetic analysis, tree visualization, and evolutionary studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Tree Format**: Requires proper Newick format.
- **Memory Usage**: Large trees require memory.
- **Complex Trees**: May not handle extremely complex trees well.
- **Validation**: Results should be validated for correctness.
- **Documentation**: Limited documentation available.

## Examples

### Display help
**Args:** `nwkit --help`
**Explanation:** Shows available options and usage instructions.

### Print tree
**Args:** `nwkit show -i tree.nwk`
**Explanation:** Displays tree structure.

### Root tree
**Args:** `nwkit root -i tree.nwk -o rooted.nwk --outgroup taxonA`
**Explanation:** Roots tree with specified outgroup.

### Prune taxa
**Args:** `nwkit prune -i tree.nwk -o pruned.nwk --taxa taxa.txt`
**Explanation:** Removes specified taxa from tree.

### Rename taxa
**Args:** `nwkit rename -i tree.nwk -o renamed.nwk --map names.txt`
**Explanation:** Renames taxa using mapping file.

### Compute statistics
**Args:** `nwkit stats -i tree.nwk`
**Explanation:** Computes tree statistics.

### Convert format
**Args:** `nwkit convert -i tree.nwk -o tree.nexus --format nexus`
**Explanation:** Converts tree to Nexus format.

### Verbose mode
**Args:** `nwkit show -i tree.nwk -v`
**Explanation:** Runs with verbose output.