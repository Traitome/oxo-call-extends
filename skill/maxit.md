---
name: maxit
category: alignment
description: MAXIT assists in processing and curation of macromolecular structure data.
tags: [maxit, structure-analysis, PDB-processing]
author: oxo-call-community
source_url: "https://sw-tools.rcsb.org/apps/MAXIT"
---

## Concepts

- **Tool Overview**: MAXIT processes and curates macromolecular structure data.
- **Core Function**: Handles PDB/mmCIF format conversion and validation.
- **Format Translation**: Converts between PDB and mmCIF formats.
- **Consistency Checks**: Validates coordinates, sequence, and crystal data.
- **Residue Alignment**: Aligns residue numbering between coordinates and sequence.
- **Installation**: `conda install -c bioconda maxit`

## Pitfalls

- **Format Compatibility**: May not handle all PDB/mmCIF variants.
- **Memory Requirements**: Large structures require significant memory.
- **Validation Strictness**: Strict validation may reject valid structures.
- **Version Differences**: Options may vary between versions.
- **Ligand Handling**: Non-standard ligands may cause issues.
- **Chain ID Assignment**: Requires careful chain ID handling.

## Examples

### Convert PDB to mmCIF
**Args:** `maxit -i input.pdb -o output.cif`
**Explanation:** Converts PDB file to mmCIF format.

### Validate structure
**Args:** `maxit -i input.pdb -v`
**Explanation:** Validates structure file for consistency.

### Reorder atoms
**Args:** `maxit -i input.pdb -r -o reordered.pdb`
**Explanation:** Reorders atoms according to Chemical Component Dictionary.

### Transform coordinates
**Args:** `maxit -i input.pdb -t transformation.txt -o transformed.pdb`
**Explanation:** Applies coordinate transformation.

### Merge structures
**Args:** `maxit -i struct1.pdb struct2.pdb -m -o merged.pdb`
**Explanation:** Merges multiple structure files.

### Help documentation
**Args:** `maxit --help`
**Explanation:** Displays available commands and options.
