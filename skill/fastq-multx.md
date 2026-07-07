---
name: fastq-multx
category: formatting
description: "Demultiplexes a fastq. Capable of auto-determining barcode id's based on a master set fields. Keeps multiple reads in-sync during demultiplexing. Can verify that the reads are in-sync as well, and fail if they're not."
tags: [fastq-multx, formatting, demultiplexing, barcodes, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brwnj/fastq-multx"
---

## Concepts

- **Tool Overview**: fastq-multx is a tool for demultiplexing FASTQ files, capable of auto-determining barcode IDs and keeping multiple reads synchronized.
- **Core Function**: Demultiplexes pooled sequencing data into individual samples based on barcodes.
- **Input/Output**: Input: Multiplexed FASTQ files, barcode file. Output: Demultiplexed FASTQ files per sample.
- **Algorithm**: Uses barcode matching to assign reads to samples.
- **Key Features**: Auto-detection of barcodes, multi-read synchronization, verification, batch processing, quality filtering.
- **Installation**: `conda install -c bioconda fastq-multx`

## Pitfalls

- **Barcode Quality**: Poor barcode quality may cause misassignment.
- **Read Synchronization**: Requires reads to be in sync across files.
- **Barcode Mismatches**: May fail if barcodes don't match expected patterns.
- **Memory Usage**: Large files may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic demultiplexing
**Args:** `fastq-multx -b barcodes.txt reads.fastq -o samples/%_reads.fastq`
**Explanation:** Demultiplexes reads using barcode file.

### Paired-end demultiplexing
**Args:** `fastq-multx -b barcodes.txt reads_1.fastq reads_2.fastq -o samples/%_reads_1.fastq samples/%_reads_2.fastq`
**Explanation:** Demultiplexes paired-end reads.

### Allow mismatches
**Args:** `fastq-multx -b barcodes.txt reads.fastq -o samples/%_reads.fastq -m 2`
**Explanation:** Allows up to 2 barcode mismatches.

### Verify synchronization
**Args:** `fastq-multx -b barcodes.txt reads.fastq -o samples/%_reads.fastq -s`
**Explanation:** Verifies reads are synchronized.

### Quality filtering
**Args:** `fastq-multx -b barcodes.txt reads.fastq -o samples/%_reads.fastq -q 20`
**Explanation:** Filters by minimum quality score.