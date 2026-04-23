---
name: bwa-fastalign
category: alignment
description: Faster version of BWA-MEM with identical outputs on commercial CPUs
tags: [bwa, alignment, fast, optimization]
author: oxo-call-community
source_url: "https://github.com/zzhofict/BWA-FastAlign"
---

## Concepts

- **Tool Overview**: BWA-FastAlign is an optimized version of BWA-MEM with faster execution.
- **Core Function**: Maps reads to reference genome with identical output to BWA-MEM.
- **Optimization**: Uses SIMD instructions and algorithmic improvements for speedup.
- **Compatibility**: Produces identical results to BWA-MEM for reproducibility.
- **Installation**: Install via bioconda: `conda install -c bioconda bwa-fastalign`

## Pitfalls

- **Index Format**: May require rebuilding indexes for optimized format.
- **CPU Requirements**: Requires modern CPU with SIMD support for full speedup.
- **Compatibility**: Verify output matches BWA-MEM for critical analyses.

## Examples

### Align reads with FastAlign
**Args:** `bwa-fastalign mem -t 8 reference.fa R1.fq R2.fq > aligned.sam`
**Explanation:** Aligns paired-end reads using optimized BWA-MEM algorithm.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
