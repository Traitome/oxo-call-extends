---
name: biobb_flexserv
category: utility
description: BioBB module for biomolecular flexibility studies on protein 3D structures
tags: [bioexcel, flexibility, protein-structure, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_flexserv"
---

## Concepts
- **Tool Overview**: biobb_flexserv wraps FlexServ tools for biomolecular flexibility studies on protein 3D structures using coarse-grained approaches.
- **Flexibility Methods**: Normal mode analysis, discrete molecular dynamics, and elastic network models.
- **Applications**: Protein flexibility prediction, conformational sampling, functional motion analysis.

## Pitfalls
- **Resolution**: Coarse-grained methods provide approximate flexibility predictions.

## Examples
### Predict protein flexibility
**Args:** `biobb_flexserv.flexserv --input structure.pdb --output flexibility_analysis/`
**Explanation:** Predicts protein flexibility using coarse-grained methods.
