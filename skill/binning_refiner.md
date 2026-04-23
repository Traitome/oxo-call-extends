---
name: binning_refiner
category: metagenomics
description: Improve genome bins through combination of different binning programs
tags: [mag, binning-refinement, metagenomics]
author: oxo-call-community
source_url: "https://github.com/songweizhi/Binning_refiner"
---

## Concepts
- **Tool Overview**: Binning_refiner improves genome bins by combining results from different binning programs. It identifies consensus bins and refines bin boundaries.
- **Multi-Binning Integration**: Takes bins from multiple binning tools (MetaBAT2, MaxBin2, CONCOCT, etc.) and identifies robust bins supported by multiple methods.
- **Refinement Strategy**: Uses consensus and intersection approaches to improve bin quality.
- **Applications**: Improving MAG quality from metagenomic assemblies.

## Pitfalls
- **Input Consistency**: Requires bins from the same assembly; different assemblies cannot be combined.
- **Computational Cost**: Processing multiple binning results requires additional computation.

## Examples
### Refine bins from multiple tools
**Args:** `binning_refiner.py -i metabat/ maxbin/ concoct/ -o refined/`
**Explanation:** Combines bins from three binning tools to produce refined MAGs.
