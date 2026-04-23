---
name: ligand-validation
category: qc
description: Extract ligand and binding site information from PDB X-ray validation reports
tags: [ligand-validation, qc]
author: oxo-call-community
source_url: "https://git.scicore.unibas.ch/schwede/ligand-validation"
---

## Concepts

- **Tool Overview**: ligand-validation v0.0.1 - This project contains script for the validation of the quality of a PDB entry, ligand and binding site based on the PDB Validation pipeline..
- **Core Function**: Extract ligand and binding site information from PDB X-ray validation reports
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda ligand-validation`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
