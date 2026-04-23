---
name: ucsc-bigwigtowig
category: formatting
description: Convert bigWig to wig. This will keep more of the same structure of the original wig than bigWigToBedGraph does, but still will break up large stepped sections into smaller ones.
tags: [ucsc-bigwigtowig, formatting]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-bigwigtowig (v482) - Convert bigWig to wig. This will keep more of the same structure of the original wig than bigWigToBedGraph does, but still will break up large stepped sections into smaller ones.
- **Core Function**: Convert bigWig to wig. This will keep more of the same structure of the original wig than bigWigToBedGraph does, but still will break up large stepped sections into smaller ones.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-bigwigtowig`

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
