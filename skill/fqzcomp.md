---
name: fqzcomp
category: formatting
description: Fqzcomp is a basic fastq compressor, designed primarily for high performance.
tags: [fqzcomp, compression, FASTQ, bioinformatics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/fqzcomp/"
---

## Concepts
- **FASTQ Compression**: High-performance compression of FASTQ files.
- **Lossless Compression**: Maintains full data integrity.
- **Quality Score Encoding**: Optimized encoding for quality scores.
- **Parallel Processing**: Supports multi-threaded compression.
- **Random Access**: Enables random access to compressed data.

## Pitfalls
- **Compression Ratio**: May not achieve highest compression ratios.
- **Format Limitations**: Only supports FASTQ format.
- **Decompression Speed**: Decompression may be slower than other tools.
- **Memory Requirements**: High memory usage for large files.
- **Tool Integration**: Limited integration with other bioinformatics tools.

## Examples
### Compress FASTQ file
**Args:** `fqzcomp reads.fastq reads.fqz`
**Explanation:** Compresses a FASTQ file using fqzcomp format.

### Decompress file
**Args:** `fqzcomp -d reads.fqz reads.fastq`
**Explanation:** Decompresses a fqzcomp file back to FASTQ.

### Parallel compression
**Args:** `fqzcomp -t 8 reads.fastq reads.fqz`
**Explanation:** Uses 8 threads for compression.

### Compress with high compression
**Args:** `fqzcomp -c 9 reads.fastq reads.fqz`
**Explanation:** Uses maximum compression level.

### Verify compressed file
**Args:** `fqzcomp -v reads.fqz`
**Explanation:** Verifies the integrity of a compressed file.