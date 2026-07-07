---
name: selam
category: population-genomics
description: selam - Simulation of Epistasis, Local adaptation, Ancestry and Mate choice
tags: ["selam", "population-genomics", "simulation", "epistasis"]
author: oxo-call-community
source_url: "https://github.com/russcd/SELAM"
---

## Concepts

- **Tool Overview**: selam (v0.9) simulates population genetics with epistasis, local adaptation, ancestry, and mate choice.
- **Core Function**: Simulates complex evolutionary scenarios in structured populations.
- **Algorithm**: Uses forward-time population genetic simulation.
- **Input/Output**: Accepts configuration files and produces population genetic outputs.
- **Epistasis Modeling**: Specifically designed to model epistatic interactions.
- **Applications**: Population genetics research, evolutionary biology, and adaptation studies.

## Pitfalls

- **Computational Resources**: May require significant compute resources for large simulations.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Configuration Complexity**: Configuration files can be complex.
- **Memory Usage**: High memory requirements for large population sizes.
- **Run Time**: Long simulation times for complex scenarios.
- **Documentation**: Some features have limited documentation.

## Examples

### Run simulation
**Args:** `selam -c config.txt -o output/`
**Explanation:** `-c` configuration file; `-o` output directory.

### Verbose mode
**Args:** `selam -c config.txt -v -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Check configuration
**Args:** `selam -c config.txt --check`
**Explanation:** Validates configuration file.

### Help command
**Args:** `selam --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `selam --version`
**Explanation:** Shows current version.

### Example configuration
**Args:** `selam --example-config > config.txt`
**Explanation:** Generates example configuration file.

### Debug mode
**Args:** `selam -c config.txt -d -o output/`
**Explanation:** `-d` enables debug mode.