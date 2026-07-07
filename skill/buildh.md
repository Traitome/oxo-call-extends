---
name: buildh
category: utility
description: Build hydrogen atoms from united-atom molecular dynamics of lipids and calculate order parameters
tags: [buildh, molecular-dynamics, lipids, hydrogen, order-parameter]
author: oxo-call-community
source_url: "https://buildh.readthedocs.io/"
---

## Concepts

- **Tool Overview**: buildh reconstructs hydrogen atoms from united-atom molecular dynamics simulations of lipid bilayers.
- **Core Function**: Adds hydrogen atoms to united-atom MD trajectories and calculates lipid order parameters.
- **Input**: GROMACS trajectory files in united-atom representation.
- **Output**: Full-atom trajectory with hydrogen atoms and order parameter calculations.
- **Application**: Lipid bilayer analysis in molecular dynamics simulations.
- **Installation**: Install via bioconda: `conda install -c bioconda buildh`

## Pitfalls

- **Lipid Specific**: Designed for lipid bilayer simulations.
- **Input Format**: Requires specific input format from GROMACS.
- **Force Field**: Must match the force field used in simulation.
- **Trajectory Quality**: Results depend on simulation quality.

## Examples

### Build hydrogen atoms
**Args:** `buildh -f traj.xtc -s topol.tpr -o traj_h.xtc`
**Explanation:** Adds hydrogen atoms to united-atom trajectory.

### Calculate order parameters
**Args:** `buildh -f traj.xtc -s topol.tpr --order -o order_params.dat`
**Explanation:** Calculates lipid order parameters from trajectory.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.