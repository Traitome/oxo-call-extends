---
name: alnstats
category: alignment
description: A high-performance command-line tool designed to calculate yield and duplicate statistics from BAM, SAM, or CRAM alignment files
tags: [alnstats, alignment, BAM, SAM, CRAM, statistics, QC]
author: oxo-call-community
source_url: "https://github.com/Poshi/alnstats"
---

## Concepts

- **Tool Overview**: alnstats is a high-performance command-line tool designed to calculate yield and duplicate statistics from BAM, SAM, or CRAM alignment files, providing essential quality control metrics for sequencing data analysis.
- **Core Function**: Computes comprehensive alignment statistics including read counts, mapping rates, duplicate rates, insert sizes, and quality metrics from alignment files.
- **Input/Output**: Input: BAM/SAM/CRAM alignment files. Output: Tabular statistics report with quality control metrics.
- **Key Features**: High-performance parsing, support for multiple alignment formats, comprehensive QC metrics, duplicate detection, insert size distribution analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda alnstats`

## Pitfalls

- **BAM Index**: BAM files should be indexed for efficient random access.
- **CRAM Support**: CRAM files may require reference genome for decoding.
- **Memory Usage**: Processing large alignment files requires sufficient memory.
- **Duplicate Marking**: Duplicate statistics depend on properly marked duplicates in the input file.
- **Quality Scores**: Ensure input files have proper quality score encoding.

## Examples

### Display help information
**Args:** `alnstats --help`
**Explanation:** Shows available command-line options and usage instructions.

### Basic statistics
**Args:** `alnstats -i input.bam -o stats.txt`
**Explanation:** Computes alignment statistics from BAM file and saves to output file.

### Multiple input files
**Args:** `alnstats -i sample1.bam sample2.bam sample3.bam -o combined_stats.txt`
**Explanation:** Processes multiple BAM files and generates combined statistics.

### Include duplicate statistics
**Args:** `alnstats -i input.bam -o stats.txt --duplicates`
**Explanation:** Computes detailed duplicate statistics including duplicate rate.

### Generate insert size distribution
**Args:** `alnstats -i input.bam -o stats.txt --insert-size`
**Explanation:** Calculates insert size distribution metrics.

### Set minimum mapping quality
**Args:** `alnstats -i input.bam -o stats.txt -q 30`
**Explanation:** Filters reads with mapping quality >= 30 for statistics calculation.

### Output JSON format
**Args:** `alnstats -i input.bam -o stats.json --json`
**Explanation:** Outputs statistics in JSON format for programmatic processing.

### Verbose mode
**Args:** `alnstats -i input.bam -o stats.txt -v`
**Explanation:** Runs with verbose output showing detailed processing information.

### Include coverage statistics
**Args:** `alnstats -i input.bam -o stats.txt --coverage`
**Explanation:** Computes coverage depth statistics across the genome.

### Process CRAM file
**Args:** `alnstats -i input.cram -r reference.fasta -o stats.txt`
**Explanation:** Processes CRAM file with reference genome for decoding.
