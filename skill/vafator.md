---
name: vafator
category: alignment
description: VAFator annotates the variants in a VCF file with technical annotations extracted from one or more BAM alignment files. We implement a set of basic coverage annotations and also more sophisticated published annotations used to assess the quality of every variant call.
tags: [vafator, alignment, bam, vcf]
author: oxo-call-community
source_url: "https://github.com/tron-bioinformatics/vafator"
---

## Concepts

- **Tool Overview**: vafator (v3.0.0) - VAFator annotates the variants in a VCF file with technical annotations extracted from one or more BAM alignment files. We implement a set of basic coverage annotations and also more sophisticated published annotations used to assess the quality of every variant call.
- **Core Function**: VAFator annotates the variants in a VCF file with technical annotations extracted from one or more BAM alignment files. We implement a set of basic coverage annotations and also more sophisticated published annotations used to assess the quality of every variant call.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vafator`

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
