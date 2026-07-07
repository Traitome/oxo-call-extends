---
name: jarvis3
category: utility
description: Improved encoder for genomic sequences with efficient compression.
tags: [jarvis3, utility, compression, encoding, genomics]
author: oxo-call-community
source_url: "https://github.com/cobilab/jarvis3"
---

## Concepts

- **Tool Overview**: jarvis3 (v3.7) - An advanced encoder/compressor for genomic sequences that provides efficient lossless compression.
- **Lossless Compression**: Compresses genomic sequences without losing any information.
- **Sequence Encoding**: Uses specialized encoding schemes optimized for DNA/RNA sequences.
- **Multi-format Support**: Works with FASTA, FASTQ, and other common bioinformatics formats.
- **Parallel Processing**: Supports parallel compression for large datasets.
- **Decompression**: Provides fast decompression to restore original sequences.

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory for compression.
- **Format Compatibility**: Some specialized formats may not be supported.
- **Compression Ratio**: Compression efficiency varies depending on sequence complexity.
- **Decompression Speed**: Decompression may be slower than compression.
- **File Size**: Very small files may not benefit from compression.
- **Version Compatibility**: Compressed files may not be compatible between versions.

## Examples

### Compress FASTA file
**Args:** `jarvis3 -c input.fasta -o output.jarvis`
**Explanation:** Compresses FASTA file using default settings.

### Decompress file
**Args:** `jarvis3 -d input.jarvis -o output.fasta`
**Explanation:** Decompresses jarvis-compressed file to FASTA format.

### Compress FASTQ with quality
**Args:** `jarvis3 -c input.fastq -o output.jarvis --keep-quality`
**Explanation:** Compresses FASTQ file while preserving quality scores.

### Use maximum compression
**Args:** `jarvis3 -c input.fasta -o output.jarvis -l 9`
**Explanation:** Uses maximum compression level (9) for best compression ratio.

### Parallel processing
**Args:** `jarvis3 -c input.fasta -o output.jarvis -t 8`
**Explanation:** Uses 8 threads for parallel compression.

### Compress multiple files
**Args:** `jarvis3 -c file1.fasta file2.fasta -o output.jarvis`
**Explanation:** Compresses multiple FASTA files into a single archive.