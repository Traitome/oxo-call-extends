---
name: beem-bio
category: formatting
description: Conversion of PDBx/mmCIF files to best effort/minimal PDB files
tags: [pdb, mmcif, structure, format-conversion]
author: oxo-call-community
source_url: "https://github.com/kad-ecoli/BeEM"
---

## Concepts
- **Tool Overview**: BeEM (Best Effort Minimal) is a tool for converting PDBx/mmCIF format files to PDB format. It produces minimal PDB files with best-effort conversion of structural data.
- **mmCIF Format**: PDBx/mmCIF is the modern successor to PDB format, providing more extensible and standardized representation of macromolecular structures.
- **PDB Format**: Traditional Protein Data Bank format with fixed-width columns, limited to handling structures with up to 99999 atoms.
- **Conversion Challenges**: mmCIF can represent data that PDB cannot (e.g., large structures, alternative conformations, complex assemblies). BeEM performs best-effort conversion.

## Pitfalls
- **Data Loss**: Conversion from mmCIF to PDB may lose information (e.g., structures with >99999 atoms, complex metadata).
- **Format Limitations**: PDB format has inherent limitations that mmCIF overcomes. Some mmCIF features cannot be represented in PDB.
- **Validation**: Converted files should be validated for structural integrity.

## Examples
### Convert mmCIF to PDB
**Args:** `beem -i structure.cif -o structure.pdb`
**Explanation:** Converts an mmCIF file to minimal PDB format.

### Batch conversion
**Args:** `for f in *.cif; do beem -i "$f" -o "${f%.cif}.pdb"; done`
**Explanation:** Converts all mmCIF files in a directory to PDB format.
