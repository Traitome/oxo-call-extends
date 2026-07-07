---
name: superstr
category: variant-calling
description: A lightweight, alignment-free utility for detecting repeat-containing reads in sequencing data.
tags: [superstr, str-detection, repeat-analysis, alignment-free]
author: oxo-call-community
source_url: "https://github.com/bahlolab/superSTR"
---

## Concepts

- **Tool Overview**: superstr (v1.0.1) detects repeat-containing reads in sequencing data without alignment.
- **Core Function**: Identifies reads containing short tandem repeats (STRs).
- **Algorithm**: Uses alignment-free k-mer based approach for repeat detection.
- **Input/Output**: Input: FASTQ reads; Output: Repeat-containing reads or statistics.
- **Applications**: STR analysis, variant calling, genome analysis, population genetics.
- **Installation**: `conda install -c bioconda superstr` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect detection accuracy.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Repeat Size**: Optimal for specific repeat sizes.
- **False Positives**: May detect false positive repeats.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.

## Examples

### Display help
**Args:** `superstr --help`
**Explanation:** Shows available options and usage information.

### Basic STR detection
**Args:** `superstr -i reads.fastq -o str_reads.fastq`
**Explanation:** Detect STR-containing reads from FASTQ.

### With repeat database
**Args:** `superstr -i reads.fastq -o str_reads.fastq -d repeats.txt`
**Explanation:** Use custom repeat database.

### Verbose mode
**Args:** `superstr -i reads.fastq -o str_reads.fastq -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `superstr -i reads.fastq -o stats.txt --stats`
**Explanation:** Generate statistics about STR detection.

### Batch processing
**Args:** `superstr -i fastqs/ -o results/`
**Explanation:** Process multiple FASTQ files together.

### Filter by quality
**Args:** `superstr -i reads.fastq -o str_reads.fastq -q 20`
**Explanation:** Filter reads by quality score.

### Include flanking regions
**Args:** `superstr -i reads.fastq -o str_reads.fastq -f 50`
**Explanation:** Include 50bp flanking regions.

### Generate report
**Args:** `superstr -i reads.fastq -o str_reads.fastq --report`
**Explanation:** Generate comprehensive HTML report.
