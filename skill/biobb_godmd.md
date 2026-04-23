---
name: biobb_godmd
category: utility
description: BioBB category for GOdMD protein conformational transitions
tags: [bioexcel, conformational-transition, protein-dynamics, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_godmd"
---

## Concepts
- **Tool Overview**: biobb_godmd wraps GOdMD (Geometrical Optimization driven Molecular Dynamics) for predicting protein conformational transitions between two structural states.
- **Transition Pathways**: Computes intermediate conformations along transition pathways between two protein states.
- **Applications**: Allosteric mechanism studies, enzyme catalysis, protein function prediction.

## Pitfalls
- **Two-State Requirement**: Requires both initial and target protein conformations.

## Examples
### Compute transition pathway
**Args:** `biobb_godmd.godmd --input initial.pdb --target target.pdb --output pathway/`
**Explanation:** Computes conformational transition pathway between two protein states.
