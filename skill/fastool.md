---
name: fastool
category: formatting
description: "A simple and quick tool to read huge FastQ and FastA files (both normal and gzipped) and manipulate them."
tags: [fastool, formatting, FASTQ, FASTA, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fstrozzi/Fastool"
---

## Concepts

- **Tool Overview**: Fastool is a simple and efficient tool for reading and manipulating large FASTQ and FASTA files, including gzipped files.
- **Core Function**: Provides utilities for processing large sequence files efficiently.
- **Input/Output**: Input: FASTQ/FASTA files (gzipped or uncompressed). Output: Processed sequences, statistics.
- **Algorithm**: Implements efficient parsing and manipulation of sequence files.
- **Key Features**: Fast parsing, gzip support, sequence manipulation, statistics generation, memory efficient.
- **Installation**: `conda install -c bioconda fastool`

## Pitfalls

- **Memory Usage**: Very large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ/FASTA format.
- **Compression**: Gzip files require appropriate decompression.
- **Processing Time**: Large files may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Count sequences
**Args:** `fastool count -i reads.fastq`
**Explanation:** Counts sequences in FASTQ file.

### Filter by length
**Args:** `fastool filter -i reads.fastq -o filtered.fastq -l 100`
**Explanation:** Filters sequences by minimum length.

### Convert FASTA to FASTQ
**Args:** `fastool convert -i input.fasta -o output.fastq`
**Explanation:** Converts FASTA to FASTQ format.

### Extract IDs
**Args:** `fastool ids -i input.fasta -o ids.txt`
**Explanation:** Extracts sequence identifiers.

### Statistics
**Args:** `fastool stats -i reads.fastq -o stats.txt`
**Explanation:** Generates sequence statistics.