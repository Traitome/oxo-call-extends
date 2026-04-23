---
name: autogrid
category: utility
description: AutoGrid - Pre-calculate grid maps for AutoDock molecular docking
tags: [molecular-docking, grid-maps, autodock, protein-ligand]
author: oxo-call-community
source_url: "http://autodock.scripps.edu/"
---

## Concepts

- **Tool Overview**: AutoGrid pre-calculates grid maps for AutoDock docking calculations. Each map represents the interaction energy of a probe atom with the receptor at grid points.

- **Grid Maps**: Generates separate maps for each atom type (C, O, N, H, etc.) plus electrostatic and desolvation maps.

- **Grid Box**: Defines 3D search space with center coordinates and dimensions (npts) in each direction.

- **Probe Atoms**: Each grid map uses a specific probe atom type to evaluate interaction energies at all grid points.

## Pitfalls

- **Grid Resolution**: Default spacing (0.375Å) may be too coarse for some applications. Adjust spacing parameter if needed.

- **Box Size**: Grid box must be large enough to contain binding site and ligand. Too small box misses correct poses.

- **Atom Types**: Must include all ligand atom types in GPF. Missing types cause AutoDock errors.

- **Memory Usage**: Large grid boxes generate large map files. Ensure sufficient disk space.

## Examples

### Basic grid map generation
**Args:** `autogrid4 -p receptor.gpf -l receptor.glg`
**Explanation:** Generates all grid maps specified in GPF file, outputs log file.

### Custom grid box
**Args:** `prepare_gpf4.py -r receptor.pdbqt -l ligand.pdbqt -p gridcenter=10.0,20.0,30.0 -p npts=60,60,60 -o receptor.gpf && autogrid4 -p receptor.gpf -l receptor.glg`
**Explanation:** Creates GPF with custom grid center and dimensions, then generates maps.

### Specify grid spacing
**Args:** `prepare_gpf4.py -r receptor.pdbqt -l ligand.pdbqt -p spacing=0.25 -o receptor.gpf && autogrid4 -p receptor.gpf -l receptor.glg`
**Explanation:** Uses finer grid spacing (0.25Å) for higher resolution energy maps.
