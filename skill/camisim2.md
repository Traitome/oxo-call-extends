---
name: camisim2
category: metagenomics
description: Simulate metagenome datasets with realistic microbial community profiles
tags: [camisim, metagenomics, simulation, cami]
author: oxo-call-community
source_url: "https://github.com/CAMI-challenge/CAMISIM"
---

## Concepts

- **Tool Overview**: CAMISIM simulates realistic metagenome sequencing datasets.
- **Core Function**: Generates synthetic metagenomes with known ground truth for benchmarking.
- **Features**: Models abundance distributions, sequencing errors, and community structure.
- **Input**: Configuration file specifying genomes, abundances, and sequencing parameters.
- **Output**: Simulated FASTQ files with known taxonomic composition.
- **Application**: Benchmarking metagenomics analysis tools.
- **Installation**: Install via bioconda: `conda install -c bioconda camisim2`

## Pitfalls

- **Configuration**: Requires careful configuration file setup.
- **Genome Database**: Needs reference genomes for simulation.
- **Disk Space**: Large simulations require significant storage.
- **Runtime**: Complex simulations can take hours.

## Examples

### Run simulation
**Args:** `camisim metagenomesimulation.ini -o simulated_data/`
**Explanation:** Runs metagenome simulation using configuration file.

### Set random seed
**Args:** `camisim metagenomesimulation.ini -s 12345 -o simulated_data/`
**Explanation:** Uses fixed random seed for reproducible simulation.

### Display help
**Args:** `camisim --help`
**Explanation:** Shows all available options and usage information.
