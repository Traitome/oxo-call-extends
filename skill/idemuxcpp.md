---
name: idemuxcpp
category: utility
description: A Lexogen tool for demultiplexing and index error correcting fastq files. Works with Lexogen i7, i5 and i1 barcodes with advanced error correction.
tags: [idemuxcpp, utility, FASTQ, demultiplexing, barcode]
author: oxo-call-community
source_url: "https://github.com/Lexogen-Tools/idemuxcpp"
---

## Concepts

- **Demultiplexing**: Separates pooled sequencing reads into individual samples based on index barcodes (i7, i5, i1).
- **Index Error Correction**: Advanced error correction algorithms to rescue reads with index sequencing errors.
- **Triple-index Support**: Handles Lexogen's triple-indexing strategy (i7, i5, i1) for high-throughput multiplexing.
- **UDI Compatibility**: Works with Unique Dual Indexes (UDIs) to minimize index hopping and misassignment.
- **Base Quality-aware**: Considers base quality scores when performing error correction for more accurate demultiplexing.

## Pitfalls

- **Barcode Design**: Requires compatible Lexogen barcode designs; non-standard barcodes may cause misassignment.
- **Index Configuration**: Incorrect index specification can lead to sample cross-contamination or lost reads.
- **Quality Thresholds**: Setting inappropriate quality thresholds may filter out valid reads or include erroneous ones.
- **Memory Management**: Large FASTQ files require sufficient memory for efficient processing.
- **Output File Management**: Generates multiple output files; proper directory structure planning is essential.

## Examples

### Basic demultiplexing
**Args:** `idemuxcpp -i input.fastq -o output_dir --barcodes barcodes.csv`
**Explanation:** Demultiplexes input FASTQ file using barcode information from CSV file.

### With error correction
**Args:** `idemuxcpp -i input.fastq -o output_dir --barcodes barcodes.csv --error_correction`
**Explanation:** Enables advanced index error correction to rescue reads with sequencing errors.

### Triple-index processing
**Args:** `idemuxcpp -i input.fastq -o output_dir --i7 i7_barcodes.txt --i5 i5_barcodes.txt --i1 i1_barcodes.txt`
**Explanation:** Processes triple-indexed data with separate barcode files for i7, i5, and i1 indices.

### Quality filtering
**Args:** `idemuxcpp -i input.fastq -o output_dir --barcodes barcodes.csv --min_quality 20`
**Explanation:** Filters reads with quality score below 20 before demultiplexing.

### Paired-end demultiplexing
**Args:** `idemuxcpp -i read1.fastq -i2 read2.fastq -o output_dir --barcodes barcodes.csv`
**Explanation:** Demultiplexes paired-end sequencing data with paired FASTQ files.