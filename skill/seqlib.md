---
name: seqlib
category: programming
description: seqlib - C++ interface to HTSlib, BWA-MEM and Fermi
tags: ["seqlib", "programming", "C++", "alignment"]
author: oxo-call-community
source_url: "https://github.com/walaj/SeqLib/blob/1.2.0/README.md"
---

## Concepts

- **Tool Overview**: seqlib (v1.2.0) provides a C++ interface to HTSlib, BWA-MEM and Fermi.
- **Core Function**: Provides unified C++ API for sequence alignment and variant calling.
- **Algorithm**: Wraps HTSlib for BAM/VCF I/O and BWA-MEM for alignment.
- **Input/Output**: Accepts FASTA/BAM/VCF files and produces aligned sequences.
- **C++ Library**: Focuses on high-performance sequence analysis in C++.
- **Applications**: Bioinformatics tool development, sequence alignment, and variant analysis.

## Pitfalls

- **C++ Knowledge**: Requires C++ programming knowledge.
- **Build System**: Requires proper CMake setup.
- **Memory Management**: Requires careful memory management in C++.
- **Compile Time**: May have long compile times.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features may require reading source code.

## Examples

### Include header
**Args:** `#include <SeqLib/SeqLib.h>`
**Explanation:** Includes SeqLib headers.

### Align reads
**Args:** `SeqLib::BWAWrapper bwa; bwa.AlignSeqs(reads, ref, alns);`
**Explanation:** Aligns reads using BWA-MEM.

### Read BAM
**Args:** `SeqLib::BamReader reader("input.bam");`
**Explanation:** Opens BAM file for reading.

### Write BAM
**Args:** `SeqLib::BamWriter writer("output.bam");`
**Explanation:** Creates BAM file for writing.

### Help documentation
**Args:** `https://github.com/walaj/SeqLib/wiki`
**Explanation:** Online documentation.

### Version check
**Args:** `SeqLib::VERSION`
**Explanation:** Shows library version.

### Build project
**Args:** `cmake -S . -B build && cmake --build build`
**Explanation:** Builds project using CMake.