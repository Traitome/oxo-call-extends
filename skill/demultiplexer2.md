---
name: demultiplexer2
category: utility
description: demultiplexer2 - Python CLI for demultiplexing Illumina reads.
tags: [demultiplexer2, utility, demultiplexing, illumina]
author: oxo-call-community
source_url: "https://github.com/DominikBuchner/demultiplexer2"
---

## Concepts

- **Tool Overview**: demultiplexer2 (v1.1.6+) is a Python command line interface for demultiplexing Illumina sequencing reads. It separates multiplexed reads by sample barcodes.
- **Core Function**: Identifies and separates sequencing reads based on sample-specific barcodes, enabling processing of multiple samples in a single sequencing run.
- **Input/Output**: Input: FASTQ files (paired-end or single-end), barcode file. Output: Demultiplexed FASTQ files per sample.
- **Algorithm**: Uses barcode matching algorithms to assign reads to samples, with configurable mismatch tolerance.
- **Key Features**: Supports paired-end reads, barcode mismatch tolerance, quality filtering, batch processing, detailed statistics.
- **Installation**: `conda install -c bioconda demultiplexer2`

## Pitfalls

- **Input Requirements**: Requires properly formatted Illumina FASTQ files with barcodes.
- **Barcode Quality**: Poor barcode quality may affect demultiplexing accuracy.
- **Mismatch Tolerance**: Too lenient mismatch settings may cause misassignment.
- **Index Hopping**: May be affected by index hopping in multiplexed sequencing.
- **Read Pair Consistency**: Requires matching barcodes for paired-end reads.

## Examples

### Demultiplex paired-end reads
**Args:** `demultiplexer2 --input R1.fq R2.fq --barcodes barcodes.tsv --output output_dir/`
**Explanation:** Demultiplexes paired-end Illumina reads by barcodes.

### With mismatch tolerance
**Args:** `demultiplexer2 --input R1.fq R2.fq --barcodes barcodes.tsv --output output_dir/ --mismatches 2`
**Explanation:** Allow up to 2 mismatches in barcode matching.

### Single-end mode
**Args:** `demultiplexer2 --input reads.fq --barcodes barcodes.tsv --output output_dir/ --single-end`
**Explanation:** Demultiplex single-end reads.