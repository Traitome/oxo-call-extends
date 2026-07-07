---
name: mark-nonconverted-reads
category: qc
description: A simple filter to mark potential nonconverted reads from methylation experiments
tags: [mark-nonconverted-reads, qc, methylation]
author: oxo-call-community
source_url: "https://github.com/nebiolabs/mark-nonconverted-reads"
---

## Concepts

- **Tool Overview**: mark-nonconverted-reads v1.2 - A filter to identify and mark potential nonconverted reads from bisulfite sequencing experiments.
- **Core Function**: Detects reads that may not have undergone bisulfite conversion in methylation experiments.
- **Input/Output**: Input: FASTQ/BAM files; Output: Marked reads, statistics, filtered files.
- **Installation**: `conda install -c bioconda mark-nonconverted-reads`
- **Bisulfite Conversion**: Identifies non-converted reads in bisulfite sequencing data.
- **Quality Control**: Provides quality control metrics for methylation experiments.

## Pitfalls

- **Conversion Rate**: Low conversion rates affect detection accuracy.
- **Read Quality**: Poor quality reads produce false positives.
- **Reference Genome**: Must use appropriate reference genome.
- **Parameter Tuning**: Incorrect thresholds affect sensitivity.
- **Memory Usage**: Large datasets require significant memory.
- **False Positives**: May incorrectly mark converted reads.

## Examples

### Mark nonconverted reads
**Args:** `mark-nonconverted-reads -i reads.fastq -o marked.fastq`
**Explanation:** Identifies and marks nonconverted reads.

### With BAM input
**Args:** `mark-nonconverted-reads -i aligned.bam -o marked.bam`
**Explanation:** Processes BAM alignment file.

### With statistics
**Args:** `mark-nonconverted-reads -i reads.fastq -o marked.fastq -s stats.txt`
**Explanation:** Generates conversion statistics.

### Verbose mode
**Args:** `mark-nonconverted-reads -i reads.fastq -o marked.fastq -v`
**Explanation:** Provides detailed logging during analysis.

### Filter mode
**Args:** `mark-nonconverted-reads -i reads.fastq -o filtered.fastq --filter`
**Explanation:** Filters out nonconverted reads.

### Custom threshold
**Args:** `mark-nonconverted-reads -i reads.fastq -o marked.fastq -t 0.1`
**Explanation:** Sets conversion threshold to 0.1.