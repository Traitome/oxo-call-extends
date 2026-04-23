---
name: tandem-genotypes
category: alignment
description: Find tandem repeat length changes, from "long" DNA reads aligned to a genome
tags: [tandem-genotypes, alignment]
author: oxo-call-community
source_url: "https://github.com/mcfrith/tandem-genotypes"
---

## Concepts

- **Tool Overview**: tandem-genotypes (v1.9.2) - Find tandem repeat length changes, from "long" DNA reads aligned to a genome
- **Core Function**: Find tandem repeat length changes, from "long" DNA reads aligned to a genome
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tandem-genotypes`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tandem-genotypes -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run tandem-genotypes with typical input and output options.
