---
name: nemo
category: utility
description: Nemo is an individual-based forward-time population genetics simulation software.
tags: [nemo, utility, population-genetics, simulation, evolution]
author: oxo-call-community
source_url: "http://nemo2.sourceforge.net"
---

## Concepts

- **Tool Overview**: Nemo is an individual-based forward-time population genetics simulation tool.
- **Core Function**: Models genetic evolution in structured populations over generations.
- **Algorithm**: Uses forward-time simulation to track individual genotypes and phenotypes.
- **Input Format**: Accepts configuration files with population parameters.
- **Output**: Produces genetic data and evolutionary statistics.
- **Use Case**: Population genetics research, evolutionary modeling, and theoretical biology.

## Pitfalls

- **Complex Configuration**: Requires detailed parameter setup.
- **Computational Cost**: Simulating large populations is computationally intensive.
- **Memory Usage**: Large simulations require significant memory.
- **Version Differences**: Options may vary between versions.
- **Parameter Sensitivity**: Results depend on parameter settings.
- **Long Simulation Time**: Complex scenarios may require extensive computation.

## Examples

### Display help
**Args:** `nemo --help`
**Explanation:** Shows available options and usage instructions.

### Basic simulation
**Args:** `nemo -c config.txt -o output/`
**Explanation:** Runs simulation with configuration file.

### Create configuration
**Args:** `nemo init -o config.txt`
**Explanation:** Generates template configuration file.

### Population structure
**Args:** `nemo -c config.txt --structure 5 -o output/`
**Explanation:** Simulates with 5 subpopulations.

### Migration rate
**Args:** `nemo -c config.txt --migration 0.01 -o output/`
**Explanation:** Sets migration rate to 0.01.

### Selection pressure
**Args:** `nemo -c config.txt --selection 0.1 -o output/`
**Explanation:** Applies selection pressure of 0.1.

### Output statistics
**Args:** `nemo -c config.txt -s stats.tsv -o output/`
**Explanation:** Outputs population statistics.