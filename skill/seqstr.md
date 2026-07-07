---
name: seqstr
category: utility
description: seqstr - Compile simple string input into long genomic sequences
tags: ["seqstr", "utility", "sequence", "generation"]
author: oxo-call-community
source_url: "https://github.com/jzhoulab/Seqstr"
---

## Concepts

- **Tool Overview**: seqstr (v0.1.0) compiles simple string input into long genomic sequences.
- **Core Function**: Generates long genomic sequences from concise string descriptions.
- **Algorithm**: Implements string expansion for sequence generation.
- **Input/Output**: Accepts string patterns and produces FASTA sequences.
- **Sequence Generation**: Focuses on creating synthetic genomic sequences.
- **Applications**: Synthetic sequence design, primer design, and sequence testing.

## Pitfalls

- **Memory Usage**: High memory requirements for very long sequences.
- **Pattern Complexity**: Complex patterns may be difficult to design.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires correct pattern syntax.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Generate sequence
**Args:** `seqstr "ATCG[AT]10" -o output.fasta`
**Explanation:** Generates sequence from pattern.

### Repeat pattern
**Args:** `seqstr "ATCG" -n 100 -o output.fasta`
**Explanation:** `-n 100` repeats pattern 100 times.

### Random sequence
**Args:** `seqstr -r 1000 -o output.fasta`
**Explanation:** `-r 1000` generates 1000bp random sequence.

### Verbose logging
**Args:** `seqstr -v "ATCG" -o output.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqstr --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqstr --version`
**Explanation:** Shows current version.

### GC content
**Args:** `seqstr -g 0.5 -r 1000 -o output.fasta`
**Explanation:** `-g 0.5` generates sequence with 50% GC content.