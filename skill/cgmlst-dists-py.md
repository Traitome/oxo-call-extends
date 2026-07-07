---
name: cgmlst-dists-py
category: genomics
description: High-performance pairwise Hamming distance calculator for cgMLST data with GPU acceleration
tags: [cgmlst-dists-py, cgmlst, distance-matrix, gpu, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/genpat-it/cgmlst-dists-py"
---

## Concepts

- **Tool Overview**: cgmlst-dists-py is a high-performance pairwise Hamming distance calculator optimized for cgMLST data with optional GPU acceleration.
- **Core Function**: Computes pairwise genetic distances between bacterial isolates using Hamming distance metric.
- **Algorithm**: Implements optimized Hamming distance calculation with GPU support for parallel processing.
- **Input**: cgMLST allele table in CSV or tab-delimited format.
- **Output**: Distance matrix in various formats (PHYLIP, CSV, JSON).
- **Application**: Rapid bacterial strain comparison for epidemiological analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cgmlst-dists-py`

## Pitfalls

- **GPU Availability**: GPU acceleration requires compatible NVIDIA GPU and CUDA.
- **Memory Requirements**: Large datasets may require significant GPU memory.
- **Input Format**: Requires specific cgMLST allele table format.
- **CUDA Setup**: Proper CUDA installation required for GPU acceleration.

## Examples

### Calculate distances with CPU
**Args:** `cgmlst-dists-py -i alleles.csv -o distances.matrix`
**Explanation:** Computes pairwise distances using CPU.

### Enable GPU acceleration
**Args:** `cgmlst-dists-py -i alleles.csv -o distances.matrix --gpu`
**Explanation:** Uses GPU for accelerated distance calculation.

### Output PHYLIP format
**Args:** `cgmlst-dists-py -i alleles.csv -o distances.phylip --format phylip`
**Explanation:** Outputs distance matrix in PHYLIP format.

### Display help
**Args:** `cgmlst-dists-py --help`
**Explanation:** Shows all available options and usage information.