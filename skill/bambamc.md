---
name: bambamc
category: formatting
description: bambamc - Lightweight C implementation for name collating BAM file processing
tags: [bambamc, formatting, BAM, sorting, C-implementation]
author: oxo-call-community
source_url: "https://github.com/gt1/bambamc"
---

## Concepts

- **Tool Overview**: bambamc is a lightweight C implementation for name collating BAM file input and output, designed for efficient read name-based sorting and processing. Version 0.0.50.
- **Core Function**: Performs read name-based collation and processing of BAM files efficiently.
- **Name Collation**: Sorts BAM records by read name for paired-end processing.
- **Lightweight**: Implemented in C for high performance and minimal memory footprint.
- **Stream Processing**: Supports streaming BAM processing without loading entire file into memory.
- **Input/Output**: Accepts BAM files, outputs sorted/processed BAM files.
- **Installation**: `conda install -c bioconda bambamc`.

## Pitfalls

- **Read Name Assumptions**: Assumes read names follow standard naming conventions.
- **Memory Usage**: While lightweight, very large files still require adequate memory.
- **Version Compatibility**: Options may vary between versions. Check help for your version.
- **BAM Format**: Requires properly formatted BAM files with correct headers.

## Examples

### Basic name collation
**Args:** `bambamc -i input.bam -o sorted.bam`
**Explanation:** Sorts BAM file by read name.

### Paired-end processing
**Args:** `bambamc -i input.bam -o paired.bam --paired`
**Explanation:** Processes paired-end reads ensuring proper pairing.

### Stream processing
**Args:** `bambamc -i input.bam --stream | samtools view`
**Explanation:** Streams sorted reads to another tool.

### Output SAM format
**Args:** `bambamc -i input.bam -o output.sam --sam`
**Explanation:** Outputs sorted reads in SAM format.

### Verbose mode
**Args:** `bambamc -i input.bam -o sorted.bam -v`
**Explanation:** Shows processing progress and statistics.

### Buffer size adjustment
**Args:** `bambamc -i input.bam -o sorted.bam --buffer 1000000`
**Explanation:** Sets custom buffer size for sorting.

### Display help
**Args:** `bambamc --help`
**Explanation:** Shows all available command-line options and usage information.