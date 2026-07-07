---
name: sctools
category: single-cell
description: SCTools - Suite of utility tools for single-cell sequencing data
tags: ["sctools", "single-cell", "utility", "processing"]
author: oxo-call-community
source_url: "https://github.com/bioinformatics-polito/SCTools"
---

## Concepts

- **Tool Overview**: SCTools (v1.0.0) is a suite of tools performing utility operations over single-cell samples.
- **Core Function**: Provides various utility operations for single-cell sequencing data processing.
- **Algorithm**: Implements various algorithms for quality control and data manipulation.
- **Input/Output**: Accepts BAM/SAM files and produces processed outputs.
- **Single-Cell Focus**: Specifically designed for single-cell sequencing data.
- **Applications**: Quality control, filtering, and preprocessing of single-cell data.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on input data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Basic processing
**Args:** `sctools process -i input.bam -o output.bam`
**Explanation:** `-i` input BAM; `-o` output BAM.

### Quality filtering
**Args:** `sctools filter -i input.bam -q 20 -o filtered.bam`
**Explanation:** `-q 20` filters reads with quality below 20.

### Sort BAM
**Args:** `sctools sort -i input.bam -o sorted.bam`
**Explanation:** Sorts BAM file by coordinate.

### Index BAM
**Args:** `sctools index -i sorted.bam`
**Explanation:** Creates index for sorted BAM file.

### Verbose logging
**Args:** `sctools process -i input.bam -v -o output.bam`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sctools process -i input.bam -t 8 -o output.bam`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Statistics
**Args:** `sctools stats -i input.bam -o stats.csv`
**Explanation:** Generates statistics report.