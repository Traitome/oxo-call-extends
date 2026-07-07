---
name: phylodeep
category: population-genomics
description: phylodeep performs deep-learning parameter estimation from phylogenetic trees.
tags: [phylodeep, population-genomics, deep-learning, phylogeny]
author: oxo-call-community
source_url: "https://github.com/evolbioinfo/phylodeep"
---

## Concepts

- **Tool Overview**: phylodeep estimates parameters from trees.
- **Core Function**: Deep-learning phylogenetic analysis.
- **Algorithm**: Uses deep learning methods.
- **Input Format**: Accepts phylogenetic tree files.
- **Output**: Produces parameter estimation results.
- **Use Case**: Phylogenetics, deep learning analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on tree quality.
- **Deep Learning**: May have prediction errors.
- **Runtime**: Estimation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylodeep --help`
**Explanation:** Shows available options and usage instructions.

### Estimate parameters
**Args:** `phylodeep -i phylogeny_tree.newick -o parameter_estimates.txt`
**Explanation:** Estimates parameters from tree.

### With parameters
**Args:** `phylodeep -i phylogeny_tree.newick -p params.yaml -o parameter_estimates.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylodeep -v -i phylogeny_tree.newick -o parameter_estimates.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylodeep -t 4 -i phylogeny_tree.newick -o parameter_estimates.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylodeep -i phylogeny_tree.newick -o parameter_estimates.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylodeep -i phylogeny_tree.newick -o parameter_estimates.txt --report report.html`
**Explanation:** Generates HTML report.