---
name: fwdpy
category: population-genomics
description: Forward-time population genetic simulation in Python.
tags: [fwdpy, population genetics, Python, simulation]
author: oxo-call-community
source_url: "http://pypi.python.org/pypi/fwdpy"
---

## Concepts
- **Forward-time Simulation**: Simulates population genetic processes forward in time.
- **Python Library**: Pure Python implementation for population genetics.
- **Genetic Drift**: Models genetic drift and population dynamics.
- **Mutation**: Models mutation processes in populations.
- **Selection**: Incorporates natural selection into simulations.

## Pitfalls
- **Performance**: Slower than compiled implementations.
- **Memory Usage**: High memory usage for large populations.
- **Deprecated**: Consider using fwdpy11 instead.
- **Limited Features**: May lack advanced features of newer tools.
- **Python Version**: May require specific Python versions.

## Examples
### Initialize population
**Args:** `python -c "import fwdpy; pop = fwdpy.DiploidPopulation(1000, 1e4)"`
**Explanation:** Creates a diploid population with 1000 individuals.

### Run simulation
**Args:** `python -c "import fwdpy; pop = fwdpy.DiploidPopulation(1000, 1e4); fwdpy.evolve(pop, 100)"`
**Explanation:** Evolves population for 100 generations.

### With mutation rate
**Args:** `python -c "import fwdpy; pop = fwdpy.DiploidPopulation(1000, 1e4); fwdpy.evolve(pop, 100, mu=1e-8)"`
**Explanation:** Runs simulation with specified mutation rate.

### Save to file
**Args:** `python -c "pop.dump('pop.dat')"`
**Explanation:** Saves population to binary file.

### Load from file
**Args:** `python -c "pop = fwdpy.DiploidPopulation.load('pop.dat')"`
**Explanation:** Loads population from binary file.