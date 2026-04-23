---
name: barbell
category: qc
description: Barbell - Extremely fast and accurate Nanopore demultiplexing
tags: [nanopore, demultiplexing, barcodes, long-reads]
author: oxo-call-community
source_url: "https://github.com/rickbeeloo/barbell"
---

## Concepts

- **Tool Overview**: Barbell is an extremely fast and accurate demultiplexing tool for Oxford Nanopore reads, using efficient barcode matching algorithms.

- **Speed Optimized**: Designed for rapid demultiplexing of large Nanopore datasets.

- **Barcode Matching**: Matches barcodes at read ends with tolerance for sequencing errors.

- **Native Barcodes**: Supports standard ONT native barcoding kits.

## Pitfalls

- **Barcode Position**: Barcodes must be at read ends. Internal barcodes not supported.

- **Error Tolerance**: High error rates in Nanopore reads may cause misassignment. Adjust matching parameters.

- **Kit Compatibility**: Ensure barcode definitions match the sequencing kit used.

## Examples

### Basic demultiplexing
**Args:** `barbell -i reads.fastq.gz -b barcodes.tsv -o demultiplexed/`
**Explanation:** Demultiplexes Nanopore reads using barcode definitions from TSV file.

### Specify barcode kit
**Args:** `barbell -i reads.fastq.gz -k SQK-NBD114-96 -o demultiplexed/`
**Explanation:** Uses built-in barcode definitions for ONT NBD114-96 kit.

### Adjust error tolerance
**Args:** `barbell -i reads.fastq.gz -b barcodes.tsv -e 2 -o demultiplexed/`
**Explanation:** Allows up to 2 mismatches in barcode matching for higher sensitivity.

### Output unassigned reads
**Args:** `barbell -i reads.fastq.gz -b barcodes.tsv --unassigned -o demultiplexed/`
**Explanation:** Saves unassigned reads to separate file for inspection.
