---
name: deepmicro
category: metagenomics
description: Deep representation learning framework for microbiome data.
tags: [deepmicro, metagenomics, deep-learning, representation-learning]
author: oxo-call-community
source_url: "https://github.com/paulzierep/DeepMicro"
---

## Concepts

- **Tool Overview**: DeepMicro v1.4 - Deep representation learning framework for microbiome data analysis.
- **Core Function**: Learns low-dimensional representations of microbiome profiles using deep autoencoders for classification and clustering.
- **Input/Output**: Expects abundance tables (OTU/ASV); outputs learned representations and classification results.
- **Installation**: `conda install -c bioconda deepmicro`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct abundance table format with proper sample labels.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmicro --data abundances.tsv --output results/`
**Explanation:** Learns deep representations from microbiome abundance data.
