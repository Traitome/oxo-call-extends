---
name: xumi
category: utility
description: CIGAR-aware extraction of per-read subsequences at specified reference regions from SAM/BAM/CRAM files.
tags: [xumi, utility, bam]
author: oxo-call-community
source_url: "https://github.com/fravadona/xumi"
---

## Concepts

- **Tool Overview**: xumi (v1.0.3) - CIGAR-aware extraction of per-read subsequences at specified reference regions from SAM/BAM/CRAM files.
- **Core Function**: CIGAR-aware extraction of per-read subsequences at specified reference regions from SAM/BAM/CRAM files.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda xumi`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
