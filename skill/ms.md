---
name: ms
category: simulation
description: Efficient coalescent simulation program for population genetics studies.
tags: [ms, simulation, population-genetics]
author: oxo-call-community
source_url: "https://github.com/gbradley/ms"
---

## Concepts

- **Tool Overview**: ms v2014_03_04 performs efficient coalescent simulation.
- **Core Function**: Simulates DNA sequence evolution under population genetics models.
- **Coalescent Theory**: Implements standard coalescent simulation.
- **Population Genetics**: Models evolutionary processes in populations.
- **Efficient Simulation**: Optimized for large-scale simulations.
- **Input/Output**: Accepts parameters; outputs simulated sequences.

## Pitfalls

- **Parameter Complexity**: Complex command-line interface.
- **Memory Requirements**: Memory usage depends on simulation size.
- **Parameter Tuning**: Requires careful parameter specification.
- **Simulation Time**: Large simulations can be time-consuming.
- **Random Seed**: Should specify random seed for reproducibility.
- **Output Format**: Output format requires parsing.

## Examples

### Basic coalescent simulation
**Args:** `ms 10 1 -t 100`
**Explanation:** Simulates 10 sequences with 100 segregating sites.

### With recombination
**Args:** `ms 10 1 -t 100 -r 100 1000`
**Explanation:** Simulates with recombination rate of 100.

### Population structure
**Args:** `ms 10 1 -t 100 -I 2 5 5`
**Explanation:** Simulates two subpopulations with migration.

### Demographic model
**Args:** `ms 10 1 -t 100 -eN 0.1 0.5`
**Explanation:** Implements population size change.

### Gene conversion
**Args:** `ms 10 1 -t 100 -c 10 1`
**Explanation:** Includes gene conversion in simulation.