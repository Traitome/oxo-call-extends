---
name: mageck
category: qc
description: MAGeCK (Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout), an algorithm to process, QC, analyze and visualize CRISPR screening data.
tags: [mageck, qc, CRISPR, screening]
author: oxo-call-community
source_url: "https://mageck.sourceforge.net"
---

## Concepts

- **Tool Overview**: mageck v0.5.9.5 - MAGeCK (Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout), a comprehensive tool for processing, QC, analyzing and visualizing CRISPR screening data.
- **Core Function**: Identifies essential genes from CRISPR-Cas9 knockout screens using robust statistical models.
- **Input/Output**: Input: FASTQ files, sgRNA library files; Output: Gene essentiality scores, statistical significance, visualizations.
- **Installation**: `conda install -c bioconda mageck`
- **Robust Ranking**: Uses Robust Rank Aggregation (RRA) to identify essential genes.
- **Quality Control**: Provides comprehensive QC metrics for screening experiments.

## Pitfalls

- **Library Design**: Poor sgRNA library design affects screen quality.
- **Mapping Quality**: Low mapping rates can introduce false positives.
- **Read Depth**: Insufficient sequencing depth reduces statistical power.
- **Off-target Effects**: Unaccounted off-target effects can confound results.
- **Batch Effects**: Variation between replicates requires proper normalization.
- **Control Selection**: Inappropriate control samples affect normalization.

## Examples

### Count sgRNA reads
**Args:** `mageck count -l library.txt -n output --fastq test1.fastq test2.fastq`
**Explanation:** Counts sgRNA reads from FASTQ files.

### Test gene essentiality
**Args:** `mageck test -k output.count.txt -t treatment -c control -n result`
**Explanation:** Tests for gene essentiality between treatment and control.

### With normalization
**Args:** `mageck test -k output.count.txt -t treatment -c control -n result --norm-method total`
**Explanation:** Uses total read count normalization.

### Multiple comparisons
**Args:** `mageck mle -k output.count.txt -n mle_result`
**Explanation:** Uses maximum likelihood estimation for multiple conditions.

### Generate QC report
**Args:** `mageck qc -k output.count.txt -n qc_report`
**Explanation:** Generates quality control report.

### Visualize results
**Args:** `mageck vis -i result.gene_summary.txt -o plot.pdf`
**Explanation:** Creates visualization of gene essentiality scores.