---
name: msms
category: utility
description: Compute molecular surfaces for biomolecules using MSMS algorithm.
tags: [msms, utility, structural-biology]
author: oxo-call-community
source_url: "http://mgltools.scripps.edu/packages/MSMS/"
---

## Concepts

- **Tool Overview**: MSMS v2.6.1 computes molecular surface areas for biomolecules.
- **Core Function**: Calculates solvent-accessible and solvent-excluded surfaces.
- **Molecular Surface**: Generates various surface representations.
- **Biomolecular Modeling**: Supports protein and other biomolecule structures.
- **Surface Analysis**: Used for binding site and interaction analysis.
- **Input/Output**: Accepts PDB files; outputs surface files.

## Pitfalls

- **PDB Format**: Requires properly formatted PDB input.
- **Memory Requirements**: Memory usage depends on molecule size.
- **Parameter Tuning**: May require parameter adjustment for probe radius.
- **Data Quality**: Results depend on structure quality.
- **Computational Resources**: Large molecules may require significant resources.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Calculate molecular surface
**Args:** `msms -ifile molecule.pdb -ofile surface`
**Explanation:** Computes molecular surface from PDB file.

### With custom probe radius
**Args:** `msms -ifile molecule.pdb -probe_radius 1.5 -ofile surface`
**Explanation:** Uses 1.5 Angstrom probe radius.

### Generate surface vertices
**Args:** `msms -ifile molecule.pdb -afile vertices -ofile surface`
**Explanation:** Outputs surface vertex coordinates.

### Solvent accessible surface
**Args:** `msms -ifile molecule.pdb -surface ASA -ofile surface`
**Explanation:** Computes solvent accessible surface area.

### Batch processing
**Args:** `msms -i pdb/ -o surfaces/`
**Explanation:** Processes multiple PDB files.