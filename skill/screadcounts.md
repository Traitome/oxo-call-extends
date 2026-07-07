---
name: screadcounts
category: single-cell
description: SCReadCounts - Cell-level assessment of read counts from scRNA-seq data
tags: ["screadcounts", "single-cell", "RNA-seq", "read-counts"]
author: oxo-call-community
source_url: "https://horvathlab.github.io/NGS/SCReadCounts"
---

## Concepts

- **Tool Overview**: SCReadCounts (v1.4.2) is a computational tool for cell-level assessment of read counts from single cell RNA sequencing data.
- **Core Function**: Counts reads bearing specific nucleotides at genomic positions of interest.
- **Algorithm**: Uses BAM alignment data to count allele-specific reads per cell.
- **Input/Output**: Accepts BAM files and produces cell-level read counts.
- **Single-Cell Focus**: Specifically designed for single-cell RNA-seq analysis.
- **Applications**: Allele-specific expression, single-cell variant analysis, and RNA editing detection.

## Pitfalls

- **Data Quality**: Results depend on sequencing depth and alignment quality.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Annotation Quality**: Depends on accurate gene annotation.
- **False Positives**: May report false allele-specific events.

## Examples

### Basic counting
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -o counts.tsv`
**Explanation:** `-i` input BAM; `-g` annotation GTF; `-o` output counts.

### With variants
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -v variants.vcf -o counts.tsv`
**Explanation:** `-v` specifies VCF with variants of interest.

### Quality filtering
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -q 20 -o counts.tsv`
**Explanation:** `-q 20` filters reads with quality below 20.

### Verbose logging
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -v -o counts.tsv`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -t 8 -o counts.tsv`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Output format
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -f csv -o counts.csv`
**Explanation:** `-f csv` outputs CSV format instead of TSV.

### Targeted regions
**Args:** `screadcounts -i aligned.bam -g annotation.gtf -r targets.bed -o counts.tsv`
**Explanation:** `-r` BED file with target regions.