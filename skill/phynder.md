---
name: phynder
category: population-genomics
description: phynder places samples into phylogenetic trees using likelihood calculations.
tags: [phynder, population-genomics, likelihood, placement]
author: oxo-call-community
source_url: "https://github.com/richarddurbin/phynder"
---

## Concepts

- **Tool Overview**: phynder places samples in phylogenetic trees.
- **Core Function**: Likelihood-based sample placement.
- **Algorithm**: Uses efficient likelihood calculations.
- **Input Format**: Accepts phylogenetic tree files.
- **Output**: Produces sample placement results.
- **Use Case**: Phylogenetics, sample placement.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on tree quality.
- **Missing Data**: High missing data rates affect results.
- **Runtime**: Placement may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phynder --help`
**Explanation:** Shows available options and usage instructions.

### Place samples
**Args:** `phynder -i phylogenetic_tree.newick -s samples.txt -o placement_results.txt`
**Explanation:** Places samples into phylogenetic tree.

### With parameters
**Args:** `phynder -i phylogenetic_tree.newick -s samples.txt -p params.yaml -o placement_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phynder -v -i phylogenetic_tree.newick -s samples.txt -o placement_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phynder -t 4 -i phylogenetic_tree.newick -s samples.txt -o placement_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phynder -i phylogenetic_tree.newick -s samples.txt -o placement_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phynder -i phylogenetic_tree.newick -s samples.txt -o placement_results.txt --report report.html`
**Explanation:** Generates HTML report.