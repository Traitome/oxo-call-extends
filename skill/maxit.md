---
name: maxit
category: alignment
description: MAXIT assists in the processing and curation of macromolecular structure data.
tags: [maxit, alignment, alignment]
author: oxo-call-community
source_url: "https://sw-tools.rcsb.org/apps/MAXIT"
---

## Concepts

- **Tool Overview**: maxit v11.400 - MAXIT assists in the processing and curation of macromolecular structure data. MAXIT can:   - Read and write PDB and mmCIF format files, and translate between file formats.   - Perform consistency checks on coordinates, sequence, and crystal data.   - Automatically construct, transform, and merge information between formats   - Align residue numbering in the coordinates with the sequence   - Reorder and rename atoms in standard and nonstandard residues and ligands according to the Chemical Component Dictionary   - Assign ligands the same chain IDs as the adjacent polymers   - Detect missing or additional atoms.
- **Core Function**: MAXIT assists in the processing and curation of macromolecular structure data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda maxit`

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
