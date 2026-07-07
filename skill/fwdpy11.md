---
name: fwdpy11
category: population-genomics
description: Forward-time population genetic simulation in Python.
tags: [fwdpy11, population genetics, Python, simulation]
author: oxo-call-community
source_url: "https://github.com/molpopgen/fwdpy11"
---

## Concepts
- **Forward-time Simulation**: Simulates population genetic processes forward in time.
- **Python Interface**: Python bindings for efficient C++ backend.
- **Population Genetics**: Models genetic variation, selection, and drift.
- **Modern API**: Clean, Pythonic API design.
- **High Performance**: Combines Python ease-of-use with C++ performance.

## Pitfalls
- **Memory Usage**: Large simulations require significant memory.
- **Performance**: Slower than pure C++ implementations.
- **Complex Models**: Complex demographic models require careful setup.
- **Dependency**: Requires proper installation of C++ dependencies.
- **Learning Curve**: Understanding population genetics required.

## Examples
### Run basic simulation
**Args:** `python -c "import fwdpy11; pop = fwdpy11.DiploidPopulation(1000, 1e4); params = fwdpy11.ModelParams(); fwdpy11.evolvets(pop, params, 100)"`
**Explanation:** Runs basic population simulation.

### With selection
**Args:** `python simulation.py --selection --generations 1000`
**Explanation:** Runs simulation with selection.

### Save population
**Args:** `python -c "pop.dump('population.fwdpy11')"`
**Explanation:** Saves population state to file.

### Load population
**Args:** `python -c "pop = fwdpy11.DiploidPopulation.load('population.fwdpy11')"`
**Explanation:** Loads population from file.

### Output VCF
**Args:** `python -c "fwdpy11.tskit_to_vcf(pop.tables, 'output.vcf')"`
**Explanation:** Exports simulation results as VCF.