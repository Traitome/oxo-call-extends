---
name: bxtools
category: expression
description: Tools for analyzing 10X Genomics single-cell data
tags: [bxtools, 10x, single-cell, barcode, cellranger]
author: oxo-call-community
source_url: "https://github.com/walaj/bxtools"
---

## Concepts

- **Tool Overview**: bxtools provides utilities for analyzing 10X Genomics single-cell data.
- **Core Function**: Extracts and manipulates barcode and UMI information from 10X data.
- **Input**: BAM files from Cell Ranger or similar 10X pipelines.
- **Output**: Barcode statistics, UMI counts, and filtered BAM files.
- **Application**: Quality control and filtering of 10X single-cell data.
- **Installation**: Install via bioconda: `conda install -c bioconda bxtools`

## Pitfalls

- **10X Specific**: Designed for 10X Genomics data format.
- **BAM Tags**: Requires proper BX (barcode) and MI (UMI) tags in BAM.
- **Memory Usage**: Large BAM files require significant memory.

## Examples

### Extract barcode statistics
**Args:** `bxtools extract -b aligned.bam -o barcode_stats.tsv`
**Explanation:** Extracts barcode and UMI statistics from 10X BAM.

### Filter by barcode
**Args:** `bxtools filter -b aligned.bam -w whitelist.txt -o filtered.bam`
**Explanation:** Filters BAM to keep only whitelisted barcodes.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
