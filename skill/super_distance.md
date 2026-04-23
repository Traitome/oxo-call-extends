---
name: super_distance
category: population-genomics
description: Supertree method with distances
tags: [super_distance, population-genomics]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/super_distance"
---

## Concepts

- **Tool Overview**: super_distance (v1.1.0) - Supertree method with distances
- **Core Function**: Supertree method with distances
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda super_distance`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `super_distance -i <input.vcf> -o <output_dir>`
**Explanation:** Run super_distance with typical input and output options.
