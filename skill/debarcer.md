---
name: debarcer
category: programming
description: De-Barcoding and Error Correction tool for sequencing data with molecular barcodes.
tags: [debarcer, programming, barcoding, error-correction, sequencing]
author: oxo-call-community
source_url: "https://github.com/oicr-gsi/debarcer"
---

## Concepts

- **Tool Overview**: debarcer (v2.1.4+) is a Python package for de-barcoding and error correction of sequencing data containing molecular barcodes. It handles combinatorial barcodes, dual-indexed libraries, and provides robust error correction.
- **Core Function**: Identifies and corrects errors in molecular barcodes, demultiplexes samples, and generates clean barcode sequences for downstream analysis.
- **Input/Output**: Input: FASTQ files with barcodes, barcode whitelist. Output: Demultiplexed FASTQ files, corrected barcodes, summary statistics.
- **Algorithm**: Uses Levenshtein distance for error correction, supports hamming distance matching, and handles combinatorial barcode designs.
- **Key Features**: Error correction, combinatorial barcode support, dual-index handling, batch processing, comprehensive reporting.
- **Installation**: `conda install -c bioconda debarcer`

## Pitfalls

- **Barcode Design**: Complex barcode designs may require custom configuration.
- **Error Rate**: High error rates may exceed correction capabilities.
- **Whitelist Quality**: Results depend on comprehensive barcode whitelist.
- **Read Orientation**: Requires correct read orientation for paired-end data.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Basic debarcoding
**Args:** `debarcer -i reads.fastq -b barcodes.txt -o output/`
**Explanation:** Debarcode sequencing reads using barcode whitelist.

### Error correction with threshold
**Args:** `debarcer -i reads.fastq -b barcodes.txt --max-distance 2 -o output/`
**Explanation:** Allow up to 2 mismatches for barcode error correction.

### Paired-end debarcoding
**Args:** `debarcer -i R1.fastq -i2 R2.fastq -b barcodes.txt -o output/`
**Explanation:** Debarcode paired-end sequencing data.