---
name: biopet-validatevcf
category: formatting
description: ValidateVcf validates a VCF file against a reference genomes.
tags: [biopet-validatevcf, formatting, VCF]
author: oxo-call-community
source_url: "https://github.com/biopet/validatevcf"
---

## Concepts

- **Tool Overview**: biopet-validatevcf (v0.1) - ValidateVcf validates a VCF file against a reference genomes.
- **Core Function**: ValidateVcf validates a VCF file against a reference genomes. It checks if the positions present in the VCF are also present on the reference genoome.  For documentation and manuals visit our github.i...
- **Input/Output**: VCF variant input/output
- **Installation**: `conda install -c bioconda biopet-validatevcf`

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
