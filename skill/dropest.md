---
name: dropest
category: expression
description: "Pipeline for initial analysis of droplet-based single-cell RNA-seq data"
tags: [dropest, expression, single-cell, RNA-seq, droplet-seq]
author: oxo-call-community
source_url: "https://github.com/hms-dbmi/dropEst/"
---

## Concepts

- **Tool Overview**: dropEst is a pipeline for initial analysis of droplet-based single-cell RNA sequencing data.
- **Core Function**: Processes raw scRNA-seq data to generate gene expression matrices.
- **Input/Output**: Input: Raw sequencing reads (FASTQ), reference genome. Output: Gene expression matrix, QC metrics.
- **Algorithm**: Uses barcode whitelists, mapping, and UMI deduplication for accurate expression quantification.
- **Key Features**: Supports multiple droplet platforms, UMI-based deduplication, comprehensive QC reporting.
- **Installation**: `conda install -c bioconda dropest`

## Pitfalls

- **Barcode Whitelist**: Must use correct barcode whitelist for the sequencing platform.
- **Reference Genome**: Must match the reference genome used for alignment.
- **Read Quality**: Poor quality reads can affect cell calling accuracy.
- **Sequencing Depth**: Low coverage can reduce gene detection sensitivity.
- **Batch Effects**: Technical variation between batches should be addressed in downstream analysis.

## Examples

### Basic processing
**Args:** `--fastq reads.fastq --genome ref.fa --output counts.txt`
**Explanation:** Processes scRNA-seq reads and generates gene expression matrix.

### With UMI deduplication
**Args:** `--fastq reads.fastq --genome ref.fa --output counts.txt --umi`
**Explanation:** Enables UMI-based deduplication for accurate quantification.

### Custom barcode whitelist
**Args:** `--fastq reads.fastq --genome ref.fa --output counts.txt --barcodes whitelist.txt`
**Explanation:** Uses custom barcode whitelist for cell identification.

### QC reporting
**Args:** `--fastq reads.fastq --genome ref.fa --output counts.txt --qc qc_report.html`
**Explanation:** Generates comprehensive QC report alongside expression matrix.

### Multiple samples
**Args:** `--fastq sample1.fastq sample2.fastq --genome ref.fa --output counts.txt --merge`
**Explanation:** Processes and merges multiple samples into single expression matrix.