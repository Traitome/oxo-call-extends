---
name: kmerfinder
category: metagenomics
description: Prediction of bacterial species using a fast K-mer algorithm.
tags: [kmerfinder, metagenomics]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/kmerfinder"
---

## Concepts

- **Tool Overview**: kmerfinder v3.0.2 - Prediction of bacterial species using a fast K-mer algorithm..
- **Core Function**: Prediction of bacterial species using a fast K-mer algorithm.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kmerfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Find species
**Args:** `kmerfinder.py -i reads.fastq -db /path/to/db -o output`
**Explanation:** Identifies species from sequencing reads using k-mer matching.

