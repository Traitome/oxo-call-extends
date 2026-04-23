---
name: je-suite
category: qc
description: Je is a suite to handle barcoded fastq files with (or without) Unique Molecule Identifiers (UMIs) and filter read duplicates using these UMIs
tags: [je-suite, qc, FASTQ]
author: oxo-call-community
source_url: "https://gbcs.embl.de/Je"
---

## Concepts

- **Tool Overview**: je-suite (v2.0.RC) - Je is a suite to handle barcoded fastq files with (or without) Unique Molecule Identifiers (UMIs) and filter read duplicates using these UMIs
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda je-suite`

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
