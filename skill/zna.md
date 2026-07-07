---
name: zna
category: formatting
description: High-performance binary format for compressed nucleic acid sequences
tags: [zna, formatting, compression, sequencing, dna, rna]
author: oxo-call-community
source_url: "https://github.com/mkiyer/zna"
---

## Concepts

- **Tool Overview**: ZNA is a specialized binary format for storing DNA/RNA sequences with exceptional compression and I/O speed
- **Compression Performance**: Achieves 3.7-4.0x compression ratio with Zstd algorithm
- **Throughput**: 135 MB/s roundtrip throughput (9.5x faster than Python baseline), 2.8+ GB/s encoding/decoding for long reads
- **Architecture**: Block-based architecture for memory efficiency, supports single-end, paired-end, and interleaved reads
- **Implementation**: C++ acceleration with pure Python fallback for cross-platform compatibility
- **Installation**: `conda install -c bioconda zna` or `pip install zna`

## Pitfalls

- **Format Compatibility**: ZNA format is not widely adopted; may require conversion for downstream tools
- **Version Compatibility**: Binary format may change between versions; ensure consistent version usage
- **Reference Genome Requirement**: Some operations may require matching reference genome
- **Limited Tool Support**: Fewer tools support ZNA format compared to FASTA/FASTQ

## Examples

### Convert FASTQ to ZNA
**Args:** `zna convert -i reads.fastq -o reads.zna`
**Explanation:** Convert FASTQ file to compressed ZNA format.

### Convert paired-end reads
**Args:** `zna convert -i reads_R1.fastq -j reads_R2.fastq -o reads.zna`
**Explanation:** Convert paired-end FASTQ files to interleaved ZNA format.

### Extract reads from ZNA
**Args:** `zna extract -i reads.zna -o extracted.fastq`
**Explanation:** Extract reads from ZNA format back to FASTQ.