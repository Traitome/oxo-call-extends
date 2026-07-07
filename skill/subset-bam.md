---
name: subset-bam
category: utility
description: A tool to subset a 10x Genomics BAM file based on a tag, most commonly the cell barcode tag.
tags: [subset-bam, 10x-genomics, single-cell, bam-processing]
author: oxo-call-community
source_url: "https://github.com/10XGenomics/subset-bam/blob/v1.1.0/README.md"
---

## Concepts

- **Tool Overview**: subset-bam (v1.1.0) is a tool for subsetting 10x Genomics BAM files based on tags.
- **Core Function**: Filters BAM files based on cell barcodes or other tags.
- **Algorithm**: Reads BAM file and filters reads based on specified tags.
- **Input/Output**: Input: BAM file, tag list; Output: Subsetted BAM file.
- **Applications**: Single-cell RNA-seq analysis, data filtering, sample separation.
- **Installation**: `conda install -c bioconda subset-bam` or download from GitHub.

## Pitfalls

- **Input Format**: Requires 10x Genomics formatted BAM files.
- **Tag Availability**: Requires proper tag annotation in BAM file.
- **Memory Requirements**: Large BAM files require significant memory.
- **Computational Time**: Processing large BAM files can be slow.
- **Index Requirement**: Requires indexed BAM file for efficient processing.
- **Tag Format**: Requires correct tag format specification.

## Examples

### Display help
**Args:** `subset-bam --help`
**Explanation:** Shows available options and usage information.

### Basic subsetting
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt`
**Explanation:** Subset BAM by cell barcodes.

### With tag specification
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt -t CB`
**Explanation:** Use custom tag (CB) for cell barcodes.

### Verbose mode
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt --stats`
**Explanation:** Generate statistics about subsetting.

### Batch processing
**Args:** `subset-bam -i bams/ -o outputs/ -b barcodes.txt`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt -q 20`
**Explanation:** Filter reads by mapping quality.

### Include unmapped
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt --include-unmapped`
**Explanation:** Include unmapped reads in output.

### Generate report
**Args:** `subset-bam -i input.bam -o output.bam -b barcodes.txt --report`
**Explanation:** Generate comprehensive HTML report.
