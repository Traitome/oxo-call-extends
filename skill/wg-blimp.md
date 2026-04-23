---
name: wg-blimp
category: alignment
description: wg-blimp (Whole Genome BisuLfIte sequencing Methylation analysis Pipeline)
tags: [wg-blimp, alignment]
author: oxo-call-community
source_url: "https://github.com/MarWoes/wg-blimp"
---

## Concepts

- **Tool Overview**: wg-blimp (v0.10.0) - wg-blimp (Whole Genome BisuLfIte sequencing Methylation analysis Pipeline) can be utilised to analyse WGBS data. It performs alignment, qc, methylation calling, DMR calling, segmentation and annotation using a multitude of tools.
- **Core Function**: wg-blimp (Whole Genome BisuLfIte sequencing Methylation analysis Pipeline)
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda wg-blimp`

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
