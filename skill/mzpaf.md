---
name: mzpaf
category: formatting
description: HUPO-PSI Peptide peak annotation format
tags: [mzpaf, formatting, peptide, peak-annotation, hupo-psi]
author: oxo-call-community
source_url: "https://github.com/HUPO-PSI/mzPAF"
---

## Concepts

- **Tool Overview**: mzPAF v0.2.0b0 - HUPO-PSI peptide peak annotation format library.
- **Core Function**: Provides tools for reading and writing peptide peak annotation data in the HUPO-PSI standard format.
- **Input/Output**: Takes/writes peak annotation files in mzPAF format.
- **Installation**: `conda install -c bioconda mzpaf`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Format Compliance**: Ensure adherence to HUPO-PSI mzPAF specification.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.mzpaf -o output.mzpaf`
**Explanation:** Processes peptide peak annotation files.
