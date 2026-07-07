---
name: rapidnj
category: programming
description: RapidNJ is an algorithmic engineered implementation of canonical neighbour-joining for phylogenetic tree construction.
tags: [rapidnj, programming, phylogenetics, neighbor-joining]
author: oxo-call-community
source_url: "https://github.com/somme89/rapidNJ/blob/master/README"
---

## Concepts

- **Tool Overview**: rapidnj builds trees.
- **Core Function**: Phylogenetic tree construction.
- **Algorithm**: Uses neighbor-joining.
- **Input Format**: Accepts distance matrices.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large matrices require memory.
- **Matrix Quality**: Affects tree building.
- **Parameters**: Must be configured.
- **Runtime**: Tree building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapidnj --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `rapidnj build -i distance_matrix.txt -o tree.newick`
**Explanation:** Builds phylogenetic tree.

### With parameters
**Args:** `rapidnj build -i distance_matrix.txt -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapidnj -v build -i distance_matrix.txt -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapidnj -t 4 build -i distance_matrix.txt -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With bootstrapping
**Args:** `rapidnj build -i distance_matrix.txt -b 100 -o tree.newick`
**Explanation:** Uses 100 bootstrap replicates.

### Generate report
**Args:** `rapidnj build -i distance_matrix.txt -o tree.newick --report report.html`
**Explanation:** Generates HTML report.