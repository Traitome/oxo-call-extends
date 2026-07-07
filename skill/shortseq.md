---
name: shortseq
category: utility
description: shortseq - Compact and efficient sequence storage for Python
tags: ["shortseq", "utility", "sequence", "python"]
author: oxo-call-community
source_url: "https://github.com/AlexTate/ShortSeq"
---

## Concepts

- **Tool Overview**: shortseq (v0.0.1) provides compact Python objects for storing short biological sequences.
- **Core Function**: Reduces memory usage by up to 73% compared to standard Python strings.
- **Algorithm**: Uses bit-packing and pre-computed hash values for efficiency.
- **Input/Output**: Accepts sequence strings and returns ShortSeq objects.
- **Memory Efficiency**: Optimized for storing millions of short sequences.
- **Applications**: Bioinformatics pipelines, sequence analysis, and memory-intensive applications.

## Pitfalls

- **Sequence Length**: Designed for short sequences, not full-length genomes.
- **Python Dependencies**: Requires Python environment.
- **Version Compatibility**: Early development stage, API may change.
- **Type Conversion**: Requires explicit conversion back to strings.
- **Limited Operations**: Not all string operations are supported.
- **Documentation**: Limited documentation available.

## Examples

### Create ShortSeq
**Args:** `shortseq -s "ATCG"`
**Explanation:** Creates a ShortSeq from sequence string.

### From file
**Args:** `shortseq -f sequences.txt -o output.pkl`
**Explanation:** `-f` input file with sequences; `-o` output pickle file.

### Convert to string
**Args:** `shortseq -c input.pkl -o sequences.txt`
**Explanation:** `-c` convert ShortSeq objects back to strings.

### Help command
**Args:** `shortseq --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shortseq --version`
**Explanation:** Shows current version.

### Benchmark memory
**Args:** `shortseq -b sequences.txt`
**Explanation:** `-b` run memory benchmark.

### Batch processing
**Args:** `shortseq -b batch_sequences.txt -t 4`
**Explanation:** `-t 4` use 4 threads for batch processing.
