---
name: dawg
category: variant-calling
description: Dawg - DNA Assembly with Gaps - simulates recombinant DNA sequence evolution
tags: [dawg, variant-calling, simulation, molecular-evolution, recombination]
author: oxo-call-community
source_url: "https://github.com/reedacartwright/dawg"
---

## Concepts

- **Tool Overview**: dawg (v2.0.beta1+) simulates the evolution of recombinant DNA sequences using the general time reversible model.
- **Core Function**: Simulates DNA sequence evolution with recombination, gap formation, and rate heterogeneity.
- **Input/Output**: Input: Ancestral sequence, model parameters. Output: Simulated sequences, evolutionary history.
- **Algorithm**: Uses continuous-time Markov chain with gamma and invariant rate heterogeneity.
- **Key Features**: Recombination simulation, length-dependent gaps, population genetics.
- **Installation**: `conda install -c bioconda dawg`

## Pitfalls

- **Parameter Complexity**: Requires careful parameter specification for realistic simulations.
- **Computational Time**: Complex simulations may be computationally intensive.
- **Memory Usage**: Large populations or long sequences require significant memory.
- **Model Assumptions**: Results depend on model assumptions and parameter choices.
- **Validation**: Simulated data should be validated against expectations.

## Examples

### Simulate sequence evolution
**Args:** `dawg -i ancestral.fasta -o simulated.fasta -t 100`
**Explanation:** Simulate 100 generations of sequence evolution.

### Include recombination
**Args:** `dawg -i ancestral.fasta -o simulated.fasta -r 0.01 -t 100`
**Explanation:** Simulate with recombination rate of 0.01 per generation.

### Use gamma rate heterogeneity
**Args:** `dawg -i ancestral.fasta -o simulated.fasta -g 4.0 -t 100`
**Explanation:** Simulate with gamma rate heterogeneity (shape=4.0).
