---
name: bamstats
category: qc
description: Bamstats - Command line tool to compute mapping statistics from BAM files
tags: [mapping-statistics, quality-control, bam-analysis, coverage]
author: oxo-call-community
source_url: "https://github.com/guigolab/bamstats"
---

## Concepts

- **Tool Overview**: Bamstats computes comprehensive mapping statistics from BAM files, providing quality metrics for sequencing experiments.

- **Coverage Statistics**: Calculates coverage depth, breadth, and distribution across the genome.

- **Mapping Quality**: Reports mapping quality distribution and alignment statistics.

- **Read Metrics**: Provides read length distribution, duplication rates, and other quality metrics.

## Pitfalls

- **Index Required**: BAM files must be indexed before analysis.

- **Reference Needed**: Some statistics require reference genome for accurate calculation.

- **Large Files**: Very large BAM files may require substantial memory for complete statistics.

## Examples

### Basic statistics
**Args:** `bamstats -i alignments.bam -o stats.txt`
**Explanation:** Computes comprehensive mapping statistics from BAM file.

### Coverage statistics
**Args:** `bamstats -i alignments.bam --coverage -o coverage_stats.txt`
**Explanation:** Calculates detailed coverage statistics including depth distribution.

### JSON output
**Args:** `bamstats -i alignments.bam -f json -o stats.json`
**Explanation:** Outputs statistics in JSON format for programmatic processing.

### Specify regions
**Args:** `bamstats -i alignments.bam -r regions.bed -o regional_stats.txt`
**Explanation:** Computes statistics only for specified genomic regions.
