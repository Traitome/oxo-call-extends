---
name: curves
category: formatting
description: CURVES+ - Conformational analysis of nucleic acid structures and MD trajectories
tags: [curves, formatting, nucleic-acid, structure-analysis, MD-trajectories]
author: oxo-call-community
source_url: "http://curvesplus.bsc.es/misc"
---

## Concepts

- **Tool Overview**: curves (v3.0.3+) is CURVES+, a tool for conformational analysis of nucleic acid structures and molecular dynamics trajectories.
- **Core Function**: Analyzes nucleic acid structure parameters including helical parameters, base pairing, and backbone conformation.
- **Input/Output**: Input: PDB files, MD trajectory files. Output: Structural parameter files, analysis reports.
- **Key Features**: Supports single structures and MD trajectories, follows international nucleic acid conventions, fast parallel processing.
- **Installation**: `conda install -c bioconda curves`

## Pitfalls

- **PDB Format**: Requires properly formatted PDB files with standard atom naming.
- **Trajectory Format**: Supports specific trajectory formats; may need conversion.
- **Memory Usage**: Long MD trajectories may require significant memory.
- **Parameter Selection**: Choose appropriate parameters for specific analysis goals.
- **Output Interpretation**: Results require structural biology knowledge for proper interpretation.

## Examples

### Analyze single PDB structure
**Args:** `curves -i structure.pdb -o output.txt`
**Explanation:** Analyze nucleic acid structure parameters from PDB file.

### Process MD trajectory
**Args:** `curves -i trajectory.xtc -s structure.pdb -o traj_results/`
**Explanation:** Analyze conformational changes across MD trajectory frames.

### Generate helical parameters
**Args:** `curves -i structure.pdb -o helical.txt --helical`
**Explanation:** Extract helical parameters from nucleic acid structure.
