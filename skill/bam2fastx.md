---
name: bam2fastx
category: formatting
description: Converting and demultiplexing of PacBio BAM files into gzipped fasta and fastq files
tags: [bam2fastx, formatting, FASTA, FASTQ, BAM]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/bam2fastx"
---

## Concepts

- **Tool Overview**: bam2fastx (v3.0.0) - Converting and demultiplexing of PacBio BAM files into gzipped fasta and fastq files
- **Core Function**: Converting and demultiplexing of PacBio BAM files into gzipped fasta and fastq files
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda bam2fastx`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.gff -o output.gtf`
**Explanation:** Convert between file formats
