---
name: phylorank
category: population-genomics
description: phylorank calculates relative evolutionary divergence of taxa.
tags: [phylorank, population-genomics, red, taxonomy]
author: oxo-call-community
source_url: "https://github.com/dparks1134/PhyloRank"
---

## Concepts

- **Tool Overview**: phylorank calculates evolutionary divergence.
- **Core Function**: Relative evolutionary divergence analysis.
- **Algorithm**: Uses phylogenetic tree analysis.
- **Input Format**: Accepts phylogenetic tree files.
- **Output**: Produces RED calculation results.
- **Use Case**: Phylogenetics, taxonomy placement.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on tree quality.
- **RED Calculation**: May have calculation errors.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylorank --help`
**Explanation:** Shows available options and usage instructions.

### Calculate RED
**Args:** `phylorank -i phylogenetic_tree.newick -o red_results.txt`
**Explanation:** Calculates relative evolutionary divergence.

### With parameters
**Args:** `phylorank -i phylogenetic_tree.newick -p params.yaml -o red_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylorank -v -i phylogenetic_tree.newick -o red_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylorank -t 4 -i phylogenetic_tree.newick -o red_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylorank -i phylogenetic_tree.newick -o red_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylorank -i phylogenetic_tree.newick -o red_results.txt --report report.html`
**Explanation:** Generates HTML report.