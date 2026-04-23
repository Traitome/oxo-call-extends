---
name: mylotools
category: utility
description: Utilities for manipulation and quality control of the myloasm long-read assembler
tags: [mylotools, utility, assembly, qc, long-reads]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/mylotools"
---

## Concepts

- **Tool Overview**: mylotools v2.0.0 - utilities for myloasm assembler manipulation and QC.
- **Core Function**: Provides quality control and manipulation tools for myloasm assembly outputs.
- **Input/Output**: Takes myloasm assembly outputs; provides QC reports and processed assemblies.
- **Installation**: `conda install -c bioconda mylotools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Dependencies**: Designed to work with myloasm outputs.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o qc_report.tsv`
**Explanation:** Generates QC report for myloasm assembly.
