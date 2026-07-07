---
name: apu-label-propagation
category: machine-learning
description: APU - Adaptive Positive-Unlabelled label propagation for disease gene identification
tags: [apu-label-propagation, PU-learning, disease-genes, machine-learning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/AndMastro/NIAPU"
---

## Concepts

- **Tool Overview**: apu-label-propagation (v1.2) - A component of the NIAPU framework for adaptive Positive-Unlabelled (PU) label propagation, designed for disease gene identification.
- **Core Function**: Implements a Markov diffusion-based multi-class labelling strategy to identify candidate disease genes from positive and unlabelled data.
- **Positive-Unlabelled Learning**: A machine learning paradigm where only a subset of instances are labelled as positive, while the rest are unlabelled.
- **NIAPU Framework**: Consists of two components - NeDBIT (Network diffusion and biology-informed topological) features computation and APU label propagation.
- **Multi-class Labelling**: Assigns labels including Positive (P), Likely Positive (LP), Weakly Negative (WN), Likely Negative (LN), and Reliable Negative (RN).
- **Applications**: Disease gene prioritization, gene-disease association discovery
- **Installation**: `conda install -c bioconda apu-label-propagation`

## Pitfalls

- **Feature Requirements**: Requires NeDBIT features as input; cannot run standalone without proper feature computation
- **Header Presence**: Must specify whether input file has header (0/1 boolean)
- **Parameter Tuning**: Requires careful selection of quantile thresholds for weak link removal and Reliable Negative computation
- **Network Data**: Depends on PPI (Protein-Protein Interaction) network data for feature computation
- **Compilation**: May require compilation from source for full functionality

## Examples

### Basic label propagation
**Args:** `apu_label_propagation nedbit_features.txt 1 output_ranking.txt 0.1 0.9`
**Explanation:** Runs APU label propagation with NeDBIT features file (with header), output ranking, 0.1 quantile for weak links, and 0.9 quantile for Reliable Negative computation.

### Without header
**Args:** `apu_label_propagation features_no_header.txt 0 results.txt 0.05 0.95`
**Explanation:** Processes feature file without header using different quantile thresholds.

### Help documentation
**Args:** `apu_label_propagation --help`
**Explanation:** Shows available options and parameters.

### Full NIAPU pipeline
**Args:** First compute NeDBIT features, then run APU: `nedbit_features_calculator ppi_links.txt seed_genes.txt features.txt && apu_label_propagation features.txt 1 output.txt 0.1 0.9`
**Explanation:** Complete pipeline for disease gene identification.