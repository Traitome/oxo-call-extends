---
name: nanoget
category: qc
description: NanoGet - Extract statistics from Oxford Nanopore sequencing data and alignments
tags: [nanoget, qc, nanopore, extraction, statistics, metrics]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanoget"
---

## Concepts

- **Tool Overview**: NanoGet v1.19.4 is a Python library and command-line tool for extracting statistics from Oxford Nanopore sequencing data and alignments. It provides comprehensive metrics for quality control.
- **Core Function**: Parses FASTQ, BAM, and sequencing summary files to extract read length distributions, quality scores, mapping statistics, and other key metrics.
- **Algorithm**: Efficiently parses sequencing files using optimized parsing libraries. Computes descriptive statistics and can generate summary reports.
- **Input Format**: Accepts FASTQ (gzipped or uncompressed), BAM (aligned reads), and sequencing summary files from Nanopore sequencers.
- **Output**: Produces tab-separated values (TSV) files with extracted metrics, suitable for further analysis or visualization.
- **Use Case**: Quality control reporting, pipeline integration, generating summary statistics for sequencing runs, and tracking sequencing performance.

## Pitfalls

- **File Compression**: Ensure input files are properly formatted. Mixed compression may cause parsing errors.
- **BAM Requirements**: BAM files must be sorted and indexed for accurate mapping statistics.
- **Memory Usage**: Processing very large files requires sufficient memory. Consider subsampling for extremely large datasets.
- **Sequencing Summary**: Requires properly formatted sequencing summary files from Guppy or Albacore basecallers.
- **Quality Scores**: Assumes standard phred quality encoding. Non-standard encodings may produce incorrect statistics.
- **Duplicate Reads**: Does not automatically remove duplicate reads. Consider deduplication before statistics extraction.

## Examples

### Extract from FASTQ
**Args:** `-i reads.fastq.gz -o stats.tsv`
**Explanation:** Extracts read statistics (length, quality) from FASTQ file.

### Extract from BAM
**Args:** `-b aligned.bam -o alignment_stats.tsv`
**Explanation:** Extracts alignment statistics including mapping rates and coverage.

### Extract from sequencing summary
**Args:** `-s sequencing_summary.txt -o run_stats.tsv`
**Explanation:** Generates comprehensive statistics from sequencing summary file.

### Combine multiple inputs
**Args:** `-i reads.fastq.gz -b aligned.bam -o combined_stats.tsv`
**Explanation:** Combines statistics from both FASTQ and BAM files.

### Display help
**Args:** `nanoget --help`
**Explanation:** Shows all available options for statistics extraction.
