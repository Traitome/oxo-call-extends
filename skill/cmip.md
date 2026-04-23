---
name: cmip
category: annotation
description: CMIP Classical Molecular Interaction Potentials
tags: [cmip, annotation]
author: oxo-call-community
source_url: "http://mmb.irbbarcelona.org/gitlab/gelpi/CMIP"
---

## Concepts

- **Tool Overview**: cmip (v2.7.0) - CMIP Classical Molecular Interaction Potentials
- **Core Function**: The latest version of the classical molecular interaction potential (CMIP) has the ability to predict the position of crystallographic waters in several proteins with great accuracy.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cmip`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
