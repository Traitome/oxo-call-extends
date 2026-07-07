---
name: mlrho
category: variant-calling
description: Takes as input a file with assembled reads from a single diploid individual and returns maximum likelihood estimates of the population mutation rate, the sequencing error, the zygosity correlation, and the population recombination rate.
tags: [mlrho, variant-calling, population-genetics]
author: oxo-call-community
source_url: "http://guanine.evolbio.mpg.de/mlRho/"
---

## Concepts

- **Tool Overview**: mlRho v2.9 estimates population genetic parameters from sequencing data.
- **Core Function**: Computes maximum likelihood estimates of population parameters.
- **Population Genetics**: Estimates mutation rate, recombination rate, and error rate.
- **Diploid Analysis**: Designed for diploid individual data.
- **Input/Output**: Accepts sequence data; outputs parameter estimates.
- **Evolutionary Analysis**: Supports population genetic inference.

## Pitfalls

- **Diploid Specific**: Designed for diploid organisms.
- **Computational Resources**: May require significant computational resources.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal estimation.
- **Data Quality**: Results depend on input sequence quality.
- **Model Assumptions**: Relies on population genetic model assumptions.

## Examples

### Estimate population parameters
**Args:** `mlrho -i sequences.fasta -o estimates.txt`
**Explanation:** Estimates population genetic parameters.

### With verbose output
**Args:** `mlrho -i sequences.fasta -o estimates.txt -v`
**Explanation:** Shows detailed estimation process.

### Custom model
**Args:** `mlrho -i sequences.fasta -o estimates.txt -m custom.model`
**Explanation:** Uses custom model configuration.

### Batch processing
**Args:** `mlrho -i fasta/ -o estimates/`
**Explanation:** Processes multiple sequence files.

### Generate statistics
**Args:** `mlrho -i sequences.fasta -o estimates.txt -s stats.txt`
**Explanation:** Generates estimation statistics.