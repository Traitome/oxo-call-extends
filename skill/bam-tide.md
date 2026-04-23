---
name: bam-tide
category: utility
description: bam-tide - Fast BAM to BigWig coverage tool written in Rust
tags: [coverage, bigwig, bam-processing, visualization]
author: oxo-call-community
source_url: "https://github.com/stela2502/bam_tide"
---

## Concepts

- **Tool Overview**: bam-tide is a high-performance Rust tool for converting BAM files to BigWig coverage tracks, serving as a fast alternative to deepTools bamCoverage.

- **Speed**: Optimized for speed using Rust, significantly faster than Python-based alternatives.

- **Coverage Normalization**: Supports various normalization methods including CPM, RPKM, and BPM.

- **BigWig Output**: Generates BigWig files suitable for genome browser visualization.

## Pitfalls

- **Index Required**: BAM files must be indexed (.bai) before processing.

- **Memory Usage**: Large genomes require substantial memory for coverage calculation.

- **Strand Specificity**: By default, combines both strands. Use options for strand-specific coverage.

## Examples

### Basic coverage track
**Args:** `bam_tide -i alignments.bam -o coverage.bigWig`
**Explanation:** Generates BigWig coverage track from BAM file.

### Normalized coverage
**Args:** `bam_tide -i alignments.bam -o coverage.bigWig --normalize CPM`
**Explanation:** Normalizes coverage to counts per million (CPM).

### Strand-specific coverage
**Args:** `bam_tide -i alignments.bam -o forward.bigWig --strand forward`
**Explanation:** Generates coverage track for forward strand only.

### Bin size specification
**Args:** `bam_tide -i alignments.bam -o coverage.bigWig --bin-size 50`
**Explanation:** Uses 50bp bins for coverage calculation instead of default.

### Quality filtering
**Args:** `bam_tide -i alignments.bam -o coverage.bigWig --min-mapping-quality 30`
**Explanation:** Includes only reads with mapping quality ≥30 in coverage calculation.
