---
name: minnow
category: expression
description: A principled framework for rapid simulation of dscRNA-seq data at the read level
tags: [minnow, expression, simulation]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/minnow"
---

## Concepts

- **Tool Overview**: Minnow v1.2 simulates single-cell RNA-seq data at read level.
- **Core Function**: Generates synthetic scRNA-seq sequencing data.
- **Read-level Simulation**: Simulates sequencing reads at individual read level.
- **RNA-seq Simulation**: Generates realistic scRNA-seq datasets.
- **Input/Output**: Accepts parameters; outputs simulated reads.
- **Benchmarking**: Supports method benchmarking workflows.

## Pitfalls

- **Computational Resources**: Simulation may require significant resources.
- **Memory Requirements**: Memory usage depends on simulation scale.
- **Parameter Tuning**: May require parameter adjustment for realistic results.
- **Data Quality**: Simulation accuracy depends on parameter settings.
- **Runtime**: Complex simulations can be time-consuming.
- **Model Assumptions**: Based on specific biological assumptions.

## Examples

### Simulate scRNA-seq data
**Args:** `minnow -c config.json -o simulated_reads.fastq`
**Explanation:** Generates simulated scRNA-seq reads.

### With custom parameters
**Args:** `minnow -c config.json -o simulated_reads.fastq -p params.yaml`
**Explanation:** Uses custom simulation parameters.

### Multiple cells
**Args:** `minnow -c config.json -o output/ -n 100`
**Explanation:** Simulates 100 cells.

### Batch processing
**Args:** `minnow -c configs/ -o outputs/`
**Explanation:** Processes multiple configuration files.

### Generate statistics
**Args:** `minnow -c config.json -o simulated_reads.fastq -s stats.txt`
**Explanation:** Generates simulation statistics.