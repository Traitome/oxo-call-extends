---
name: barcode_splitter
category: utility
description: barcode_splitter - Split FASTQ files by matching barcodes in index reads
tags: [barcode_splitter, utility, FASTQ, demultiplexing, barcodes]
author: oxo-call-community
source_url: "https://bitbucket.org/princeton_genomics/barcode_splitter"
---

## Concepts

- **Tool Overview**: barcode_splitter (v0.18.6) splits multiple FASTQ files by matching barcodes in index reads, enabling demultiplexing of pooled sequencing data.
- **Core Function**: Demultiplexes pooled sequencing data by matching barcodes in index reads.
- **Barcode Matching**: Matches barcodes against beginning or end of specified index reads.
- **Error Tolerance**: Supports configurable mismatch tolerance for barcode matching.
- **Compression Support**: Automatically handles gzip-compressed input files.
- **Input/Output**: Accepts multiple FASTQ files; outputs demultiplexed FASTQ files by barcode.
- **Installation**: `conda install -c bioconda barcode_splitter`.

## Pitfalls

- **Barcode Position**: Barcodes must be at beginning or end of reads as specified.
- **Barcode File Format**: Requires tab-delimited barcode definition file.
- **Mismatch Setting**: Too many mismatches may cause incorrect assignment.
- **File Compression**: Ensure consistent compression across all input files.

## Examples

### Basic demultiplexing
**Args:** `barcode_splitter --bcfile barcodes.txt --reads reads.fastq --index index.fastq --outdir demultiplexed/`
**Explanation:** Splits reads by matching barcodes in index file.

### Allow mismatches
**Args:** `barcode_splitter --bcfile barcodes.txt --reads reads.fastq --index index.fastq --mismatches 2 --outdir demultiplexed/`
**Explanation:** Allows up to 2 mismatches in barcode matching.

### Barcode at end of read
**Args:** `barcode_splitter --bcfile barcodes.txt --reads reads.fastq --index index.fastq --bc-end --outdir demultiplexed/`
**Explanation:** Searches for barcodes at the end of index reads.

### Compressed input
**Args:** `barcode_splitter --bcfile barcodes.txt --reads reads.fastq.gz --index index.fastq.gz --outdir demultiplexed/`
**Explanation:** Processes gzip-compressed input files.

### Force gzip input
**Args:** `barcode_splitter --bcfile barcodes.txt --reads reads.fastq --index index.fastq --gzipin --outdir demultiplexed/`
**Explanation:** Forces gzip decompression even if files don't have .gz extension.

### Multiple read files
**Args:** `barcode_splitter --bcfile barcodes.txt --reads r1.fastq r2.fastq --index index.fastq --outdir demultiplexed/`
**Explanation:** Processes paired-end reads with single index file.

### Display help
**Args:** `barcode_splitter --help`
**Explanation:** Shows all available command-line options and usage information.