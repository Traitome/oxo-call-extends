---
name: mantis-msi2
category: alignment
description: MANTIS2 is a program developed for detecting microsatellite instability from paired-end BAM files.
tags: [mantis-msi2, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/nh13/MANTIS2"
---

## Concepts

- **Tool Overview**: mantis-msi2 v2.0.0 - MANTIS2 (Microsatellite Analysis for Normal-Tumor InStability) is a program developed for detecting microsatellite instability from paired-end BAM files. To perform analysis, the program needs a tumor BAM and a matched normal BAM file (produced using the same pipeline) to determine the instability score between the two samples within the pair. Longer reads (ideally, 100 bp or longer) are recommended, as shorter reads are unlikely to entirely cover the microsatellite loci, and will be discarded after failing the quality control filters.  Originally developed and maintained here: https://github.com/OSU-SRLab/MANTIS..
- **Core Function**: MANTIS2 is a program developed for detecting microsatellite instability from paired-end BAM files.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mantis-msi2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
