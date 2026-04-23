---
name: svtk
category: variant-calling
description: Utilities for consolidating, filtering, resolving, and annotating structural variants.
tags: [svtk, variant-calling]
author: oxo-call-community
source_url: "https://github.com/talkowski-lab/svtk"
---

## Concepts

- **Tool Overview**: svtk (v0.0.20190615) - Utilities for consolidating, filtering, resolving, and annotating structural variants.
- **Core Function**: Utilities for consolidating, filtering, resolving, and annotating structural variants.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svtk`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svtk -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svtk with typical input and output options.
