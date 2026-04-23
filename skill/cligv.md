---
name: cligv
category: alignment
description: command line Interactive Genome Viewer
tags: [cligv, alignment, BAM, VCF]
author: oxo-call-community
source_url: "https://github.com/jonasfreudig/cligv"
---

## Concepts

- **Tool Overview**: cligv (v0.1.0) - command line Interactive Genome Viewer
- **Core Function**: clIGV (command line Interactive Genome Viewer) is a fast, interactive genome browser for the terminal. It allows visualization of genomic sequences, variants from VCF files, and alignments from BAM fi...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda cligv`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
