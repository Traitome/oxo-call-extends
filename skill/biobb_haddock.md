---
name: biobb_haddock
category: utility
description: BioBB module for information-driven flexible protein-protein docking
tags: [bioexcel, haddock, protein-docking, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_haddock"
---

## Concepts
- **Tool Overview**: biobb_haddock wraps HADDOCK (High Ambiguity Driven protein-protein DOCKing) for information-driven flexible protein-protein docking.
- **Data-Driven Docking**: Incorporates experimental data (NMR, mutagenesis, etc.) to guide docking predictions.
- **Applications**: Protein-protein complex prediction, antibody-antigen docking, biomolecular assembly modeling.

## Pitfalls
- **HADDOCK License**: HADDOCK may require academic or commercial license.
- **Data Requirements**: Best results require experimental restraints or bioinformatic predictions.

## Examples
### Run protein-protein docking
**Args:** `biobb_haddock.docking --receptor proteinA.pdb --ligand proteinB.pdb --output complexes/`
**Explanation:** Performs protein-protein docking to predict complex structures.
