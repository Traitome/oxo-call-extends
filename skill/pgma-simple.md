---
name: pgma-simple
category: utility
description: pgma-simple builds WPGMA trees from distance matrices.
tags: [pgma-simple, utility, phylogeny, wpgma]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/GraphClust"
---

## Concepts

- **Tool Overview**: pgma-simple builds phylogenetic trees.
- **Core Function**: Uses WPGMA clustering algorithm.
- **Algorithm**: Weighted Pair Group Method with Arithmetic mean.
- **Input Format**: Accepts distance matrix files.
- **Output**: Produces phylogenetic tree structures.
- **Use Case**: Phylogenetic analysis, tree construction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large matrices require memory.
- **Distance Format**: Requires proper distance matrix format.
- **Tree Quality**: Results depend on distance accuracy.
- **Runtime**: Building may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgma-simple --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `pgma-simple -i distances.txt -o tree.nwk`
**Explanation:** Builds WPGMA tree from distance matrix.

### With format
**Args:** `pgma-simple -i distances.txt -f phylip -o tree.nwk`
**Explanation:** Uses specific input format.

### Verbose mode
**Args:** `pgma-simple -v -i distances.txt -o tree.nwk`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgma-simple -t 4 -i distances.txt -o tree.nwk`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pgma-simple -i distances.txt -o tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `pgma-simple -i distances.txt -o tree.nwk --report report.html`
**Explanation:** Generates HTML report.