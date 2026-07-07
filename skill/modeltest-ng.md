---
name: modeltest-ng
category: alignment
description: ModelTest-NG is a tool for selecting the best-fit model of evolution for DNA and protein alignments.
tags: [modeltest-ng, alignment, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/ddarriba/modeltest"
---

## Concepts

- **Tool Overview**: ModelTest-NG v0.1.7 selects best-fit evolutionary models for sequence alignments.
- **Core Function**: Identifies optimal substitution models for phylogenetic analysis.
- **Model Selection**: Evaluates multiple evolutionary models using statistical criteria.
- **DNA/Protein Support**: Works with both DNA and protein sequence alignments.
- **Input/Output**: Accepts FASTA alignments; outputs best-fit model.
- **Phylogenetics**: Supports downstream phylogenetic tree inference.

## Pitfalls

- **Alignment Required**: Requires pre-aligned sequences.
- **Memory Requirements**: Memory usage depends on alignment size.
- **Parameter Tuning**: May require parameter adjustment for model evaluation.
- **Data Quality**: Results depend on alignment quality.
- **Computational Resources**: Model testing may require significant resources.
- **Model Assumptions**: Relies on evolutionary model assumptions.

## Examples

### Select best model
**Args:** `modeltest-ng -i alignment.fasta -o model_result.txt`
**Explanation:** Selects best-fit evolutionary model for alignment.

### For protein sequences
**Args:** `modeltest-ng -i protein_alignment.fasta -p -o model_result.txt`
**Explanation:** Evaluates protein substitution models.

### With AIC criterion
**Args:** `modeltest-ng -i alignment.fasta -c aic -o model_result.txt`
**Explanation:** Uses Akaike Information Criterion.

### With BIC criterion
**Args:** `modeltest-ng -i alignment.fasta -c bic -o model_result.txt`
**Explanation:** Uses Bayesian Information Criterion.

### Batch processing
**Args:** `modeltest-ng -i fasta/ -o results/`
**Explanation:** Processes multiple alignment files.