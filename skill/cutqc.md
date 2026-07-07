---
name: cutqc
category: qc
description: CutQC generates aggregated FASTQC reports comparing raw and trimmed sequencing data for quality assessment
tags: [cutqc, qc, FASTQ, quality-control, trimming, perl, aggregation]
author: oxo-call-community
source_url: "https://github.com/obenno/cutqc"
---

## Concepts

- **Tool Overview**: CutQC (v0.07) generates aggregated FASTQC reports comparing before and after trimming quality metrics.
- **Core Function**: Processes multiple samples by running FastQC on raw and trimmed reads, then creates aggregated summary reports.
- **Input/Output**: Input: FASTQ files or sample list; Output: aggregated HTML reports comparing QC metrics pre/post trimming
- **Perl-based**: Written in Perl, requires FastQC to be installed and in PATH
- **Installation**: `conda install -c bioconda cutqc`

## Pitfalls

- **FastQC Dependency**: Must have FastQC installed and accessible in PATH for cutqc to function
- **File Format**: Input samples file should be in tab-separated format with sample names and file paths
- **Output Structure**: Creates separate directories for raw and trimmed FastQC results before aggregation
- **Perl Modules**: Requires standard Perl modules (Getopt::Long) which are usually pre-installed

## Examples

### Display help
**Args:** `cutqc --help`
**Explanation:** Show all available options and usage information.

### Basic usage with sample file
**Args:** `cutqc -s samples.txt -o cutqc_results/`
**Explanation:** Run with a tab-delimited sample file containing sample names and FASTQ paths.

### Single-end data
**Args:** `cutqc -s samples_se.txt -o results_se/`
**Explanation:** Process single-end sequencing data; each line has sample name and read file path.

### Paired-end data
**Args:** `cutqc -s samples_pe.txt -p -o results_pe/`
**Explanation:** Process paired-end data with `-p` flag; each sample has R1 and R2 files in the sample file.

### Run with custom thread count
**Args:** `cutqc -s samples.txt -o results/ -t 4`
**Explanation:** Specify number of threads for parallel FastQC execution.

### Aggregate from existing FastQC results
**Args:** `cutqc -r raw_fastqc/ -t trimmed_fastqc/ -o aggregated_report/`
**Explanation:** Use `-r` and `-t` to aggregate from existing FastQC output directories.
