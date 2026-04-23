---
name: zna
category: formatting
description: High-performance binary format for compressed nucleic acid sequences
tags: [zna, formatting]
author: oxo-call-community
source_url: "https://github.com/mkiyer/zna/blob/main/README.md"
---

## Concepts

- **Tool Overview**: zna (v0.3.0) - ZNA (Compressed Z-Nucleic N-Acid A) is a specialized binary format for storing DNA/RNA sequences with exceptional compression and I/O speed.  Features: - 135 MB/s roundtrip throughput (9.5x faster than Python baseline) - 2.8+ GB/s encoding/decoding for long reads - 3.7-4.0x compression ratio with Zstd - C++ acceleration with pure Python fallback - Block-based architecture for memory efficiency - Supports single-end, paired-end, and interleaved reads - Supports strand-specific protocols
- **Core Function**: High-performance binary format for compressed nucleic acid sequences
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda zna`

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
