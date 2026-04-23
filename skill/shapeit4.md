---
name: shapeit4
category: population-genomics
description: fast and accurate method for estimation of haplotypes (phasing)
tags: [shapeit4, population-genomics]
author: oxo-call-community
source_url: "https://odelaneau.github.io/shapeit4/"
---

## Concepts

- **Tool Overview**: shapeit4 (v4.2.2) - fast and accurate method for estimation of haplotypes (phasing)
- **Core Function**: fast and accurate method for estimation of haplotypes (phasing)
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shapeit4`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shapeit4 -i <input.vcf> -o <output_dir>`
**Explanation:** Run shapeit4 with typical input and output options.
