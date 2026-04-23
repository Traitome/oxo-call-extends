---
name: nail
category: alignment
description: Profile Hidden Markov Model (pHMM) biological sequence alignment tool.
tags: [nail, alignment, phmm, hmm, sequence]
author: oxo-call-community
source_url: "https://github.com/TravisWheelerLab/nail"
---

## Concepts

- **Tool Overview**: NAIL v0.5.0 - profile Hidden Markov Model biological sequence alignment tool.
- **Core Function**: Aligns biological sequences using profile HMMs for sensitive homology detection.
- **Input/Output**: Takes sequence files and HMM profiles; outputs alignments.
- **Installation**: `conda install -c bioconda nail`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted HMM profiles.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i sequences.fasta -p profile.hmm -o alignment.txt`
**Explanation:** Aligns sequences against a profile HMM.
