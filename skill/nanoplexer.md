---
name: nanoplexer
category: utility
description: NanoPlexer - Demultiplexing tool for Nanopore barcode sequence data
tags: [nanoplexer, utility, nanopore, demultiplexing, barcoding, multiplexing]
author: oxo-call-community
source_url: "https://github.com/hanyue36/nanoplexer"
---

## Concepts

- **Tool Overview**: NanoPlexer v0.1.2 is a tool for demultiplexing Oxford Nanopore barcode sequence data. It separates reads from multiplexed sequencing runs based on barcode sequences.
- **Core Function**: Identifies barcode sequences in Nanopore reads and separates them into individual samples. Supports both inline and adapter barcodes.
- **Algorithm**: Uses exact matching or fuzzy matching to identify barcodes. Handles barcode orientation and quality trimming.
- **Input Format**: Accepts barcoded FASTQ files and a barcode reference file (TSV format with barcode sequences and sample names).
- **Output**: Produces separate FASTQ files for each barcode/sample combination.
- **Use Case**: Demultiplexing multiplexed Nanopore sequencing runs, separating pooled samples, and preparing individual sample datasets for downstream analysis.

## Pitfalls

- **Barcode Quality**: Poor barcode quality reduces demultiplexing accuracy. Ensure high-quality barcodes during library preparation.
- **Barcode Misassignment**: Ambiguous barcodes may cause misassignment. Use unique barcodes for each sample.
- **Barcode Orientation**: Some barcodes may be read in reverse complement. Ensure proper orientation handling.
- **Adapter Sequences**: Adapter sequences should be trimmed before demultiplexing if not handled automatically.
- **Sample Balance**: Uneven sample representation may affect downstream analysis. Monitor sample distribution.
- **Index Hopping**: Cross-contamination between samples may occur. Consider unique dual barcodes for sensitive applications.

## Examples

### Basic demultiplexing
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir`
**Explanation:** Demultiplexes Nanopore reads by barcode sequences.

### Allow mismatches
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir -m 2`
**Explanation:** Allows up to 2 mismatches in barcode sequences.

### Trim adapters
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir --trim_adapters`
**Explanation:** Trims adapter sequences after demultiplexing.

### Gzip output
**Args:** `-i reads.fastq.gz -b barcodes.tsv -o output_dir --gzip`
**Explanation:** Compresses output FASTQ files with gzip.

### Display help
**Args:** `nanoplexer --help`
**Explanation:** Shows all available options for demultiplexing.
