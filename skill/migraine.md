---
name: migraine
category: expression
description: Implements coalescent algorithms for maximum likelihood analysis of population genetic data.
tags: [migraine, expression, population-genetics]
author: oxo-call-community
source_url: "http://kimura.univ-montp2.fr/~rousset/Migraine.htm"
---

## Concepts

- **Tool Overview**: Migraine v0.6.0 implements coalescent algorithms for population genetic analysis.
- **Core Function**: Performs maximum likelihood analysis of population genetic data.
- **Coalescent Theory**: Uses coalescent algorithms for population genetics inference.
- **Allelic Counts**: Handles allelic count data for population analysis.
- **Input/Output**: Accepts population genetic data; outputs demographic inferences.
- **Population Genetics**: Supports population genetic parameter estimation.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal inference.
- **Data Quality**: Inference accuracy depends on input data quality.
- **Runtime**: Analysis can be time-consuming for complex models.
- **Model Assumptions**: Based on specific coalescent model assumptions.

## Examples

### Run population genetic analysis
**Args:** `migraine -i data.txt -o results.txt`
**Explanation:** Performs maximum likelihood analysis on population data.

### With custom model
**Args:** `migraine -i data.txt -o results.txt -m 2`
**Explanation:** Uses model 2 for analysis.

### Detailed output
**Args:** `migraine -i data.txt -o results.txt -v`
**Explanation:** Generates detailed analysis report.

### Batch processing
**Args:** `migraine -i data/ -o results/`
**Explanation:** Processes multiple datasets in batch mode.

### Generate confidence intervals
**Args:** `migraine -i data.txt -o results.txt -c`
**Explanation:** Computes confidence intervals for parameters.