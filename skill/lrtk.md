---
name: lrtk
category: utility
description: Unified and versatile ToolKit for analyzing Linked-Read sequencing data.
tags: [lrtk, utility, linked-reads, sequencing]
author: oxo-call-community
source_url: "https://github.com/ericcombiolab/LRTK"
---

## Concepts

- **Tool Overview**: lrtk v2.0 is a unified toolkit for comprehensive analysis of Linked-Read sequencing data from platforms like 10X Genomics.
- **Core Function**: Provides a suite of tools for barcode processing, read mapping, variant calling, and haplotype phasing from linked-read data.
- **Barcode Processing**: Handles barcode extraction, error correction, and read grouping for linked-read analysis.
- **Input/Output**: Input: FASTQ/BAM files with barcoded reads; Output: Processed reads, mapped alignments, variant calls.
- **Installation**: `conda install -c bioconda lrtk`
- **Key Features**: Integrated pipeline for linked-read analysis, supports multiple sequencing platforms, includes visualization tools.

## Pitfalls

- **Barcode Quality**: Poor-quality barcodes can lead to incorrect read grouping and downstream analysis errors.
- **Memory Requirements**: Processing large linked-read datasets may require significant memory resources.
- **Reference Genome**: Accurate mapping requires a high-quality reference genome.
- **Version Compatibility**: Command options may change between versions.
- **Computation Time**: Some analyses can be computationally intensive for large datasets.
- **Input Format**: Requires specific FASTQ format with barcode information in read headers.

## Examples

### Process raw reads
**Args:** `lrtk process -i reads.fastq -o processed/`
**Explanation:** Processes raw linked-reads and extracts barcode information.

### Map reads
**Args:** `lrtk map -i processed.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Maps processed reads to reference genome.

### Call variants
**Args:** `lrtk variant -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from aligned linked-reads.

### Phase variants
**Args:** `lrtk phase -i variants.vcf -b aligned.bam -o phased.vcf`
**Explanation:** Phases variants using linked-read barcode information.

### Generate statistics
**Args:** `lrtk stats -i aligned.bam -o stats.txt`
**Explanation:** Generates quality metrics and statistics for linked-read data.

### Help documentation
**Args:** `lrtk --help`
**Explanation:** Displays all available commands and options.