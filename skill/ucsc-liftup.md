---
name: ucsc-liftup
category: alignment
description: Change coordinates of .psl, .agp, .gap, .gl, .out, .align, .gff, .gtf.
tags: [ucsc-liftup, alignment]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-liftup (v482) - Change coordinates of .psl, .agp, .gap, .gl, .out, .align, .gff, .gtf.
- **Core Function**: Change coordinates of .psl, .agp, .gap, .gl, .out, .align, .gff, .gtf.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-liftup`

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
