---
name: fastsimcoal2
category: utility
description: "fast sequential markov coalescent simulation of genomic data under complex evolutionary models"
tags: [fastsimcoal2, utility, coalescent-simulation, population-genetics, bioinformatics]
author: oxo-call-community
source_url: "http://cmpg.unibe.ch/software/fastsimcoal27/"
---

## Concepts

- **Tool Overview**: fastsimcoal2 is a tool for simulating genomic data under complex evolutionary models using the sequential Markov coalescent approach.
- **Core Function**: Simulates genetic variation under various population genetic models.
- **Input/Output**: Input: Parameter file defining demographic model. Output: Simulated SNP data, trees, statistics.
- **Algorithm**: Uses sequential Markov coalescent for efficient simulation.
- **Key Features**: Complex demographic models, SNP simulation, tree generation, population genetics, forward-time simulation.
- **Installation**: `conda install -c bioconda fastsimcoal2`

## Pitfalls

- **Parameter Complexity**: Requires careful parameter specification.
- **Computation Time**: Complex models may require significant processing time.
- **Memory Usage**: Large simulations may require significant memory.
- **Model Validation**: Results depend on model assumptions.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic simulation
**Args:** `fsc27 -i params.par -o output/`
**Explanation:** Runs simulation with parameter file.

### With validation
**Args:** `fsc27 -i params.par -o output/ -v`
**Explanation:** Validates parameters before simulation.

### Multiple replicates
**Args:** `fsc27 -i params.par -o output/ -r 100`
**Explanation:** Runs 100 simulation replicates.

### Generate trees
**Args:** `fsc27 -i params.par -o output/ -t`
**Explanation:** Generates gene trees.

### Forward simulation
**Args:** `fsc27 -i params.par -o output/ --forward`
**Explanation:** Runs forward-time simulation.