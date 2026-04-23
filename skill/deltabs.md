---
name: deltabs
category: population-genomics
description: Quantifying the significance of genetic variation using probabilistic profile-based methods.
tags: [deltabs, population-genomics, genetic-variation, probabilistic]
author: oxo-call-community
source_url: "https://github.com/UCanCompBio/deltaBS/wiki"
---

## Concepts

- **Tool Overview**: deltaBS v0.1 - Tool for quantifying the significance of genetic variation using probabilistic profile-based methods.
- **Core Function**: Evaluates the significance of observed genetic variation against background expectations.
- **Input/Output**: Expects multiple sequence alignments and profiles; outputs significance scores for variation.
- **Installation**: `conda install -c bioconda deltabs`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted sequence alignments.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deltabs --alignment input.fa --output results.tsv`
**Explanation:** Quantifies significance of genetic variation in alignment.
