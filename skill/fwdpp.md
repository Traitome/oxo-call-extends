---
name: fwdpp
category: population-genomics
description: A C++ template library for forward-time population genetic simulation.
tags: [fwdpp, population genetics, C++, simulation]
author: oxo-call-community
source_url: "https://www.github.com/molpopgen/fwdpp"
---

## Concepts
- **Forward-time Simulation**: Simulates population genetic processes forward in time.
- **C++ Template Library**: High-performance C++ template-based library.
- **Population Genetics**: Models genetic variation and evolution.
- **Flexible Design**: Highly customizable simulation framework.
- **Efficient Algorithms**: Optimized for large-scale simulations.

## Pitfalls
- **C++ Expertise**: Requires C++ programming knowledge.
- **Complex API**: Steep learning curve for the API.
- **Compilation**: Requires proper compilation setup.
- **Memory Management**: Manual memory management required.
- **Performance Tuning**: Requires performance optimization for large simulations.

## Examples
### Basic population simulation
**Args:** `g++ -std=c++17 -O2 simulation.cpp -o simulation -lfwdpp`
**Explanation:** Compiles a population simulation program.

### Run simulation
**Args:** `./simulation --pop-size 1000 --generations 1000`
**Explanation:** Runs simulation with population size 1000 for 1000 generations.

### With selection
**Args:** `./simulation --pop-size 1000 --selection --generations 1000`
**Explanation:** Runs simulation with natural selection.

### Output VCF
**Args:** `./simulation --pop-size 1000 --vcf -o output.vcf`
**Explanation:** Outputs simulation results as VCF file.

### Parallel simulation
**Args:** `./simulation --pop-size 1000 --threads 8`
**Explanation:** Runs simulation using 8 threads.