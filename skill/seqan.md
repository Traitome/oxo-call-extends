---
name: seqan
category: programming
description: seqan - C++ template library for biological sequence analysis (legacy version)
tags: ["seqan", "programming", "C++", "sequence-analysis"]
author: oxo-call-community
source_url: "https://seqan.readthedocs.io"
---

## Concepts

- **Tool Overview**: seqan (v2.5.3) is the legacy C++ template library for biological sequence analysis.
- **Core Function**: Provides data structures and algorithms for sequence analysis.
- **Algorithm**: Implements various algorithms for sequence manipulation and analysis.
- **Input/Output**: Accepts sequence data and produces analysis results.
- **C++ Library**: Focuses on high-performance C++ sequence analysis.
- **Applications**: Bioinformatics tool development, sequence analysis, and algorithm implementation.

## Pitfalls

- **Legacy Version**: This is the older version; consider upgrading to seqan3.
- **C++ Knowledge**: Requires C++ programming knowledge.
- **Build System**: Requires proper CMake setup.
- **Memory Management**: Requires careful memory management in C++.
- **Compile Time**: May have long compile times for large projects.
- **Documentation**: Some features may require reading source code.

## Examples

### Include header
**Args:** `#include <seqan/sequence.h>`
**Explanation:** Includes sequence header.

### Read FASTA
**Args:** `seqan::StringSet<seqan::Dna5String> seqs; seqan::readRecords(seqs, "input.fasta");`
**Explanation:** Reads FASTA file.

### Write FASTA
**Args:** `seqan::writeRecords(seqs, "output.fasta");`
**Explanation:** Writes FASTA file.

### Sequence alignment
**Args:** `seqan::GlobalAlignmentAlignmentResult result = seqan::globalAlignment(seq1, seq2);`
**Explanation:** Performs global sequence alignment.

### Help documentation
**Args:** `https://seqan.readthedocs.io/en/seqan-v2.5.3/`
**Explanation:** Online documentation.

### Version check
**Args:** `SEQAN_VERSION_MAJOR`
**Explanation:** Shows library version.

### Build project
**Args:** `cmake -S . -B build && cmake --build build`
**Explanation:** Builds project using CMake.