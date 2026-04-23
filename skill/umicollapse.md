---
name: umicollapse
category: utility
description: Accelerating the deduplication and collapsing process for reads with Unique Molecular Identifiers (UMI).
tags: [umicollapse, utility]
author: oxo-call-community
source_url: "https://github.com/Daniel-Liu-c0deb0t/UMICollapse"
---

## Concepts

- **Tool Overview**: umicollapse (v1.1.0) - UMIs are a popular way to identify duplicate DNA/RNA reads caused by PCR amplification. This requires software for collapsing duplicate reads with the same UMI, while accounting for sequencing/PCR errors. This tool implements many efficient algorithms for orders-of-magnitude faster UMI deduplication than previous tools (UMI-tools, etc.), while maintaining similar functionality. This is achieved by using faster data structures with n-grams and BK-trees, along other techniques that are carefully implemented to scale well to larger datasets and longer UMIs. Users of UMICollapse have reported speedups from taking hours or days to run with a previous tool to taking only a few minutes with this tool with real datasets! doi 10.7717/peerj.8275.
- **Core Function**: Accelerating the deduplication and collapsing process for reads with Unique Molecular Identifiers (UMI).
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda umicollapse`

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
