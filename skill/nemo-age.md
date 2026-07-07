---
name: nemo-age
category: population-genomics
description: Nemo-age models genetic and phenotypic evolution in populations with overlapping generations, seed banks, and multiple age classes.
tags: [nemo-age, population-genomics, evolution, simulation]
author: oxo-call-community
source_url: "https://bitbucket.org/ecoevo/nemo-age-release"
---

## Concepts

- **Tool Overview**: Nemo-age is a population genetics simulation tool with age-structured populations.
- **Core Function**: Models evolutionary processes in age-structured populations.
- **Algorithm**: Uses forward-time population genetics simulation with age classes.
- **Input Format**: Accepts configuration files with population parameters.
- **Output**: Produces population genetic data and evolutionary statistics.
- **Use Case**: Population genetics research, evolutionary modeling, and conservation biology.

## Pitfalls

- **Complex Configuration**: Requires detailed parameter configuration.
- **Computational Cost**: Simulating large populations is computationally intensive.
- **Memory Usage**: Large simulations require significant memory.
- **Version Differences**: Options may vary between versions.
- **Parameter Sensitivity**: Results depend on parameter settings.
- **Long Simulation Time**: Complex scenarios may require extensive computation.

## Examples

### Display help
**Args:** `nemo-age --help`
**Explanation:** Shows available options and usage instructions.

### Basic simulation
**Args:** `nemo-age -c config.txt -o output/`
**Explanation:** Runs simulation with configuration file.

### Create configuration
**Args:** `nemo-age init -o config.txt`
**Explanation:** Generates template configuration file.

### Age-class model
**Args:** `nemo-age -c config.txt --age-classes 5 -o output/`
**Explanation:** Simulates with 5 age classes.

### Seed bank model
**Args:** `nemo-age -c config.txt --seed-bank -o output/`
**Explanation:** Includes seed bank in simulation.

### Selection pressure
**Args:** `nemo-age -c config.txt --selection 0.1 -o output/`
**Explanation:** Applies selection pressure of 0.1.

### Parallel simulation
**Args:** `nemo-age -c config.txt -t 8 -o output/`
**Explanation:** Uses 8 threads for parallel processing.