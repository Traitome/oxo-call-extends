---
name: biobb_cp2k
category: utility
description: BioBB category for CP2K quantum mechanics package
tags: [bioexcel, cp2k, quantum-mechanics, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_cp2k"
---

## Concepts
- **Tool Overview**: biobb_cp2k wraps the CP2K quantum mechanics/molecular mechanics package for BioBB workflows. CP2K performs ab initio and DFT calculations.
- **QM/MM Calculations**: Supports density functional theory, molecular dynamics, and geometry optimization at quantum mechanical level.
- **Applications**: Electronic structure calculations, QM/MM simulations, spectroscopy prediction.

## Pitfalls
- **CP2K Dependency**: Requires CP2K installation separately.
- **Computational Cost**: QM calculations are significantly more expensive than classical MD.

## Examples
### Run DFT calculation
**Args:** `biobb_cp2k.cp2k --input structure.pdb --config dft_config.yml --output energies.out`
**Explanation:** Runs a DFT energy calculation using CP2K.
