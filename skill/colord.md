---
name: colord
category: qc
description: Versatile compressor for third generation sequencing reads
tags: [colord, compression, third-generation-sequencing, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/colord"
---

## Concepts

- **Tool Overview**: colord is a versatile compression tool specifically designed for third-generation sequencing reads from platforms like Oxford Nanopore and PacBio.
- **Core Function**: Compresses long-read sequencing data efficiently while maintaining quality information and enabling fast random access.
- **Algorithm**: Uses specialized compression algorithms optimized for long-read characteristics including quality scores and signal data.
- **Input**: FASTQ or BAM files from third-generation sequencing platforms.
- **Output**: Compressed sequence files with optional quality score preservation.
- **Application**: Long-read data storage, transfer, and archival.
- **Installation**: Install via bioconda: `conda install -c bioconda colord`

## Pitfalls

- **Compression Ratio**: Compression efficiency depends on read characteristics.
- **Memory Usage**: May require significant memory for large datasets.
- **Decompression Speed**: Decompression may be slower than compression.
- **Quality Scores**: Quality score compression may be lossy in some modes.
- **Compatibility**: Compressed files require colord for decompression.

## Examples

### Compress sequencing reads
**Args:** `colord -i reads.fastq -o reads.colord`
**Explanation:** Compresses FASTQ reads using colord algorithm.

### With quality score compression
**Args:** `colord -i reads.fastq -q lossless -o reads.colord`
**Explanation:** Uses lossless quality score compression.

### Decompress file
**Args:** `colord -d -i reads.colord -o reads.fastq`
**Explanation:** Decompresses colord file back to FASTQ format.

### Display help
**Args:** `colord --help`
**Explanation:** Shows all available options and usage information.