---
name: intarna
category: rna-analysis
description: Efficient RNA-RNA interaction prediction tool incorporating accessibility of interacting sites and seed region constraints.
tags: [intarna, rna-analysis, rna-rna-interaction, target-prediction]
author: oxo-call-community
source_url: "https://backofenlab.github.io/IntaRNA"
---

## Concepts

- **RNA-RNA Interaction Prediction**: IntaRNA predicts interactions between two RNA molecules using energy-based approaches.
- **Accessibility Integration**: Incorporates accessibility of interaction sites by calculating free energy required to unfold secondary structures.
- **Seed Region Constraints**: Requires user-definable seed regions with near-perfect complementarity to initiate interactions.
- **Energy Calculation**: Combines hybridization free energy with accessibility free energy for accurate scoring.
- **Dynamic Programming**: Uses dynamic programming for efficient prediction of optimal interactions.

## Pitfalls

- **Parameter Tuning**: Seed region parameters may need adjustment based on specific RNA types.
- **Computational Complexity**: Genome-wide searches can be computationally intensive.
- **Energy Thresholds**: Default energy thresholds may need adjustment for specific applications.
- **Input Format**: Requires proper FASTA format with valid RNA sequences (A, C, G, U).
- **Memory Usage**: Large RNA sequences may require significant memory resources.

## Examples

### Basic RNA-RNA interaction prediction
**Args:** `IntaRNA -q query.fa -t target.fa -o interactions.tsv`
**Explanation:** Predicts interactions between query and target RNA sequences.

### With custom seed parameters
**Args:** `IntaRNA -q sRNA.fa -t mRNA.fa -o results.tsv --seed-minBP 7 --seed-maxUP 2`
**Explanation:** Sets minimum 7 base pairs and maximum 2 unpaired bases in seed region.

### Genome-wide target prediction
**Args:** `IntaRNA -q sRNA.fa -t genome.fa -o genome_targets.tsv --threads 8`
**Explanation:** Searches for targets across entire genome using 8 threads.

### Output detailed interaction information
**Args:** `IntaRNA -q query.fa -t target.fa -o detailed.tsv --outMode=detail`
**Explanation:** Generates detailed output with interaction positions and energies.

### Filter by energy threshold
**Args:** `IntaRNA -q query.fa -t target.fa -o filtered.tsv --maxE -15`
**Explanation:** Only reports interactions with energy ≤ -15 kcal/mol.

### Use accessibility data from probing
**Args:** `IntaRNA -q query.fa -t target.fa -o results.tsv --acc-probing target_probing.txt`
**Explanation:** Incorporates experimental probing data for improved target prediction.