---
name: bax2bam
category: formatting
description: bax2bam converts the legacy PacBio basecall format (bax.h5) into the BAM basecall format
tags: [bax2bam, formatting, BAM, HDF5]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/bax2bam"
---

## Concepts

- **Tool Overview**: bax2bam (v0.0.11) - bax2bam converts the legacy PacBio basecall format (bax.h5) into the BAM basecall format
- **Core Function**: bax2bam converts the legacy PacBio basecall format (bax.h5) into the BAM basecall format
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bax2bam`

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
