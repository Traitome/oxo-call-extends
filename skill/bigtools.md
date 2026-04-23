---
name: bigtools
category: utility
description: High-performance API for reading and writing bigWig and bigBed files
tags: [bigwig, bigbed, genomics, file-format]
author: oxo-call-community
source_url: "https://github.com/jackh726/bigtools"
---

## Concepts
- **Tool Overview**: bigtools provides a high-level, performant Rust API and command-line tools for reading and writing bigWig and bigBed files. These are indexed binary formats for storing genomic interval and signal data.
- **bigWig Format**: Binary format for storing dense, continuous genomic signal data (e.g., ChIP-seq signal, conservation scores).
- **bigBed Format**: Binary format for storing genomic interval annotations (e.g., gene models, peaks).
- **Performance**: Written in Rust for memory safety and speed, with random access support.

## Pitfalls
- **Index Requirement**: bigWig/bigBed files must have proper index for random access.
- **File Size**: Converting large wig/bed files to bigWig/bigBed can be memory-intensive.

## Examples
### Convert wig to bigWig
**Args:** `bigtools wig-to-bigwig input.wig chrom.sizes output.bw`
**Explanation:** Converts wig format to bigWig using chromosome sizes file.

### Extract signal from bigWig
**Args:** `bigtools bigwig-to-wig input.bw --chr chr1 --start 1000000 --end 2000000`
**Explanation:** Extracts signal values for a specific genomic region.

### Convert bed to bigBed
**Args:** `bigtools bed-to-bigbed input.bed chrom.sizes output.bb`
**Explanation:** Converts BED format to bigBed.
