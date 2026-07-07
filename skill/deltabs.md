---
name: deltabs
category: population-genomics
description: deltaBS - quantifying the significance of genetic variation using probabilistic profile-based methods.
tags: [deltabs, population-genomics, genetic-variation, probabilistic]
author: oxo-call-community
source_url: "https://github.com/UCanCompBio/deltaBS/wiki"
---

## Concepts

- **Tool Overview**: deltaBS is a tool for quantifying the significance of genetic variation using probabilistic profile-based methods. It compares observed variation against background expectations.
- **Core Function**: Evaluates whether observed genetic variation in a sequence alignment deviates significantly from neutral expectations, aiding in detecting selection or functional constraints.
- **Input/Output**: Input: Multiple sequence alignments, probabilistic profiles. Output: Significance scores, p-values, variation statistics.
- **Algorithm**: Uses hidden Markov models (HMMs) and probabilistic profiles to model background variation and detect significant deviations.
- **Key Features**: Probabilistic framework, handles multiple sequence alignments, detects selection signatures, statistical significance testing, batch processing.
- **Installation**: `conda install -c bioconda deltabs`

## Pitfalls

- **Alignment Quality**: Requires high-quality multiple sequence alignments.
- **Model Selection**: Choosing appropriate background models is critical.
- **Sequence Diversity**: May perform poorly with very low or very high diversity.
- **Computational Time**: May be slow for large alignments.
- **Interpretation**: Requires understanding of statistical significance.

## Examples

### Analyze genetic variation significance
**Args:** `deltabs --alignment input.fa --output results.tsv`
**Explanation:** Quantifies significance of genetic variation in alignment.

### With custom profile
**Args:** `deltabs --alignment input.fa --profile profile.hmm --output results.tsv`
**Explanation:** Use custom HMM profile for background modeling.

### Generate detailed report
**Args:** `deltabs --alignment input.fa --output results.tsv --verbose`
**Explanation:** Generate detailed output with additional statistics.