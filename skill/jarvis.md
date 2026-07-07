---
name: jarvis
category: utility
description: Efficient lossless compression of genomic sequences.
tags: [jarvis, utility, compression, genomics, sequences]
author: oxo-call-community
source_url: "https://github.com/cobilab/jarvis"
---

## Concepts

- **Tool Overview**: jarvis (v1.1) - A tool for efficient lossless compression of genomic sequences, reducing storage requirements.
- **Reference-based Compression**: Uses reference sequences to achieve higher compression ratios.
- **Delta Encoding**: Encodes differences from a reference sequence rather than full sequences.
- **FASTA/FASTQ Support**: Handles both sequence and quality data compression.
- **Random Access**: Supports random access to compressed sequences without full decompression.
- **Multiple References**: Can use multiple reference sequences for improved compression.

## Pitfalls

- **Reference Selection**: Choosing an appropriate reference sequence is critical.
- **Memory Usage**: Building reference indexes requires significant memory.
- **Reference Bias**: Compression may be less effective for sequences highly divergent from the reference.
- **Decompression Dependency**: Requires the same reference for decompression.
- **Initial Overhead**: Building reference index adds initial processing time.
- **Format Limitations**: May not support all specialized sequence formats.

## Examples

### Compress with reference
**Args:** `jarvis compress -i input.fasta -r reference.fasta -o output.jarvis`
**Explanation:** Compresses input sequences using reference sequence.

### Decompress with reference
**Args:** `jarvis decompress -i input.jarvis -r reference.fasta -o output.fasta`
**Explanation:** Decompresses file using the same reference used for compression.

### Compress FASTQ
**Args:** `jarvis compress -i input.fastq -r reference.fasta -o output.jarvis --fastq`
**Explanation:** Compresses FASTQ file with quality scores.

### Build reference index
**Args:** `jarvis index -r reference.fasta -o ref_index/`
**Explanation:** Pre-builds index for faster compression/decompression.

### Multiple references
**Args:** `jarvis compress -i input.fasta -r ref1.fasta ref2.fasta -o output.jarvis`
**Explanation:** Uses multiple reference sequences for compression.

### Check compression ratio
**Args:** `jarvis stats -i input.jarvis`
**Explanation:** Shows compression statistics including ratio and original size.