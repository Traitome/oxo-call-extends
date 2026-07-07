---
name: seqan3
category: programming
description: seqan3 - C++ template library for biological sequence analysis
tags: ["seqan3", "programming", "C++", "sequence-analysis"]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan3"
---

## Concepts

- **Tool Overview**: seqan3 (v3.4.2) is a C++ template library for biological sequence analysis.
- **Core Function**: Provides data structures and algorithms for sequence analysis.
- **Algorithm**: Implements various algorithms for sequence manipulation and analysis.
- **Input/Output**: Accepts sequence data and produces analysis results.
- **C++ Library**: Focuses on high-performance C++ sequence analysis.
- **Applications**: Bioinformatics tool development, sequence analysis, and algorithm implementation.

## Pitfalls

- **C++ Knowledge**: Requires C++ programming knowledge.
- **Build System**: Requires proper CMake setup.
- **Memory Management**: Requires careful memory management in C++.
- **Compile Time**: May have long compile times for large projects.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features may require reading source code.

## Examples

### Include header
**Args:** `#include <seqan3/sequence/all.hpp>`
**Explanation:** Includes all sequence-related headers.

### Read FASTA
**Args:** `seqan3::sequence_file_input fin{"input.fasta"};`
**Explanation:** Reads FASTA file.

### Write FASTA
**Args:** `seqan3::sequence_file_output fout{"output.fasta"};`
**Explanation:** Writes FASTA file.

### Sequence alignment
**Args:** `seqan3::align_pairwise(seq1, seq2);`
**Explanation:** Performs pairwise sequence alignment.

### Help documentation
**Args:** `https://docs.seqan.de/seqan/3.4.2/`
**Explanation:** Online documentation.

### Version check
**Args:** `seqan3::version`
**Explanation:** Shows library version.

### Build project
**Args:** `cmake -S . -B build && cmake --build build`
**Explanation:** Builds project using CMake.