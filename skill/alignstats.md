---
name: alignstats
category: alignment
description: Comprehensive alignment, whole-genome coverage, and capture coverage statistics for SAM/BAM/CRAM files
tags: [alignstats, alignment-statistics, BAM, coverage, quality-control]
author: oxo-call-community
source_url: "https://github.com/jfarek/alignstats"
---

## Concepts

- **Tool Overview**: AlignStats is a tool for generating comprehensive alignment statistics, whole-genome coverage metrics, and capture coverage statistics from sequence alignment files.
- **Core Function**: Produces alignment metrics, coverage statistics, insert size distribution, and quality metrics for SAM, BAM, and CRAM format files.
- **Input Formats**: SAM, BAM, CRAM alignment files
- **Output**: Text report with alignment statistics, coverage metrics, and quality control information
- **Key Metrics**: Total reads, mapped reads, duplicate reads, insert size distribution, coverage depth, GC content, mapping quality distribution
- **Installation**: Install via bioconda: `conda install -c bioconda alignstats`
- **License**: BSD-3-Clause

## Pitfalls

- **BAM Index Required**: Input BAM files must be indexed with corresponding .bai file.
- **Sorted Files**: BAM files should be coordinate-sorted for optimal performance.
- **Memory Usage**: For very large BAM files, use `-n` option to limit records in memory.
- **Target Regions**: For capture coverage analysis, provide BED file with target regions.
- **Quality Filtering**: Default mapping quality filter may exclude low-quality alignments.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and usage instructions.

### Basic alignment statistics
**Args:** `alignstats -i input.bam -o report.txt`
**Explanation:** Generates comprehensive alignment statistics report from BAM file.

### Capture coverage mode
**Args:** `alignstats -C -i input.bam -t targets.bed -o capture_report.txt`
**Explanation:** Analyzes capture coverage using target regions from BED file.

### Specify regions of interest
**Args:** `alignstats -i input.bam -r chr1:1-1000000 -o region_report.txt`
**Explanation:** Limits analysis to specific genomic region.

### Set minimum mapping quality
**Args:** `alignstats -i input.bam -q 30 -o report.txt`
**Explanation:** Only includes reads with mapping quality >= 30.

### Include unmapped reads
**Args:** `alignstats -i input.bam -U -o report.txt`
**Explanation:** Includes statistics for unmapped reads in the report.

### Include duplicate reads
**Args:** `alignstats -i input.bam -D -o report.txt`
**Explanation:** Includes duplicate reads in statistics calculation.

### Verbose output
**Args:** `alignstats -v -i input.bam -o report.txt`
**Explanation:** Prints verbose runtime information to stderr.

### Set memory limit
**Args:** `alignstats -i input.bam -n 1000000 -o report.txt`
**Explanation:** Limits maximum number of records in memory to 1,000,000.

### Whole-genome coverage analysis
**Args:** `alignstats -W -i input.bam -o genome_report.txt`
**Explanation:** Performs whole-genome coverage analysis.

### Filter by flags
**Args:** `alignstats -i input.bam -f 0x2 -F 0x4 -o report.txt`
**Explanation:** Filters reads by SAM flags (include 0x2, exclude 0x4).

### Calculate insert size statistics
**Args:** `alignstats -i input.bam -A -o report.txt`
**Explanation:** Reports detailed insert size distribution statistics.

### Combined options
**Args:** `alignstats -C -v -q 20 -i input.bam -t targets.bed -o capture_qc.txt`
**Explanation:** Runs capture mode with verbose output and quality threshold of 20.
