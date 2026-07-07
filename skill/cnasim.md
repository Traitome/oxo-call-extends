---
name: cnasim
category: formatting
description: Improved simulation of single-cell copy number profiles and DNA-seq data from tumors
tags: [cnasim, copy-number, single-cell, simulation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/samsonweiner/CNAsim"
---

## Concepts

- **Tool Overview**: CNAsim is a software package for improved simulation of single-cell copy number alteration (CNA) profiles and DNA-seq data from tumors.
- **Core Function**: Simulates realistic copy number profiles and sequencing data to test CNA detection algorithms.
- **Algorithm**: Models tumor evolution and generates synthetic CNA profiles with realistic noise and biases.
- **Input**: Configuration parameters for simulation (ploidy, tumor purity, etc.).
- **Output**: Simulated copy number profiles and synthetic sequencing data.
- **Application**: Algorithm testing, benchmarking CNA detection tools, and method development.
- **Installation**: Install via bioconda: `conda install -c bioconda cnasim`

## Pitfalls

- **Parameter Selection**: Requires careful selection of simulation parameters.
- **Realism**: Simulation may not perfectly capture all aspects of real data.
- **Computational Resources**: May require significant resources for large simulations.
- **Output Size**: Large simulations can generate substantial output files.
- **Model Assumptions**: Results depend on underlying simulation model assumptions.

## Examples

### Simulate CNA profiles
**Args:** `cnasim -o simulated_data/`
**Explanation:** Generates simulated copy number profiles with default parameters.

### With custom ploidy
**Args:** `cnasim -p 3 -o simulated_data/`
**Explanation:** Simulates with average ploidy of 3.

### With tumor purity
**Args:** `cnasim -t 0.7 -o simulated_data/`
**Explanation:** Simulates with 70% tumor purity.

### Display help
**Args:** `cnasim --help`
**Explanation:** Shows all available options and usage information.