---
name: gappa
category: utility
description: Genesis Applications for Phylogenetic Placement Analysis.
tags: [gappa, phylogenetics, phylogenetic placement, EPA-ng]
author: oxo-call-community
source_url: "https://github.com/lczech/gappa"
---

## Concepts
- **Phylogenetic Placement**: Places short sequences on reference trees.
- **Jplace Format**: Works with jplace format files.
- **Tree Analysis**: Analyzes phylogenetic tree structures.
- **EPA-ng Integration**: Integrates with EPA-ng for placement.
- **Statistical Analysis**: Provides statistical analysis of placements.

## Pitfalls
- **Tree Quality**: Results depend on reference tree quality.
- **Jplace Format**: Requires proper jplace format.
- **Computational Time**: Large datasets can be slow.
- **Memory Usage**: High memory for large analyses.
- **Parameter Selection**: Requires careful parameter selection.

## Examples
### Examine placement
**Args:** `gappa examine --jplace placements.jplace -o results/`
**Explanation:** Examines phylogenetic placements.

### Assign taxonomy
**Args:** `gappa assign --jplace placements.jplace --taxonomy taxonomy.tsv -o assigned/`
**Explanation:** Assigns taxonomy to placed sequences.

### Draw tree
**Args:** `gappa draw --jplace placements.jplace --tree tree.nwk -o tree.png`
**Explanation:** Generates tree visualization.

### Analyze redundancy
**Args:** `gappa analyze redundancy --jplace placements.jplace -o redundancy.txt`
**Explanation:** Analyzes placement redundancy.

### Export results
**Args:** `gappa export --jplace placements.jplace --format csv -o results.csv`
**Explanation:** Exports results to CSV format.