---
name: bctools
category: qc
description: BCtools - Tools for handling barcodes in NGS data
tags: [barcodes, demultiplexing, ngs, barcode-processing]
author: oxo-call-community
source_url: "https://github.com/dmaticzka/bctools"
---

## Concepts

- **Tool Overview**: BCtools provides utilities for handling barcodes in NGS data, including barcode extraction and correction.

- **Barcode Extraction**: Extracts barcode sequences from reads for demultiplexing.

- **Error Correction**: Corrects barcode sequencing errors using whitelist or Hamming distance.

- **Demultiplexing Support**: Supports downstream demultiplexing workflows.

## Pitfalls

- **Barcode Position**: Requires knowledge of barcode position in reads.

- **Whitelist Quality**: Error correction quality depends on whitelist completeness.

- **Hamming Distance**: Appropriate Hamming distance threshold depends on barcode design.

## Examples

### Extract barcodes
**Args:** `bctools extract --input reads.fastq --position start --output barcodes.txt`
**Explanation:** Extracts barcode sequences from start of reads.

### Correct barcodes
**Args:** `bctools correct --barcodes barcodes.txt --whitelist whitelist.txt --output corrected.txt`
**Explanation:** Corrects barcode errors using whitelist reference.
