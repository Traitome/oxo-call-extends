---
name: demultiplex
category: utility
description: demultiplex - demultiplex FASTA/FASTQ files based on barcode lists.
tags: [demultiplex, utility, barcoding, fastq, fasta]
author: oxo-call-community
source_url: "https://github.com/jfjlaros/demultiplex"
---

## Concepts

- **Tool Overview**: demultiplex (v1.2.2+) is a tool for demultiplexing FASTA/FASTQ files based on barcode sequences. It provides flexible barcode matching for various sequencing protocols.
- **Core Function**: Splits sequencing reads into separate files based on user-provided barcode sequences, supporting multiple barcode locations and mismatch tolerances.
- **Input/Output**: Input: FASTA/FASTQ files (single-end or paired-end), barcode list file. Output: Demultiplexed read files per sample, summary statistics.
- **Algorithm**: Uses exact or fuzzy barcode matching to assign reads to samples, with configurable mismatch tolerance and quality filtering.
- **Key Features**: Supports multiple barcode formats, mismatch tolerance, paired-end reads, quality filtering, batch processing, detailed reporting.
- **Installation**: `conda install -c bioconda demultiplex`

## Pitfalls

- **Input Requirements**: Requires properly formatted barcode list matching read structure.
- **Barcode Quality**: Poor quality barcodes may affect demultiplexing accuracy.
- **Mismatch Tolerance**: Too lenient settings may cause misassignment.
- **Read Headers**: Barcodes in headers require specific format.
- **Output Management**: Generates multiple output files per sample.

## Examples

### Demultiplex reads by barcodes
**Args:** `demultiplex --input reads.fq --barcodes barcodes.txt --output output_dir/`
**Explanation:** Demultiplexes reads based on barcode sequences.

### With mismatch tolerance
**Args:** `demultiplex --input reads.fq --barcodes barcodes.txt --output output_dir/ --mismatches 1`
**Explanation:** Allow single mismatch in barcode matching.

### Paired-end mode
**Args:** `demultiplex --input R1.fq R2.fq --barcodes barcodes.txt --output output_dir/ --paired`
**Explanation:** Demultiplex paired-end reads keeping pairs together.