---
name: strvctvre
category: variant-calling
description: StrVCTVRE, a structural variant classifier for exonic deletions and duplications
tags: [strvctvre, variant-calling]
author: oxo-call-community
source_url: "https://github.com/andrewSharo/StrVCTVRE/tree/master"
---

## Concepts

- **Tool Overview**: strvctvre (v1.10) - StrVCTVRE, a structural variant classifier for exonic deletions and duplications
- **Core Function**: StrVCTVRE, a structural variant classifier for exonic deletions and duplications
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strvctvre`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strvctvre -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run strvctvre with typical input and output options.
