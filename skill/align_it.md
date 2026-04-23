---
name: align_it
category: alignment
description: Align-it is a tool to align molecules according to their pharmacophores. A pharmacophore is an abstract concept based on the specific interactions observed in drug-receptor interactions: hydrogen bonding, charge transfer, electrostatic and hydrophobic interactions.
tags: [align_it, alignment]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/align-it/1.0.4/align-it.html"
---

## Concepts

- **Tool Overview**: align_it (v1.0.4) - Align-it is a tool to align molecules according to their pharmacophores. A pharmacophore is an abstract concept based on the specific interactions observed in drug-receptor interactions: hydrogen bonding, charge transfer, electrostatic and hydrophobic interactions.
- **Core Function**: Align-it is a tool to align molecules according to their pharmacophores. A pharmacophore is an abstract concept based on the specific interactions observed in drug-receptor interactions: hydrogen bonding, charge transfer, electrostatic and hydrophobic interactions.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda align_it`

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
