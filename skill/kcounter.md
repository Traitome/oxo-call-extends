---
name: kcounter
category: programming
description: A simple library for counting DNA k-mers in Python, written in Rust.
tags: [kcounter, programming, k-mer, Python, Rust]
author: oxo-call-community
source_url: "https://github.com/apcamargo/kcounter"
---

## Concepts

- **Tool Overview**: kcounter (v0.1.1) - Fast k-mer counting library for Python.
- **Rust Backend**: Core implementation in Rust for speed.
- **Python Interface**: Easy-to-use Python API.
- **Memory Efficient**: Optimized memory usage.
- **Multiple Formats**: Supports FASTA and FASTQ input.
- **Flexible k-mer Sizes**: Supports various k-mer sizes.

## Pitfalls

- **k-mer Size Limits**: Maximum k-mer size may be limited.
- **Memory Usage**: Very large k-mers require more memory.
- **Python Version**: Requires specific Python version.
- **Rust Dependencies**: Requires Rust toolchain for building.
- **Input Size**: Extremely large files may cause issues.
- **Output Size**: k-mer counts can be large files.

## Examples

### Count k-mers from FASTA
**Args:** `kcounter -i genome.fasta -k 21 -o counts.txt`
**Explanation:** Counts 21-mers in FASTA file.

### Count k-mers from FASTQ
**Args:** `kcounter -i reads.fastq -k 31 -o counts.txt`
**Explanation:** Counts 31-mers in FASTQ file.

### Multiple k-mer sizes
**Args:** `kcounter -i genome.fasta -k 15,21,31 -o counts/`
**Explanation:** Counts multiple k-mer sizes.

### Filter low-frequency k-mers
**Args:** `kcounter -i genome.fasta -k 21 -m 5 -o counts.txt`
**Explanation:** Only keeps k-mers with count >= 5.

### Output as JSON
**Args:** `kcounter -i genome.fasta -k 21 -o counts.json -f json`
**Explanation:** Outputs counts in JSON format.

### Use in Python script
**Args:** `from kcounter import KCounter; kc = KCounter(21); kc.count("genome.fasta")`
**Explanation:** Use kcounter in Python code.