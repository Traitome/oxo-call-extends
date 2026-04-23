---
name: booster
category: utility
description: Computing bootstrap supports in large phylogenies
tags: [booster, phylogenetics, bootstrap, tree]
author: oxo-call-community
source_url: "https://github.com/evolbioinfo/booster"
---

## Concepts

- **Tool Overview**: BOOSTER computes bootstrap supports in large phylogenies using a novel approach.
- **Core Function**: Re-assigns bootstrap supports to branches of a reference tree using transfer distance.
- **Input**: Reference tree (Newick) and bootstrap tree files.
- **Output**: Reference tree with updated bootstrap support values.
- **Advantage**: More accurate than standard bootstrap for large datasets.
- **Installation**: Install via bioconda: `conda install -c bioconda booster`

## Pitfalls

- **Tree Format**: Input trees must be in Newick format with consistent taxon names.
- **Rooted Trees**: Both reference and bootstrap trees should be rooted consistently.
- **Branch Lengths**: Branch lengths in bootstrap trees are not used; only topology matters.
- **Memory Usage**: Large tree collections require significant memory.

## Examples

### Compute bootstrap supports
**Args:** `booster -i reference.tree -b bootstrap_trees.nwk -o supported.tree`
**Explanation:** Computes transfer bootstrap supports for reference tree branches.

### Specify number of threads
**Args:** `booster -i ref.tree -b boot.trees -t 4 -o supported.tree`
**Explanation:** Uses 4 threads for parallel support computation.

### Silent mode
**Args:** `booster -i ref.tree -b boot.trees -o supported.tree -s`
**Explanation:** Runs in silent mode with minimal output.

### Output supports as CSV
**Args:** `booster -i ref.tree -b boot.trees -o supported.tree -c supports.csv`
**Explanation:** Also outputs branch support values as CSV for further analysis.
