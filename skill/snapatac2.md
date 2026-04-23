---
name: snapatac2
category: epigenomics
description: SnapATAC2: Single-cell epigenomics analysis pipeline.
tags: [snapatac2, epigenomics]
author: oxo-call-community
source_url: "https://scverse.org/SnapATAC2"
---

## Concepts

- **Tool Overview**: snapatac2 (v2.9.0) - SnapATAC2: Single-cell epigenomics analysis pipeline.
- **Core Function**: SnapATAC2: Single-cell epigenomics analysis pipeline.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snapatac2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snapatac2 -i <input.bam> -o <output_dir>`
**Explanation:** Run snapatac2 with typical input and output options.
