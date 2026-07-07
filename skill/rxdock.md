---
name: rxdock
category: molecular_docking
description: RxDock - a fast, versatile open-source program for docking ligands to proteins and nucleic acids.
tags: ["rxdock", "molecular docking", "drug discovery", "protein-ligand", "bioinformatics"]
author: oxo-call-community
source_url: "https://www.rxdock.org"
---

## Concepts

- **Tool Overview**: RxDock (v2013.1.1) is a fast and versatile molecular docking program for predicting ligand-protein interactions. It is a fork of rDock with enhanced features and performance.
- **Core Function**: Performs molecular docking to predict the binding mode of small molecule ligands to protein or nucleic acid targets. Uses scoring functions to rank potential binding poses.
- **Algorithm**: Implements a hybrid search algorithm combining genetic algorithms and local optimization for efficient exploration of conformational space.
- **Input Format**: Protein structures in PDB format, ligand structures in SDF or SMILES format, optional receptor cavity definitions.
- **Output Format**: Docked poses in PDB/SDF format, scoring results with binding affinities, interaction energy profiles.
- **Use Case**: Structure-based drug design, virtual screening of compound libraries, studying protein-ligand interactions, lead optimization.

## Pitfalls

- **Receptor preparation**: Requires properly prepared protein structures (removed water, added hydrogens).
- **Cavity definition**: Accurate cavity identification is crucial for successful docking.
- **Scoring limitations**: Scoring functions may not perfectly predict binding affinities.
- **Conformational sampling**: May miss optimal binding poses in complex binding sites.
- **Computational time**: Docking large compound libraries can be time-consuming.
- **Force field limitations**: Simplified force fields may not capture all interactions accurately.

## Examples

### Basic docking
**Args:** `rxdock -r receptor.pdb -l ligand.sdf -o docked.sdf`
**Explanation:** `-r` receptor protein; `-l` ligand file; `-o` output with docked poses.

### Virtual screening
**Args:** `rxdock -r receptor.pdb -l library.sdf -o results.sdf --screen`
**Explanation:** `--screen` enables virtual screening mode.

### Specify cavity
**Args:** `rxdock -r receptor.pdb -l ligand.sdf -c cavity.def -o docked.sdf`
**Explanation:** `-c` cavity definition file.

### Number of poses
**Args:** `rxdock -r receptor.pdb -l ligand.sdf -o docked.sdf -n 10`
**Explanation:** `-n` number of poses to generate per ligand.

### Score only mode
**Args:** `rxdock -r receptor.pdb -l ligand.sdf -o scores.txt --score-only`
**Explanation:** `--score-only` calculates score without full docking.

### Flexible docking
**Args:** `rxdock -r receptor.pdb -l ligand.sdf -o docked.sdf --flexible`
**Explanation:** `--flexible` allows sidechain flexibility in binding site.

### Generate cavity
**Args:** `rxdock -r receptor.pdb --gen-cavity cavity.def`
**Explanation:** `--gen-cavity` generates cavity definition from receptor.
