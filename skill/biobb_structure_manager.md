---
name: biobb_structure_manager
category: utility
description: Library to efficiently load and process biomolecular 3D structures
tags: [bioexcel, structure-management, pdb, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/BioBB_structure_manager"
---

## Concepts
- **Tool Overview**: biobb_structure_manager is a Python library for efficiently loading and processing biomolecular 3D structures, wrapping Bio.PDB with additional features.
- **Structure Handling**: Loading, parsing, and manipulating PDB/mmCIF structures with enhanced functionality.
- **Applications**: Structure preprocessing, format conversion, chain/model selection.

## Pitfalls
- **Indirect Use**: Primarily used as a library by other biobb packages.

## Examples
### Load and process structure
**Args:** `biobb_structure_manager.load --input structure.pdb --output processed.pdb`
**Explanation:** Loads and processes a PDB structure file.
