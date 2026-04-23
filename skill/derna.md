---
name: derna
category: annotation
description: RNA sequence design for a target protein sequence.
tags: [derna, annotation, rna-design, protein, codon-optimization]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/derna"
---

## Concepts

- **Tool Overview**: derNA v1.0.4 - Tool for designing RNA sequences that encode a target protein sequence.
- **Core Function**: Designs optimal RNA coding sequences for given protein targets, considering codon usage and structural constraints.
- **Input/Output**: Expects protein sequence input; outputs designed RNA sequences.
- **Installation**: `conda install -c bioconda derna`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires valid protein sequence.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `derna --protein target.fa --output rna_design.fa`
**Explanation:** Designs RNA sequence encoding the target protein.
