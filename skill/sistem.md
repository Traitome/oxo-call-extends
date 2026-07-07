---
name: sistem
category: simulation
description: SiSTEM - Tumor growth and DNA-seq simulation
tags: ["sistem", "simulation", "tumor", "dna-seq"]
author: oxo-call-community
source_url: "https://sistem.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: SiSTEM (v1.0.4) simulates tumor growth and DNA-seq data.
- **Core Function**: Generates synthetic tumor genomes with mutations.
- **Algorithm**: Uses agent-based modeling for tumor evolution.
- **Input/Output**: Accepts simulation parameters and produces sequencing data.
- **Tumor Simulation**: Specialized for cancer genomics simulation.
- **Applications**: Cancer research, algorithm testing, benchmarking.

## Pitfalls

- **Memory Usage**: High memory requirements for large simulations.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for realistic simulation.
- **Input Quality**: Results depend on parameter settings.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Simulate tumor
**Args:** `sistem simulate -p params.yaml -o output/`
**Explanation:** `-p` parameter file; `-o` output directory.

### With seed
**Args:** `sistem simulate -p params.yaml -s 12345 -o output/`
**Explanation:** `-s 12345` random seed for reproducibility.

### Generate reads
**Args:** `sistem reads -i tumor_genome.fasta -c 30 -o reads.fastq`
**Explanation:** `-c 30` sequencing coverage.

### Help command
**Args:** `sistem --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sistem --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sistem -v simulate -p params.yaml -o output/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sistem -t 8 simulate -p params.yaml -o output/`
**Explanation:** `-t 8` uses 8 threads.
