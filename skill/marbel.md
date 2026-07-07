---
name: marbel
category: expression
description: Marbel generates realistic in silico metatranscriptomic dataset based on specified parameters.
tags: [marbel, expression, metatranscriptomics, simulation]
author: oxo-call-community
source_url: "https://github.com/jlab/marbel"
---

## Concepts

- **Tool Overview**: marbel v0.2.4 - Generates realistic in silico metatranscriptomic datasets based on specified parameters.
- **Core Function**: Simulates metatranscriptomic sequencing data for testing and validation.
- **Input/Output**: Input: Configuration file, reference sequences; Output: Simulated FASTQ reads.
- **Installation**: `conda install -c bioconda marbel`
- **In Silico Simulation**: Generates simulated sequencing data with realistic characteristics.
- **Metatranscriptomics**: Specifically designed for metatranscriptomic data simulation.

## Pitfalls

- **Parameter Configuration**: Incorrect parameters produce unrealistic data.
- **Reference Data**: Requires comprehensive reference sequences.
- **Computational Resources**: Large simulations require significant memory.
- **Realism**: Simulated data may not perfectly match real sequencing data.
- **Format Compatibility**: Requires specific input formats.
- **Seed Selection**: Random seed affects reproducibility.

## Examples

### Generate simulated data
**Args:** `marbel -c config.yaml -o simulated_reads/`
**Explanation:** Generates simulated metatranscriptomic data.

### With custom parameters
**Args:** `marbel -c config.yaml -o simulated_reads/ --params params.txt`
**Explanation:** Uses custom parameter file.

### Paired-end simulation
**Args:** `marbel -c config.yaml -o simulated_reads/ --paired-end`
**Explanation:** Generates paired-end reads.

### Verbose mode
**Args:** `marbel -c config.yaml -o simulated_reads/ -v`
**Explanation:** Provides detailed logging during simulation.

### Quality control
**Args:** `marbel -c config.yaml -o simulated_reads/ --qc`
**Explanation:** Performs quality control on output.

### Reproducible simulation
**Args:** `marbel -c config.yaml -o simulated_reads/ --seed 12345`
**Explanation:** Sets random seed for reproducibility.