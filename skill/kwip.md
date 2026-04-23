---
name: kwip
category: population-genomics
description: kWIP implements a de novo, alignment free measure of sample genetic dissimilarity
tags: [kwip, population-genomics, alignment]
author: oxo-call-community
source_url: "https://github.com/kdmurray91/kWIP"
---

## Concepts

- **Tool Overview**: kwip v0.2.0 - kWIP implements a de novo, alignment free measure of sample genetic dissimilarity.
- **Core Function**: kWIP implements a de novo, alignment free measure of sample genetic dissimilarity
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kwip`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Compute distance
**Args:** `kwip -k hash1.kh -k hash2.kh -o dist_matrix.txt`
**Explanation:** Computes weighted inner product distance between samples.

