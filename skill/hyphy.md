---
name: hyphy
category: phylogenetics
description: HyPhy - Hypothesis Testing using Phylogenies for molecular evolution analysis
tags: [hyphy, phylogenetics, molecular evolution, selection analysis]
author: oxo-call-community
source_url: "https://hyphy.org"
---

## Concepts

- **Tool Overview**: HyPhy is an open-source software package for comparative sequence analysis using stochastic evolutionary models.
- **Markov Models**: Implements continuous-time, discrete-state Markov models for sequence evolution.
- **Selection Detection**: Provides multiple methods for detecting positive and purifying selection (FEL, FUBAR, MEME, SLAC).
- **dN/dS Analysis**: Specializes in codon-based analyses to detect selection pressure.
- **Custom Models**: Supports user-defined evolutionary models via the HyPhy Batch Language (HBL).
- **Installation**: `conda install -c bioconda hyphy`

## Pitfalls

- **Input Format**: Requires properly formatted sequence alignments and phylogenetic trees.
- **Computational Resources**: Complex analyses can be computationally intensive.
- **Model Selection**: Choice of evolutionary model significantly impacts results.
- **Alignment Quality**: Poor alignments can lead to incorrect inference.
- **Branch Length**: Short branches may not contain enough information for reliable inference.
- **Recombination**: Recombination can violate model assumptions; use GARD for detection.

## Examples

### Detect pervasive selection with FUBAR
**Args:** `hyphy fubar --alignment align.fasta --tree tree.nwk --output results.json`
**Explanation:** Runs FUBAR analysis to detect pervasive selection at sites.

### Detect episodic selection with MEME
**Args:** `hyphy meme --alignment align.fasta --tree tree.nwk --output meme_results.json`
**Explanation:** Uses MEME to detect episodic positive selection on specific branches.

### Basic MG94 model fit
**Args:** `hyphy FitMG94 --alignment align.fasta --tree tree.nwk`
**Explanation:** Fits the Muse-Gaut 94 codon model to sequence data.

### Site model analysis
**Args:** `hyphy fel --alignment align.fasta --tree tree.nwk --output fel_results.json`
**Explanation:** Uses Fixed Effects Likelihood to detect selection at individual sites.

### Check for recombination with GARD
**Args:** `hyphy gard --alignment align.fasta --output recombination.json`
**Explanation:** Detects recombination breakpoints before selection analysis.