---
name: density-fitness
category: utility
description: Application to calculate density statistics (RSR, SRSR, RSCCS, EDIAm and OPIA) for X-ray structures.
tags: [density-fitness, utility, crystallography, x-ray, structure-validation]
author: oxo-call-community
source_url: "https://github.com/PDB-REDO/density-fitness"
---

## Concepts

- **Tool Overview**: density-fitness v1.2.0 - Calculates electron density metrics for X-ray crystallography structures.
- **Core Function**: Computes RSR, SRSR, RSCC, EDIAm and OPIA density statistics for main- and side-chain atoms.
- **Input/Output**: Expects PDB/mmCIF structure files and MTZ/density maps; outputs per-residue density metrics.
- **Installation**: `conda install -c bioconda density-fitness`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires structure model and electron density maps (2mFo-DFc and mFo-DFc).

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `density-fitness --model structure.cif --mtz data.mtz --output metrics.tsv`
**Explanation:** Calculates density fitness metrics for X-ray structure.
