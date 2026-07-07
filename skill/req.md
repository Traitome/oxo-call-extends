---
name: req
category: utility
description: REQ estimates the rate of elementary quartets for assessing branch supports in phylogenetic trees.
tags: [req, utility, phylogenetics, branch-support]
author: oxo-call-community
source_url: "https://research.pasteur.fr/fr/tool/r%CE%B5q-assessing-branch-supports-o%C6%92-a-distance-based-phylogenetic-tree-with-the-rate-o%C6%92-elementary-quartets/"
---

## Concepts

- **Tool Overview**: req assesses branch support.
- **Core Function**: Quartet-based branch support.
- **Algorithm**: Uses distance matrix methods.
- **Input Format**: Accepts distance matrices.
- **Output**: Produces support values.
- **Use Case**: Phylogenetic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Matrix Quality**: Affects assessment.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `req --help`
**Explanation:** Shows available options and usage instructions.

### Analyze tree
**Args:** `req -i distance.matrix -t tree.nwk -o supports.txt`
**Explanation:** Estimates branch supports from distance matrix.

### With parameters
**Args:** `req -i distance.matrix -p params.yaml -o supports.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `req -v -i distance.matrix -o supports.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `req -t 4 -i distance.matrix -o supports.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With bootstrap
**Args:** `req -i distance.matrix -b 100 -o supports.txt`
**Explanation:** Uses 100 bootstrap replicates.

### Generate report
**Args:** `req -i distance.matrix -o supports.txt --report report.html`
**Explanation:** Generates HTML report.