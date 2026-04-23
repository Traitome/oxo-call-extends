---
name: ibdne
category: population-genomics
description: The IBDNe program estimates the historical effective population size of a homogenous population (from the output of IDBseq).
tags: [ibdne, population-genomics]
author: oxo-call-community
source_url: "http://faculty.washington.edu/browning/ibdne.html"
---

## Concepts

- **Tool Overview**: ibdne (v04Sep15.e78) - The IBDNe program estimates the historical effective population size of a homogenous population (from the output of IDBseq).
- **Core Function**: Provides functionality for population-genomics tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda ibdne`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
