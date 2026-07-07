---
name: newick_utils
category: utility
description: Newick Utilities are Unix shell tools for processing and manipulating phylogenetic trees in Newick format.
tags: [newick_utils, utility, phylogenetics, tree, bioinformatics]
author: oxo-call-community
source_url: "http://cegg.unige.ch/newick_utils"
---

## Concepts

- **Tool Overview**: Newick Utilities provides command-line tools for phylogenetic tree manipulation.
- **Core Function**: Processes Newick format trees with various operations.
- **Algorithm**: Parses Newick format and applies tree operations.
- **Input Format**: Accepts Newick format tree files.
- **Output**: Produces modified trees or tree statistics.
- **Use Case**: Phylogenetic analysis, tree visualization, and evolutionary biology research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Format Compatibility**: Requires standard Newick format.
- **Tree Size**: Very large trees may cause performance issues.
- **Memory Usage**: Complex tree operations require memory.
- **Error Handling**: Poorly formatted trees may cause errors.
- **Visualization Limitations**: ASCII graphics have resolution limits.

## Examples

### Display help
**Args:** `nw_display --help`
**Explanation:** Shows available options and usage instructions.

### Display tree
**Args:** `nw_display tree.nw`
**Explanation:** Displays tree in ASCII format.

### Re-root tree
**Args:** `nw_reroot tree.nw outgroup > rooted.nw`
**Explanation:** Re-roots tree at specified outgroup.

### Extract subtree
**Args:** `nw_clade tree.nw species1 species2 > subtree.nw`
**Explanation:** Extracts subtree containing specified species.

### Prune tree
**Args:** `nw_prune tree.nw species_to_remove > pruned.nw`
**Explanation:** Removes specified species from tree.

### Draw SVG
**Args:** `nw_svg tree.nw > tree.svg`
**Explanation:** Generates SVG visualization of tree.

### Statistics
**Args:** `nw_stats tree.nw`
**Explanation:** Outputs tree statistics.