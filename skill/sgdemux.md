---
name: sgdemux
category: utility
description: sgdemux - Demultiplexing for Singular Genomics sequencing instruments
tags: ["sgdemux", "utility", "demultiplexing", "sequencing"]
author: oxo-call-community
source_url: "https://github.com/Singular-Genomics/singular-demux"
---

## Concepts

- **Tool Overview**: sgdemux (v1.2.0) demultiplexes sequencing data from Singular Genomics instruments.
- **Core Function**: Separates pooled sequencing data into individual samples.
- **Algorithm**: Uses barcode matching for sample identification.
- **Input/Output**: Accepts raw sequencing data and produces demultiplexed FASTQ files.
- **Demultiplexing**: Focuses on sample separation using barcodes.
- **Applications**: Sequencing data processing, NGS analysis, and sample management.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Format**: Requires correct sequencing data format.
- **Performance**: May be slow for extremely large files.
- **Barcode Quality**: Results depend on barcode quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Demultiplex reads
**Args:** `sgdemux -i input_data/ -o output/ -b barcodes.csv`
**Explanation:** `-i` input directory; `-o` output directory; `-b` barcode file.

### With mismatches
**Args:** `sgdemux -i input_data/ -o output/ -b barcodes.csv -m 2`
**Explanation:** `-m 2` allows 2 barcode mismatches.

### Verbose logging
**Args:** `sgdemux -v -i input_data/ -o output/ -b barcodes.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sgdemux --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sgdemux --version`
**Explanation:** Shows current version.

### Sample sheet
**Args:** `sgdemux -i input_data/ -o output/ -s samplesheet.csv`
**Explanation:** `-s` sample sheet file.