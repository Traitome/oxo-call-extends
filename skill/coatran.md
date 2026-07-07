---
name: coatran
category: population-genomics
description: Coalescent tree simulation along a transmission network
tags: [coatran, coalescent-simulation, transmission-network, population-genetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/niemasd/CoaTran"
---

## Concepts

- **Tool Overview**: CoaTran is a tool for simulating coalescent trees along a transmission network, combining coalescent theory with transmission dynamics.
- **Core Function**: Simulates genetic sequences evolving along a transmission network with coalescent events.
- **Algorithm**: Integrates coalescent simulation with transmission network models to generate realistic genetic data.
- **Input**: Transmission network in Newick or similar format.
- **Output**: Simulated genetic sequences and coalescent trees.
- **Application**: Epidemiology, pathogen evolution, and transmission dynamics studies.
- **Installation**: Install via bioconda: `conda install -c bioconda coatran`

## Pitfalls

- **Network Format**: Requires properly formatted transmission network.
- **Parameter Selection**: Requires careful selection of population genetic parameters.
- **Computational Resources**: May require significant resources for complex simulations.
- **Model Assumptions**: Results depend on coalescent and transmission model assumptions.
- **Output Size**: Large simulations can generate substantial output files.

## Examples

### Simulate coalescent along transmission network
**Args:** `coatran -i transmission.nwk -o simulated_data/`
**Explanation:** Simulates coalescent trees along transmission network.

### With mutation rate
**Args:** `coatran -i transmission.nwk -m 1e-8 -o simulated_data/`
**Explanation:** Sets mutation rate to 1e-8 per generation.

### With sample times
**Args:** `coatran -i transmission.nwk -t sampling_times.txt -o simulated_data/`
**Explanation:** Uses specified sampling times for nodes.

### Display help
**Args:** `coatran --help`
**Explanation:** Shows all available options and usage information.