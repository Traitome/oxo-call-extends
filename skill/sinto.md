---
name: sinto
category: single-cell
description: sinto - Tools for single-cell data processing
tags: ["sinto", "single-cell", "processing", "scatac"]
author: oxo-call-community
source_url: "https://timoast.github.io/sinto/"
---

## Concepts

- **Tool Overview**: sinto (v0.10.1) provides tools for single-cell data processing.
- **Core Function**: Processes and manipulates single-cell sequencing data.
- **Algorithm**: Handles various single-cell data formats and transformations.
- **Input/Output**: Accepts BAM/FASTQ files and produces processed data.
- **Single-cell Processing**: Specialized for scATAC-seq and scRNA-seq data.
- **Applications**: Single-cell data preprocessing, quality control, analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Dependency Issues**: Requires Python environment and specific packages.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Filter cells
**Args:** `sinto filterbarcodes -b alignments.bam -c barcodes.txt -o filtered.bam`
**Explanation:** `-c` barcode whitelist.

### Convert to fragments
**Args:** `sinto fragments -b alignments.bam -o fragments.tsv`
**Explanation:** Converts BAM to fragments format.

### Merge BAMs
**Args:** `sinto merge -b bam_list.txt -o merged.bam`
**Explanation:** Merges multiple BAM files.

### Help command
**Args:** `sinto --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sinto --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sinto -v filterbarcodes -b alignments.bam -c barcodes.txt -o filtered.bam`
**Explanation:** `-v` verbose output.

### Split by barcode
**Args:** `sinto split -b alignments.bam -c barcodes.txt -o split/`
**Explanation:** Splits BAM by cell barcodes.
