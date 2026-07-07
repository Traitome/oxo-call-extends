---
name: humid
category: qc
description: HUMID -- High-performance UMI Deduplicator
tags: [humid, UMI, deduplication, FASTQ]
author: oxo-call-community
source_url: "https://humid.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: HUMID is a high-performance tool for removing duplicate reads from FASTQ files, with or without Unique Molecular Identifiers (UMIs).
- **Reference-free Deduplication**: Operates directly on FASTQ files without requiring alignment, making it ideal as a preprocessing step.
- **UMI Support**: Supports UMIs in headers (with underscore or colon delimiters) or in separate FASTQ files.
- **Directional Method**: Uses the directional method by default to account for expected PCR errors when grouping reads by UMI.
- **Word Length Parameter**: By default uses 24 nucleotides for deduplication, adjustable with the `-n` flag.
- **Installation**: `conda install -c bioconda humid`

## Pitfalls

- **UMI Format**: Ensure UMIs are in supported formats (header with underscore/colon, or separate file); use fastp to reformat if needed.
- **Deduplication Without UMI**: Without UMIs, duplicates may be overestimated similar to Picard MarkDuplicates.
- **Word Length Selection**: Adjust word length based on read length and sequencing error rate.
- **Compressed Files**: Supports gzip-compressed FASTQ files automatically.
- **Paired-end Reads**: When using paired-end data, both files must be provided in correct order.
- **Segmentation Fault**: May occur during cluster calculation; reduce input size or adjust parameters.

## Examples

### Basic deduplication with UMIs in header
**Args:** `humid forward.fastq.gz reverse.fastq.gz`
**Explanation:** Deduplicates paired-end FASTQ files where UMIs are in the read headers.

### Deduplication with separate UMI file
**Args:** `humid forward.fastq.gz reverse.fastq.gz umi.fastq.gz`
**Explanation:** Uses a separate UMI file for deduplication of paired-end reads.

### Single-end deduplication without UMIs
**Args:** `humid single_end.fastq.gz -o deduplicated.fastq.gz`
**Explanation:** Removes duplicates from single-end reads without UMIs.

### Custom word length
**Args:** `humid forward.fastq.gz reverse.fastq.gz -n 30`
**Explanation:** Uses 30 nucleotides for deduplication instead of the default 24.

### Stream from stdin
**Args:** `cat input.fastq | humid - -o output.fastq`
**Explanation:** Reads from standard input and writes deduplicated reads to output.