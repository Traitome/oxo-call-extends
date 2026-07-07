---
name: mapula
category: alignment
description: Calculation of alignment statistics
tags: [mapula, alignment, statistics]
author: oxo-call-community
source_url: "https://github.com/epi2me-labs/mapula"
---

## Concepts

- **Tool Overview**: mapula v2.1.2 - A tool for calculating comprehensive alignment statistics from sequencing data.
- **Core Function**: Computes various alignment metrics and statistics from BAM/SAM files.
- **Input/Output**: Input: BAM/SAM alignment files; Output: Statistics reports, quality metrics.
- **Installation**: `conda install -c bioconda mapula`
- **Alignment Metrics**: Calculates mapping quality, coverage, and other alignment statistics.
- **Quality Assessment**: Provides quality assessment metrics for sequencing data.

## Pitfalls

- **Alignment Quality**: Poor quality alignments affect statistics.
- **File Format**: Requires properly formatted BAM/SAM files.
- **Memory Usage**: Large BAM files require significant memory.
- **Reference Genome**: Must use the same reference for consistency.
- **Duplicate Reads**: Unmarked duplicates may affect coverage statistics.
- **Parameter Selection**: Incorrect parameters affect metric calculation.

## Examples

### Calculate alignment statistics
**Args:** `mapula -i aligned.bam -o stats.txt`
**Explanation:** Computes alignment statistics from BAM file.

### With coverage analysis
**Args:** `mapula -i aligned.bam -o stats.txt --coverage`
**Explanation:** Includes coverage statistics.

### Multiple BAM files
**Args:** `mapula -i bams/ -o stats.txt`
**Explanation:** Processes multiple BAM files.

### Verbose mode
**Args:** `mapula -i aligned.bam -o stats.txt -v`
**Explanation:** Provides detailed logging during analysis.

### Generate plot
**Args:** `mapula -i aligned.bam -o stats.txt --plot plot.pdf`
**Explanation:** Generates visualization of statistics.

### Filter by quality
**Args:** `mapula -i aligned.bam -o stats.txt -q 30`
**Explanation:** Filters reads with mapping quality >= 30.