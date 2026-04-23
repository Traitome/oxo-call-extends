---
name: tophat
category: alignment
description: A spliced read mapper for RNA-Seq.
tags: [tophat, alignment]
author: oxo-call-community
source_url: "http://ccb.jhu.edu/software/tophat"
---

## Concepts

- **Tool Overview**: tophat (v2.1.2) - A spliced read mapper for RNA-Seq.
- **Core Function**: A spliced read mapper for RNA-Seq.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda tophat`

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
