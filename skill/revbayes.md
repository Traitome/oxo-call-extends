---
name: revbayes
category: utility
description: RevBayes performs Bayesian phylogenetic inference using graphical models.
tags: [revbayes, utility, phylogenetics, bayesian-inference]
author: oxo-call-community
source_url: "https://revbayes.github.io/tutorials"
---

## Concepts

- **Tool Overview**: revbayes infers phylogenies.
- **Core Function**: Bayesian phylogenetic inference.
- **Algorithm**: Uses MCMC methods.
- **Input Format**: Accepts sequence data.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Phylogenetic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Chain Convergence**: Must be monitored.
- **Parameters**: Must be configured.
- **Runtime**: Inference may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rb -h`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `rb script.Rev`
**Explanation:** Runs RevBayes analysis script.

### With parameters
**Args:** `rb -p params.Rev script.Rev`
**Explanation:** Uses parameter file.

### Verbose mode
**Args:** `rb -v script.Rev`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rb -n 4 script.Rev`
**Explanation:** Uses 4 threads for parallel processing.

### With seed
**Args:** `rb -s 12345 script.Rev`
**Explanation:** Sets random seed.

### Generate tree
**Args:** `rb -o tree.nwk script.Rev`
**Explanation:** Outputs tree to file.