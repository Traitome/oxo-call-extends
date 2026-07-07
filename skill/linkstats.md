---
name: linkstats
category: qc
description: LinkStats - Collect and process statistics from aligned linked-reads
tags: [linkstats, qc, linked-reads, statistics, bioinformatics, sequencing]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/LinkStats"
---

## Concepts

- **Linked-read Analysis**: Analysis of 10X Genomics linked-read data
- **Statistical Analysis**: Collects statistics from aligned reads
- **Barcode Statistics**: Analyzes molecular barcode distribution
- **Coverage Analysis**: Assesses sequencing coverage
- **Quality Control**: Quality control for linked-read data
- **Library Complexity**: Estimates library complexity

## Pitfalls

- **Alignment Quality**: Poor alignment affects statistics
- **Barcode Quality**: Low-quality barcodes affect results
- **Duplicate Reads**: PCR duplicates may skew statistics
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Output Interpretation**: Results require careful interpretation

## Examples

### Collect statistics
**Args:** `linkstats -i aligned.bam -o stats.txt`
**Explanation:** Collects statistics from aligned linked-reads.

### Barcode distribution
**Args:** `linkstats -i aligned.bam -o barcode_stats.txt -b`
**Explanation:** Outputs barcode distribution statistics.

### Coverage analysis
**Args:** `linkstats -i aligned.bam -o coverage.txt -c`
**Explanation:** Performs coverage analysis.

### Library complexity
**Args:** `linkstats -i aligned.bam -o complexity.txt -l`
**Explanation:** Estimates library complexity.

### Threads
**Args:** `linkstats -i aligned.bam -o stats.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### BED region
**Args:** `linkstats -i aligned.bam -o stats.txt -r regions.bed`
**Explanation:** Analyzes specific genomic regions.