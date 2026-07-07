---
name: nanospring
category: utility
description: NanoSpring is a specialized compression tool for nanopore reads in FASTQ files with high compression ratios.
tags: [nanospring, utility, nanopore, compression, fastq]
author: oxo-call-community
source_url: "https://github.com/qm2/NanoSpring"
---

## Concepts

- **Tool Overview**: NanoSpring v0.2 is a specialized compression tool designed for Oxford Nanopore FASTQ files.
- **Core Function**: Compresses Nanopore FASTQ files using reference-based or de novo compression algorithms.
- **Algorithm**: Uses context-specific compression optimized for long-read sequencing data characteristics.
- **Input Format**: Accepts FASTQ files from Nanopore sequencing, either gzipped or uncompressed.
- **Output**: Produces compressed .nss archives with high compression ratios.
- **Use Case**: Storage optimization for large Nanopore datasets, efficient data transfer and sharing.

## Pitfalls

- **Reference Requirements**: Reference-based compression requires matching reference sequence.
- **Decompression Speed**: Decompression may be slower than other formats.
- **File Compatibility**: Compressed files can only be read by NanoSpring.
- **Memory Usage**: Compression of large files requires significant RAM.
- **Version Compatibility**: Archives created with different versions may not be compatible.
- **Lossy Compression**: Some modes may discard quality information.

## Examples

### Display help
**Args:** `nanospring --help`
**Explanation:** Shows available options and usage instructions.

### Compress FASTQ
**Args:** `nanospring -i reads.fastq -o compressed.nss`
**Explanation:** Compresses Nanopore FASTQ file into NanoSpring archive.

### Decompress archive
**Args:** `nanospring -d compressed.nss -o reads.fastq`
**Explanation:** Decompresses NanoSpring archive back to FASTQ format.

### Reference-based compression
**Args:** `nanospring -i reads.fastq -r reference.fasta -o ref_compressed.nss`
**Explanation:** Uses reference sequence for improved compression ratio.

### Gzipped input
**Args:** `nanospring -i reads.fastq.gz -o compressed.nss`
**Explanation:** Processes gzipped FASTQ file directly.

### Quality-aware compression
**Args:** `nanospring -i reads.fastq -q -o quality_compressed.nss`
**Explanation:** Preserves quality scores during compression.