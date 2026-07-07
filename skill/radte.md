---
name: radte
category: utility
description: RADTE (Reconciliation-Assisted Divergence Time Estimation) estimates divergence times for gene families using phylogenetic reconciliation.
tags: [radte, utility, divergence-time, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/kfuku52/radte"
---

## Concepts

- **Tool Overview**: radte estimates divergence times.
- **Core Function**: Divergence time estimation.
- **Algorithm**: Uses reconciliation methods.
- **Input Format**: Accepts gene trees.
- **Output**: Produces time estimates.
- **Use Case**: Evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Tree Quality**: Affects estimation.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `radte --help`
**Explanation:** Shows available options and usage instructions.

### Estimate times
**Args:** `radte estimate -i gene_tree.newick -o times.txt`
**Explanation:** Estimates divergence times.

### With parameters
**Args:** `radte estimate -i gene_tree.newick -p params.yaml -o times.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `radte -v estimate -i gene_tree.newick -o times.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `radte -t 4 estimate -i gene_tree.newick -o times.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With species tree
**Args:** `radte estimate -i gene_tree.newick -s species_tree.newick -o times.txt`
**Explanation:** Uses species tree for reconciliation.

### Generate report
**Args:** `radte estimate -i gene_tree.newick -o times.txt --report report.html`
**Explanation:** Generates HTML report.