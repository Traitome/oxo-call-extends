---
name: msprime
category: simulation
description: Fast and accurate coalescent simulator for population genetics.
tags: [msprime, simulation, population-genetics]
author: oxo-call-community
source_url: "https://github.com/tskit-dev/msprime"
---

## Concepts

- **Tool Overview**: msprime v0.4.0 performs efficient coalescent simulation.
- **Core Function**: Simulates genealogical histories using coalescent theory.
- **Fast Simulation**: Optimized for large-scale population genetic simulations.
- **Tree Sequences**: Uses tree sequence format for efficient storage.
- **Python API**: Provides Python interface for simulations.
- **Input/Output**: Accepts simulation parameters; outputs tree sequences.

## Pitfalls

- **Python Dependency**: Requires Python environment.
- **Memory Requirements**: Memory usage depends on simulation complexity.
- **Parameter Tuning**: May require parameter adjustment for demographics.
- **Simulation Time**: Large simulations can be time-consuming.
- **Random Seed**: Should specify random seed for reproducibility.
- **Output Format**: Tree sequence format requires learning.

## Examples

### Simulate coalescent tree
**Args:** `msprime simulate --sample-size 10 --length 1000 --recombination-rate 1e-8`
**Explanation:** Simulates coalescent tree for 10 samples.

### With demographic model
**Args:** `msprime simulate --sample-size 10 --demography bottleneck.model -o tree.trees`
**Explanation:** Uses bottleneck demographic model.

### Generate mutations
**Args:** `msprime simulate --sample-size 10 --mutation-rate 1e-8 -o tree.trees`
**Explanation:** Adds mutations along branches.

### Load and analyze tree sequence
**Args:** `msprime.load("tree.trees")`
**Explanation:** Loads and analyzes tree sequence in Python.

### Export to Newick
**Args:** `msprime.write_newick("tree.trees", "tree.newick")`
**Explanation:** Exports tree to Newick format.