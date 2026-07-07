---
name: 2pg_cartesian
category: utility
description: Framework of optimization algorithms for protein structure prediction using Cartesian coordinates.
tags: [2pg_cartesian, utility, protein, structure-prediction, optimization, evolutionary-computation, structural-biology]
author: oxo-call-community
source_url: "https://github.com/rodrigofaccioli/2pg_cartesian"
---

## Concepts

- **Tool Overview**: 2pg_cartesian is a framework of evolutionary computation algorithms designed for structural biology applications, particularly protein structure prediction using Cartesian coordinates. Version 1.0.1.
- **Core Function**: Provides a framework for building and running optimization algorithms to predict protein 3D structures by optimizing atomic coordinates.
- **Input/Output**: Input is typically protein structure files; output is predicted 3D coordinates in standard structural biology formats.
- **Installation Methods**:
  - Install via bioconda: `conda install -c bioconda 2pg_cartesian`
  - Install via mamba: `mamba install 2pg_cartesian`
  - Build from source using cmake 2.8+: `mkdir build && cd build && cmake .. && make && make install`
- **Platform Support**: Linux (x86_64) only
- **Dependencies**: Requires GROMACS, libgcc-ng >=12, libstdcxx-ng >=12
- **License**: Apache License 2.0

## Pitfalls

- **Linux Only**: This tool only runs on Linux x86_64 systems. Not available for macOS or Windows.
- **Build from Source Complexity**: When building from source, cmake 2.8 or later is required. Use `-DCMAKE_INSTALL_PREFIX` to specify custom installation directory.
- **GROMACS Dependency**: Requires GROMACS to be installed as a dependency for molecular dynamics components.
- **Limited Documentation**: As a framework for algorithm development, specific usage depends on the algorithms being implemented. Users may need to refer to source code and examples.
- **Evolutionary Computation Background**: Effective use requires understanding of evolutionary algorithms and structural biology concepts.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available command-line options and usage information. Use this to discover available parameters for your specific installation.

### Basic structure prediction
**Args:** `input.pdb output.pdb`
**Explanation:** Runs protein structure prediction using the framework's default optimization algorithm on the input structure file and writes the predicted coordinates to output.

### Run with custom configuration file
**Args:** `-c config.ini input.pdb output.pdb`
**Explanation:** Uses a custom configuration file to specify optimization parameters such as population size, mutation rate, and convergence criteria.

### Specify number of generations
**Args:** `-g 1000 input.pdb output.pdb`
**Explanation:** Sets the maximum number of evolutionary generations to 1000 for the optimization process. Higher values may improve results but increase runtime.

### Run with population size specification
**Args:** `-p 100 input.pdb output.pdb`
**Explanation:** Sets the population size to 100 individuals for the evolutionary algorithm. Larger populations explore more of the solution space but require more computational resources.
