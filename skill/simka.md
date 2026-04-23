---
name: simka
category: utility
description: Simka and simkaMin are de novo comparative metagenomics tools. Simka represents each dataset as a k-mer spectrum and computes several classical ecological distances between them. SimkaMin outputs approximate (but very similar) results by subsampling the kmer space and requires much less computational resources.
tags: [simka, utility, sam]
author: oxo-call-community
source_url: "https://github.com/GATB/simka"
---

## Concepts

- **Tool Overview**: simka (v1.5.3) - Simka and simkaMin are de novo comparative metagenomics tools. Simka represents each dataset as a k-mer spectrum and computes several classical ecological distances between them. SimkaMin outputs approximate (but very similar) results by subsampling the kmer space and requires much less computational resources.
- **Core Function**: Simka and simkaMin are de novo comparative metagenomics tools. Simka represents each dataset as a k-mer spectrum and computes several classical ecological distances between them. SimkaMin outputs approximate (but very similar) results by subsampling the kmer space and requires much less computational resources.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda simka`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `simka -i <input_file> -o <output_file>`
**Explanation:** Run simka with typical input and output options.
