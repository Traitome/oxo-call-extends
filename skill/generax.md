---
name: generax
category: phylogenetics
description: GeneRax - A parallel tool for species tree-aware maximum likelihood based gene tree inference under gene duplication, transfer, and loss.
tags: [generax, gene-tree, phylogenetics, duplication-transfer-loss]
author: oxo-call-community
source_url: "https://github.com/benoitmorel/generax"
---

## Concepts
- **Gene Tree Inference**: Infers gene trees from sequence alignments.
- **Species Tree-Aware**: Considers species tree in gene tree inference.
- **Maximum Likelihood**: Uses ML-based methods for tree inference.
- **Duplication-Transfer-Loss**: Models gene family evolution with DTL.
- **Parallel Computing**: Supports parallel computation for scalability.

## Pitfalls
- **Computational Resources**: Requires significant computational resources.
- **Memory Usage**: Large datasets require sufficient memory.
- **Species Tree Quality**: Depends on accurate species tree.
- **Alignment Quality**: Requires high-quality sequence alignments.
- **Parameter Tuning**: DTL parameters require careful adjustment.

## Examples
### Infer gene trees
**Args:** `generax --families families.txt --species-tree species.nwk --output results/`
**Explanation:** Infers gene trees using species tree-aware approach.

### With DTL model
**Args:** `generax --families families.txt --species-tree species.nwk --model DTL --output results/`
**Explanation:** Uses duplication-transfer-loss model.

### Parallel execution
**Args:** `generax --families families.txt --species-tree species.nwk --threads 16 --output results/`
**Explanation:** Uses 16 threads for parallel computation.

### Bootstrap analysis
**Args:** `generax --families families.txt --species-tree species.nwk --bootstrap 100 --output results/`
**Explanation:** Performs bootstrap analysis with 100 replicates.

### Generate reconciliation
**Args:** `generax --families families.txt --species-tree species.nwk --reconcile --output results/`
**Explanation:** Generates gene-species tree reconciliation.