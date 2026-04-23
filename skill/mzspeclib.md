---
name: mzspeclib
category: formatting
description: HUPO-PSI Spectral library format
tags: [mzspeclib, formatting, spectral-library, hupo-psi, proteomics]
author: oxo-call-community
source_url: "https://github.com/HUPO-PSI/mzSpecLib"
---

## Concepts

- **Tool Overview**: mzSpecLib v1.0.7 - HUPO-PSI spectral library format library.
- **Core Function**: Provides tools for reading and writing spectral libraries in the HUPO-PSI standard format.
- **Input/Output**: Takes/writes spectral library files in mzSpecLib format.
- **Installation**: `conda install -c bioconda mzspeclib`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Format Compliance**: Ensure adherence to HUPO-PSI mzSpecLib specification.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i library.mzsplib -o output.mzsplib`
**Explanation:** Processes spectral library files.
