---
name: autodock
category: utility
description: AutoDock - Suite of automated docking tools for molecular docking simulations
tags: [molecular-docking, drug-discovery, protein-ligand, virtual-screening]
author: oxo-call-community
source_url: "http://autodock.scripps.edu/"
---

## Concepts

- **Tool Overview**: AutoDock is a suite of automated docking tools for predicting how small molecules bind to receptor proteins. It includes AutoDock for docking calculations and AutoGrid for pre-calculating grid maps.

- **Grid-Based Docking**: Uses pre-calculated grid maps (from AutoGrid) to evaluate ligand-receptor interactions efficiently.

- **Lamarckian Genetic Algorithm**: Employs LGA for conformational search, combining genetic algorithms with local search for efficient exploration.

- **Flexible Ligands**: Supports full ligand flexibility with rotatable bonds defined in PDBQT format.

- **Scoring Function**: Uses force field-based scoring function with van der Waals, hydrogen bonding, electrostatic, and desolvation terms.

## Pitfalls

- **Grid Map Requirement**: Must run AutoGrid before AutoDock to generate grid maps. Missing maps cause docking failure.

- **PDBQT Preparation**: Both receptor and ligand must be properly prepared in PDBQT format with correct atom types and charges.

- **GPF/DPF Files**: Grid Parameter File (GPF) and Docking Parameter File (DPF) must be correctly configured.

- **Computation Time**: AutoDock is significantly slower than AutoDock Vina. Consider Vina for large-scale screening.

## Examples

### Generate grid maps with AutoGrid
**Args:** `autogrid4 -p receptor.gpf -l receptor.glg`
**Explanation:** Pre-calculates grid maps from Grid Parameter File, outputs grid log file.

### Run docking with AutoDock
**Args:** `autodock4 -p docking.dpf -l docking.dlg`
**Explanation:** Performs molecular docking using Docking Parameter File, outputs docking log file.

### Prepare receptor PDBQT
**Args:** `prepare_receptor4.py -r receptor.pdb -o receptor.pdbqt`
**Explanation:** Converts receptor PDB file to PDBQT format with added hydrogens and charges.

### Prepare ligand PDBQT
**Args:** `prepare_ligand4.py -l ligand.pdb -o ligand.pdbqt`
**Explanation:** Converts ligand PDB file to PDBQT format with rotatable bonds identified.

### Generate GPF file
**Args:** `prepare_gpf4.py -r receptor.pdbqt -l ligand.pdbqt -o receptor.gpf`
**Explanation:** Generates Grid Parameter File with default grid box centered on ligand.

### Generate DPF file
**Args:** `prepare_dpf4.py -r receptor.pdbqt -l ligand.pdbqt -o docking.dpf`
**Explanation:** Generates Docking Parameter File with default LGA search parameters.
