---
name: yanagiba
category: qc
description: Filter short or low quality Oxford Nanopore reads which have been basecalled with Albacore.
tags: [yanagiba, qc]
author: oxo-call-community
source_url: "https://github.com/Adamtaranto/Yanagiba"
---

## Concepts

- **Tool Overview**: yanagiba (v1.0.0) - Filter short or low quality Oxford Nanopore reads which have been basecalled with Albacore.
- **Core Function**: Filter short or low quality Oxford Nanopore reads which have been basecalled with Albacore.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda yanagiba`

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
