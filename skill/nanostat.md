---
name: nanostat
category: qc
description: NanoStat calculates comprehensive statistics for Oxford Nanopore sequencing data and alignments.
tags: [nanostat, qc, nanopore, statistics, summary]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanostat"
---

## Concepts

- **Tool Overview**: NanoStat v1.6.0 is a quality control tool for generating summary statistics from Oxford Nanopore sequencing data.
- **Core Function**: Calculates read length distributions, quality scores, alignment statistics, and base composition metrics.
- **Algorithm**: Parses sequencing data files and computes descriptive statistics using efficient data processing techniques.
- **Input Format**: Accepts FASTQ (gzipped), BAM alignments, sequencing summary files, or even directly from MinKNOW.
- **Output**: Produces comprehensive text reports with statistics tables and optionally plots in various formats.
- **Use Case**: Quality assessment of Nanopore sequencing runs, batch processing QC reports, pipeline integration.

## Pitfalls

- **Version Differences**: Command-line options may vary between different versions.
- **Input Requirements**: Requires properly formatted input files with valid quality scores.
- **Memory Usage**: Processing large datasets can require significant memory.
- **Alignment Dependencies**: BAM statistics require sorted and indexed alignments.
- **Compression Issues**: Gzipped files need proper handling to avoid decompression errors.
- **Output Format**: Default output may need post-processing for custom reporting.

## Examples

### Display help
**Args:** `nanostat --help`
**Explanation:** Shows available options and usage instructions.

### Stats from FASTQ
**Args:** `nanostat -i reads.fastq.gz -o stats.txt`
**Explanation:** Calculates read statistics from gzipped FASTQ file.

### Stats from BAM
**Args:** `nanostat -b aligned.bam -o alignment_stats.txt`
**Explanation:** Calculates alignment statistics from BAM file.

### Stats from sequencing summary
**Args:** `nanostat -s sequencing_summary.txt -o summary_stats.txt`
**Explanation:** Generates statistics from MinKNOW sequencing summary file.

### Multiple input files
**Args:** `nanostat -i reads1.fastq.gz reads2.fastq.gz -o combined_stats.txt`
**Explanation:** Combines statistics from multiple FASTQ files.

### Generate plot
**Args:** `nanostat -i reads.fastq.gz --plot -o stats/`
**Explanation:** Generates statistics report with visual plots.