---
name: scrnasim-toolz
category: single-cell
description: scrnasim-toolz - Tools used by scRNAsim workflow
tags: ["scrnasim-toolz", "single-cell", "RNA-seq", "simulation"]
author: oxo-call-community
source_url: "https://github.com/zavolanlab/scRNAsim-toolz"
---

## Concepts

- **Tool Overview**: scrnasim-toolz (v0.1.1) provides tools used by the scRNAsim workflow.
- **Core Function**: Supports single-cell RNA-seq data simulation.
- **Algorithm**: Implements various simulation strategies for scRNA-seq data.
- **Input/Output**: Accepts configuration files and produces simulated data.
- **Workflow Integration**: Designed to work with the scRNAsim pipeline.
- **Applications**: Single-cell RNA-seq simulation, method testing, and benchmarking.

## Pitfalls

- **Workflow Dependency**: Designed for use with scRNAsim workflow.
- **Parameter Tuning**: Requires careful adjustment for realistic simulations.
- **Computational Resources**: May require significant compute resources.
- **Memory Usage**: High memory requirements for large simulations.
- **Documentation**: Some features have limited documentation.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Run simulation
**Args:** `scrnasim-toolz simulate -c config.yaml -o output/`
**Explanation:** `-c` configuration file; `-o` output directory.

### Generate config
**Args:** `scrnasim-toolz generate-config -o config.yaml`
**Explanation:** Generates template configuration file.

### Validate config
**Args:** `scrnasim-toolz validate-config -c config.yaml`
**Explanation:** Validates configuration file.

### Verbose logging
**Args:** `scrnasim-toolz simulate -c config.yaml -v -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `scrnasim-toolz --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `scrnasim-toolz --version`
**Explanation:** Shows current version.

### List commands
**Args:** `scrnasim-toolz list`
**Explanation:** Lists available commands.