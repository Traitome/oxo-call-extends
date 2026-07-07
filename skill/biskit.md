---
name: biskit
category: structural-bioinformatics
description: Python platform for structural bioinformatics research
tags: [structural-bioinformatics, python, molecular-modeling, PDB]
author: oxo-call-community
source_url: "https://biskit.pasteur.fr"
---

## Concepts

- **Tool Overview**: Biskit is a modular, object-oriented Python library for structural bioinformatics research, developed at Institut Pasteur.
- **Structure Analysis**: Tools for analyzing protein and nucleic acid structures from PDB files.
- **Molecular Modeling**: Support for molecular modeling, docking, and simulation analysis.
- **Data Integration**: Integrates various structural biology data sources and formats.
- **Applications**: Protein structure analysis, ligand binding, structural comparison, molecular dynamics analysis.

## Pitfalls

- **Python 2 Legacy**: Some versions may have Python 2 dependencies; check version compatibility.
- **External Dependencies**: Requires external programs for some advanced functions (e.g., NAMD, AMBER).
- **Documentation**: May require consulting source code for advanced usage.

## Examples

### Parse PDB structure
**Args:** `from biskit import PDB; p = PDB('protein.pdb'); print(p.sequence())`
**Explanation:** Loads and parses a PDB structure file.

### Calculate RMSD
**Args:** `from biskit.metrics import RMSD; rmsd = RMSD(struct1, struct2).run()`
**Explanation:** Calculates RMSD between two structures.

### Analyze binding sites
**Args:** `from biskit import BindingSite; sites = BindingSite.find(pdb, ligand='ATP')`
**Explanation:** Identifies binding sites for a specific ligand.