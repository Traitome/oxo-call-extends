---
name: pargenes
category: population-genomics
description: ParGenes performs parallel model selection and tree inference on thousands of genes.
tags: [pargenes, population-genomics, phylogenetics, tree-inference]
author: oxo-call-community
source_url: "https://github.com/BenoitMorel/ParGenes"
---

## Concepts

- **Tool Overview**: ParGenes performs large-scale phylogenetic analysis.
- **Core Function**: Conducts model selection and tree inference.
- **Algorithm**: Uses RAxML and IQ-TREE for parallel analysis.
- **Input Format**: Accepts multiple sequence alignments.
- **Output**: Produces phylogenetic trees and statistics.
- **Use Case**: Comparative genomics, phylogenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Dependency Management**: Requires RAxML/IQ-TREE.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pargenes --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pargenes -a alignments/ -o trees/`
**Explanation:** Performs tree inference on alignments.

### With model selection
**Args:** `pargenes -a alignments/ -o trees/ --model-selection`
**Explanation:** Includes model selection step.

### Verbose mode
**Args:** `pargenes -v -a alignments/ -o trees/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pargenes -t 16 -a alignments/ -o trees/`
**Explanation:** Uses 16 threads for parallel processing.

### Use IQ-TREE
**Args:** `pargenes -a alignments/ -o trees/ --iqtree`
**Explanation:** Uses IQ-TREE instead of RAxML.

### Bootstrap replicates
**Args:** `pargenes -a alignments/ -o trees/ --bootstrap 100`
**Explanation:** Performs 100 bootstrap replicates.