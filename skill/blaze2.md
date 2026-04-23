---
name: blaze2
category: expression
description: Barcode identification from Nanopore Long reads for AnalyZing single-cell gene Expression
tags: [blaze2, nanopore, single-cell, barcode, expression]
author: oxo-call-community
source_url: "https://github.com/shimlab/BLAZE"
---

## Concepts

- **Tool Overview**: BLAZE identifies cell barcodes from Nanopore long reads for single-cell analysis.
- **Core Function**: Extracts and corrects cell barcodes from single-cell Nanopore data.
- **Input**: Nanopore FASTQ files from single-cell experiments.
- **Output**: Corrected barcode sequences and cell assignments.
- **Application**: Single-cell RNA-seq analysis with Nanopore sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda blaze2`

## Pitfalls

- **Nanopore Specific**: Designed for Nanopore data; not for Illumina single-cell.
- **Barcode Chemistry**: Must match barcode chemistry used in experiment.
- **Error Rate**: Nanopore error rate affects barcode identification accuracy.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Identify barcodes from Nanopore reads
**Args:** `blaze2 -i reads.fq -o barcodes.tsv`
**Explanation:** Extracts and corrects cell barcodes from Nanopore single-cell reads.

### Specify barcode chemistry
**Args:** `blaze2 -i reads.fq -c 10x_v3 -o barcodes.tsv`
**Explanation:** Uses 10x v3 chemistry barcode whitelist for correction.

### Set minimum barcode count
**Args:** `blaze2 -i reads.fq -m 100 -o barcodes.tsv`
**Explanation:** Requires minimum 100 reads per barcode for cell calling.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
