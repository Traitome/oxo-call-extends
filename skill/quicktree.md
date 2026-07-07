---
name: quicktree
category: utility
description: QuickTree provides fast implementation of the neighbor-joining phylogenetic inference method.
tags: [quicktree, utility, phylogenetics, tree-building]
author: oxo-call-community
source_url: "https://github.com/khowe/quicktree"
---

## Concepts

- **Tool Overview**: quicktree builds phylogenetic trees.
- **Core Function**: Tree inference.
- **Algorithm**: Uses Neighbor-Joining.
- **Input Format**: Accepts distance matrices.
- **Output**: Produces tree files.
- **Use Case**: Evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Distance Matrix**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Inference may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quicktree --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `quicktree -i distance.txt -o tree.newick`
**Explanation:** Builds Neighbor-Joining tree.

### With parameters
**Args:** `quicktree -i distance.txt -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quicktree -v -i distance.txt -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quicktree -t 4 -i distance.txt -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With outgroup
**Args:** `quicktree -i distance.txt -o tree.newick -O outgroup`
**Explanation:** Root tree with outgroup.

### Generate report
**Args:** `quicktree -i distance.txt -o tree.newick --report report.html`
**Explanation:** Generates HTML report.