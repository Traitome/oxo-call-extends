---
name: cramino
category: qc
description: Fast quality assessment tool for long-read BAM/CRAM files using rust-htslib with gap-compressed identity metrics
tags: [cramino, qc, BAM, CRAM, long-reads, nanopore, pacbio, sequencing-quality]
author: oxo-call-community
source_url: "https://github.com/wdecoster/cramino"
---

## Concepts

- **Tool Overview**: cramino is a fast quality assessment tool for BAM/CRAM files, optimized for long-read sequencing data from Oxford Nanopore and PacBio platforms.
- **Core Function**: Extracts and reports sequencing quality metrics including read length statistics, coverage, sequence identity, and gap-compressed identity for long reads.
- **Algorithm**: Uses rust-htslib for high-performance BAM/CRAM parsing; calculates gap-compressed identity that counts consecutive alignment gaps as single differences (important for long reads with structural variants).
- **Input**: BAM or CRAM files (alignment files from long-read aligners like minimap2).
- **Output**: Quality metrics table including read count, mean/median length, N50, coverage, identity percentages, phasing metrics.
- **Application**: Long-read sequencing QC, nanopore/pacbio quality control, structural variant analysis validation, population-scale sequencing metrics.
- **Installation**: `conda install -c bioconda cramino` or download pre-built binaries from GitHub releases

## Pitfalls

- **Reference Required**: For identity calculations, CRAM files require reference genome access via REF_PATH or local cache.
- **Alignment Quality**: Metrics are only meaningful for aligned reads; unaligned reads skew statistics.
- **Memory Usage**: Very large files may require significant memory despite optimized parsing.
- **Identity Calculation**: Long reads with structural variants benefit from gap-compressed identity rather than standard alignment identity.

## Examples

### Basic quality assessment
**Args:** `cramino input.bam`
**Explanation:** Reports quality metrics for the BAM file including read lengths, coverage, and identity.

### Specify output file
**Args:** `cramino input.cram -o quality_report.txt`
**Explanation:** Writes quality metrics to specified output file instead of stdout.

### Generate read length histograms
**Args:** `cramino input.bam --hist`
**Explanation:** Produces histogram data of read lengths for distribution visualization.

### Filter by minimum read length
**Args:** `cramino input.bam -m 1000`
**Explanation:** Only includes reads >= 1000 bp in quality calculations.

### Calculate sex determination metrics
**Args:** `cramino input.bam --sex`
**Explanation:** Calculates normalized read counts per chromosome for biological sex evaluation.

### Output in JSON format
**Args:** `cramino input.bam --json`
**Explanation:** Exports metrics in JSON format for downstream processing.

### Get phasing metrics
**Args:** `cramino input.bam --phasing`
**Explanation:** Reports read phasing performance metrics (useful for haplotyping applications).

### Multiple files comparison
**Args:** `cramino file1.bam file2.bam --compare`
**Explanation:** Compares quality metrics between multiple BAM files side-by-side.

### Calculate MD5 checksum
**Args:** `cramino input.bam --md5`
**Explanation:** Reports MD5 checksum of the file for integrity verification.

### Output Arrow format
**Args:** `cramino input.bam --arrow output.arrow`
**Explanation:** Exports data in Apache Arrow format for interoperability with other tools.
