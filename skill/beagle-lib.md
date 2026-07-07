---
name: beagle-lib
category: programming
description: beagle-lib - Library for evaluating sequence evolution likelihood on phylogenetic trees
tags: [beagle-lib, programming, phylogenetics, likelihood-calculation, tree-inference]
author: oxo-call-community
source_url: "https://github.com/beagle-dev/beagle-lib/blob/v4.0.1/README.md"
---

## Concepts

- **Tool Overview**: beagle-lib (v4.0.1) is a high-performance library for evaluating the likelihood of sequence evolution on phylogenetic trees, used by many phylogenetic inference tools.
- **Core Function**: Computes maximum likelihood scores for sequence alignments on phylogenetic trees.
- **Likelihood Calculation**: Efficiently calculates evolutionary likelihoods using numerical methods.
- **Parallel Processing**: Supports parallel computation across multiple CPU cores and GPUs.
- **Phylogenetic Integration**: Used as backend by tools like BEAST, RAxML, and MrBayes.
- **Input/Output**: Accepts sequence alignments and tree topologies; outputs likelihood scores.
- **Installation**: `conda install -c bioconda beagle-lib`.

## Pitfalls

- **Library Dependency**: Designed as a library, not a standalone tool.
- **Tree Format**: Requires properly formatted phylogenetic tree input.
- **Alignment Quality**: Likelihood calculations depend on alignment quality.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Version Differences**: Options may vary between versions. Check documentation for your version.

## Examples

### Build and install
**Args:** `cd beagle-lib && mkdir build && cd build && cmake .. && make && make install`
**Explanation:** Compiles and installs beagle-lib from source.

### Test installation
**Args:** `beagle-test`
**Explanation:** Runs test suite to verify installation.

### Check available resources
**Args:** `beagle-info`
**Explanation:** Displays available computational resources (CPU/GPU).

### Python binding usage
**Args:** `python -c "import pybeagle; beagle = pybeagle.Beagle(); print(beagle.getResourceCount())"`
**Explanation:** Uses Python bindings to access beagle-lib functionality.

### Set thread count
**Args:** `export BEAGLE_NUM_THREADS=8`
**Explanation:** Sets number of threads for parallel computation.

### Use GPU acceleration
**Args:** `export BEAGLE_USE_GPU=true`
**Explanation:** Enables GPU acceleration if available.

### Display help
**Args:** `beagle-info --help`
**Explanation:** Shows available options and system information.