---
name: mmdb2
category: annotation
description: C++ toolkit for working with macromolecular coordinate files.
tags: [mmdb2, annotation, pdb]
author: oxo-call-community
source_url: "https://www.ccp4.ac.uk"
---

## Concepts

- **Tool Overview**: mmdb2 v2.0.22 is a C++ toolkit for macromolecular coordinate files.
- **Core Function**: Manipulates PDB and mmCIF files for structural biology.
- **Coordinate Handling**: Supports macromolecular coordinate operations.
- **Symmetry Operations**: Handles crystallographic symmetry.
- **Input/Output**: Accepts PDB/mmCIF files; outputs modified structures.
- **Molecular Geometry**: Performs geometry calculations.

## Pitfalls

- **C++ Specific**: Requires C++ development environment.
- **Memory Requirements**: Memory usage depends on structure size.
- **Parameter Tuning**: May require parameter adjustment.
- **Data Quality**: Results depend on input file quality.
- **Build Requirements**: May require compilation from source.
- **API Complexity**: Requires understanding of C++ API.

## Examples

### Read PDB file
**Args:** `mmdb2_read structure.pdb -o output.txt`
**Explanation:** Reads and analyzes PDB file.

### Convert to mmCIF
**Args:** `mmdb2_convert structure.pdb -f mmcif -o structure.cif`
**Explanation:** Converts PDB to mmCIF format.

### Apply symmetry
**Args:** `mmdb2_symmetry structure.pdb -s spacegroup -o symmetric.pdb`
**Explanation:** Applies crystallographic symmetry.

### Geometry calculation
**Args:** `mmdb2_geometry structure.pdb -o geometry.txt`
**Explanation:** Calculates molecular geometry.

### Batch processing
**Args:** `mmdb2_batch pdb/ -o results/`
**Explanation:** Processes multiple PDB files.