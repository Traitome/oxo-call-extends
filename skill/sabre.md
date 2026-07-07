---
name: sabre
category: quality_control
description: A barcode demultiplexing and trimming tool for FastQ files.
tags: ["sabre", "barcode", "demultiplexing", "FastQ", "trimming"]
author: oxo-call-community
source_url: "https://github.com/najoshi/sabre/"
---

## Concepts

- **Tool Overview**: sabre (v1.000) is a fast barcode demultiplexing tool that separates multiplexed sequencing reads based on barcodes. It supports both single-end and paired-end sequencing data.
- **Core Function**: Demultiplexes FastQ files by matching barcode sequences, allowing mismatches and trimming barcodes from reads.
- **Algorithm**: Uses exact or fuzzy matching to identify barcodes, supports multiple barcode mismatches, and efficiently processes large sequencing files.
- **Input Format**: Multiplexed FastQ files (single or paired-end), barcode file with barcode sequences and sample identifiers.
- **Output Format**: Demultiplexed FastQ files for each sample, statistics report with barcode counts.
- **Use Case**: Demultiplexing pooled sequencing libraries, removing barcode sequences from reads, quality control of multiplexed sequencing runs.

## Pitfalls

- **Barcode design**: Poorly designed barcodes can lead to misassignment.
- **Mismatch tolerance**: Too many allowed mismatches increases false positives.
- **Barcode orientation**: Must match barcode orientation (forward/reverse complement).
- **File size**: Large FastQ files require sufficient disk space for output.
- **Barcode collisions**: Similar barcodes may cause misidentification.
- **Quality trimming**: Does not perform quality trimming, may need separate tool.

## Examples

### Basic demultiplexing
**Args:** `sabre se -f input.fastq -b barcodes.txt -u unmatched.fastq`
**Explanation:** `se` single-end mode; `-f` input FastQ; `-b` barcode file; `-u` unmatched reads.

### Paired-end demultiplexing
**Args:** `sabre pe -f1 reads_1.fastq -f2 reads_2.fastq -b barcodes.txt -u1 unmatched_1.fastq -u2 unmatched_2.fastq`
**Explanation:** `pe` paired-end mode; `-f1/-f2` paired reads; `-u1/-u2` unmatched pairs.

### Allow mismatches
**Args:** `sabre se -f input.fastq -b barcodes.txt -u unmatched.fastq -m 2`
**Explanation:** `-m` maximum number of mismatches allowed (default: 0).

### Trim barcodes
**Args:** `sabre se -f input.fastq -b barcodes.txt -u unmatched.fastq --trim`
**Explanation:** `--trim` removes barcode sequences from reads after demultiplexing.

### Output statistics
**Args:** `sabre se -f input.fastq -b barcodes.txt -u unmatched.fastq -s stats.txt`
**Explanation:** `-s` outputs statistics file with barcode counts.

### Reverse complement barcodes
**Args:** `sabre se -f input.fastq -b barcodes.txt -u unmatched.fastq --rc`
**Explanation:** `--rc` matches barcodes against reverse complement.

### Gzipped input
**Args:** `sabre se -f input.fastq.gz -b barcodes.txt -u unmatched.fastq`
**Explanation:** Automatically detects and decompresses gzipped input.
