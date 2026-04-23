---
name: virasign
category: alignment
description: Virasign is a viral taxonomic classification tool designed for nanopore sequencing data.
tags: [virasign, alignment, fastq, bam]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/virasign/blob/main/README.md"
---

## Concepts

- **Tool Overview**: virasign (v0.0.5) - Virasign (Viral Read ASSIGNment) is a viral taxonomic classification and reference selection tool for nanopore data. It maps long-read sequencing data (via minimap2) against viral databases (RVDB, RefSeq, or custom accessions) and performs taxonomic classification to identify viral species. Virasign generates comprehensive interactive HTML reports with filterable tables, charts and heatmaps. For each identified virus, Virasign also provides the closest reference sequence, mapped reads in FASTQ format, and BAM files which can be used to easily generate a consensus genome and visualize data (e.g., IGV). Virasign includes options to blind yourself from certain incidental findings (such as HIV, Hepatitis viruses, HTLV, EBV, CMV, HPV) when wanted, ensuring these findings do not appear in any output files, in line with consent guidelines and ethical research practices.
- **Core Function**: Virasign is a viral taxonomic classification tool designed for nanopore sequencing data.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda virasign`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
