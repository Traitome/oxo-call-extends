---
name: smina
category: drug-discovery
description: smina is a fork of AutoDock Vina customized for scoring function development and high-performance energy minimization
tags: [smina, drug-discovery, molecular-docking, vina, protein-ligand]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/smina/"
---

## Concepts

- **Tool Overview**: smina (v2017.11.9) - A molecular docking tool based on AutoDock Vina
- **Core Function**: Performs protein-ligand docking and energy minimization
- **Input/Output**: Accepts PDBQT files; outputs docked poses with scores
- **Algorithm**: Uses gradient-based optimization for molecular docking
- **Installation**: `conda install -c bioconda smina`
- **Key Features**: Customizable scoring functions, fast performance, supports GPU acceleration

## Pitfalls

- **Input Format**: Requires PDBQT format for proteins and ligands
- **Protein Preparation**: Protein must be properly prepared (protonation, water removal)
- **Ligand Preparation**: Ligand must have correct protonation state
- **Grid Box Size**: Appropriate grid box definition affects results
- **Computation Time**: Complex systems can be computationally intensive
- **Score Interpretation**: Docking scores require careful interpretation

## Examples

### Display help
**Args:** `smina --help`
**Explanation:** Shows available options and usage information.

### Basic docking
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o docked.pdbqt`
**Explanation:** Perform molecular docking of ligand to protein.

### With custom grid
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o docked.pdbqt --center_x 10 --center_y 20 --center_z 30 --size_x 20 --size_y 20 --size_z 20`
**Explanation:** Define custom grid box for docking.

### Energy minimization
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o minimized.pdbqt --minimize`
**Explanation:** Perform energy minimization only.

### Multiple ligands
**Args:** `smina -r protein.pdbqt -l ligands.sdf -o docked.sdf`
**Explanation:** Dock multiple ligands from SDF file.

### Custom scoring function
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o docked.pdbqt --scoring vinardo`
**Explanation:** Use Vinardo scoring function.

### GPU acceleration
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o docked.pdbqt --gpu`
**Explanation:** Use GPU for accelerated docking.

### Generate output in different format
**Args:** `smina -r protein.pdbqt -l ligand.pdbqt -o docked.sdf --out_format sdf`
**Explanation:** Output results in SDF format.