---
name: hifiadapterfilt
category: qc
description: Convert .bam to .fastq and remove reads with remnant PacBio HiFi adapter sequences
tags: [hifiadapterfilt, qc, FASTQ, BAM]
author: oxo-call-community
source_url: "https://bio.tools/hifiadapterfilt"
---

## Concepts

- **Tool Overview**: hifiadapterfilt (v3.0.0) - Convert .bam to .fastq and remove reads with remnant PacBio HiFi adapter sequences
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hifiadapterfilt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
