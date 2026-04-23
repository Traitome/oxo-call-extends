---
name: slclust
category: population-genomics
description: A utility that performs single-linkage clustering with the option of applying a Jaccard similarity coefficient to break weakly bound clusters into distinct clusters.
tags: [slclust, population-genomics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/slclust"
---

## Concepts

- **Tool Overview**: slclust (v02022010) - A utility that performs single-linkage clustering with the option of applying a Jaccard similarity coefficient to break weakly bound clusters into distinct clusters.
- **Core Function**: A utility that performs single-linkage clustering with the option of applying a Jaccard similarity coefficient to break weakly bound clusters into distinct clusters.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda slclust`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `slclust -i <input.vcf> -o <output_dir>`
**Explanation:** Run slclust with typical input and output options.
