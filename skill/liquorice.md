---
name: liquorice
category: epigenomics
description: LIQUORICE - Bias correction and quantification of cfDNA WGS coverage changes
tags: [liquorice, epigenomics, cfDNA, WGS, coverage, bias-correction]
author: oxo-call-community
source_url: "https://github.com/epigen/LIQUORICE"
---

## Concepts

- **cfDNA Analysis**: Analysis of cell-free DNA sequencing data
- **Bias Correction**: Corrects sequencing biases in cfDNA data
- **Coverage Quantification**: Quantifies coverage changes around regions of interest
- **WGS Analysis**: Whole-genome sequencing data analysis
- **Epigenetic Analysis**: Epigenetic profiling using cfDNA
- **Region of Interest**: Focused analysis on specific genomic regions

## Pitfalls

- **GC Bias**: GC content bias affects coverage
- **Mappability**: Low mappability regions may cause issues
- **Sample Quality**: Poor quality cfDNA affects results
- **Normalization**: Requires proper normalization
- **Parameter Tuning**: Requires careful parameter optimization
- **Memory Usage**: Memory-intensive for large datasets

## Examples

### Analyze cfDNA coverage
**Args:** `liquorice -i input.bam -o output.txt -r regions.bed`
**Explanation:** Analyzes coverage around regions of interest.

### Bias correction
**Args:** `liquorice -i input.bam -o output.txt -r regions.bed -b`
**Explanation:** Applies bias correction to coverage data.

### Normalization
**Args:** `liquorice -i input.bam -o output.txt -r regions.bed -n`
**Explanation:** Normalizes coverage values.

### Threads
**Args:** `liquorice -i input.bam -o output.txt -r regions.bed -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### GC correction
**Args:** `liquorice -i input.bam -o output.txt -r regions.bed -g`
**Explanation:** Applies GC content bias correction.

### Plot results
**Args:** `liquorice -i input.bam -o output.pdf -r regions.bed -p`
**Explanation:** Generates coverage plot.