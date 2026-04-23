---
name: circleseeker
category: assembly
description: Comprehensive eccDNA detection from PacBio HiFi sequencing data
tags: [circleseeker, assembly]
author: oxo-call-community
source_url: "https://github.com/leoxqy/CircleSeeker#readme"
---

## Concepts

- **Tool Overview**: circleseeker (v1.1.2) - Comprehensive eccDNA detection from PacBio HiFi sequencing data
- **Core Function**: CircleSeeker is a specialized bioinformatics pipeline designed for the identification, classification, and characterization of extrachromosomal circular DNA (eccDNA) from PacBio HiFi long-read sequenc...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda circleseeker`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
