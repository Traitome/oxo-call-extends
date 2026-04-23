---
name: biopet-vcffilter
category: qc
description: This tool enables a user to filter VCF files.
tags: [biopet-vcffilter, qc, SAM, VCF]
author: oxo-call-community
source_url: "https://github.com/biopet/vcffilter"
---

## Concepts

- **Tool Overview**: biopet-vcffilter (v0.2) - This tool enables a user to filter VCF files.
- **Core Function**: This tool enables a user to filter VCF files. For example on sample depth and/or total depth. It can also be used to filter out the reference calls and/or minimum number of sample passes. There is a w...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda biopet-vcffilter`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
