---
name: kmtricks
category: utility
description: A k-mer matrix framework
tags: [kmtricks, utility]
author: oxo-call-community
source_url: "https://github.com/tlemane/kmtricks"
---

## Concepts

- **Tool Overview**: kmtricks v1.5.1 - kmtricks allows for efficient construction of k-mer and Bloom filter matrices from large read collections.
- **Core Function**: A k-mer matrix framework
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kmtricks`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Build k-mer matrix
**Args:** `kmtricks pipeline --file reads.list --run-dir output --kmer-size 31`
**Explanation:** Builds k-mer presence/absence matrix from read files.

