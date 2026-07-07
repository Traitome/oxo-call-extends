---
name: gadma
category: utility
description: Genetic Algorithm for Demographic Inference.
tags: [gadma, population genetics, demographic inference, simulation]
author: oxo-call-community
source_url: "https://github.com/ctlab/GADMA"
---

## Concepts
- **Demographic Inference**: Infers demographic history of populations.
- **Genetic Algorithm**: Uses genetic algorithms for optimization.
- **Population Genetics**: Analyzes genetic variation in populations.
- **Model Selection**: Automatically selects best demographic model.
- **Simulation**: Simulates demographic scenarios for comparison.

## Pitfalls
- **Computational Time**: Demanding computations for complex models.
- **Parameter Complexity**: Many parameters to optimize.
- **Model Assumptions**: Results depend on model assumptions.
- **Data Quality**: Requires high-quality genetic data.
- **Convergence**: May require multiple runs for convergence.

## Examples
### Run demographic inference
**Args:** `gadma -i data.sfs -o results/`
**Explanation:** Infers demographic history from SFS data.

### With custom model
**Args:** `gadma -i data.sfs -m model.py -o results/`
**Explanation:** Uses custom demographic model.

### Set population structure
**Args:** `gadma -i data.sfs -p 2 -o results/`
**Explanation:** Assumes 2 populations in the model.

### Generate report
**Args:** `gadma -i data.sfs --report -o results/`
**Explanation:** Generates detailed analysis report.

### Validate model
**Args:** `gadma -i data.sfs --validate -o results/`
**Explanation:** Validates the inferred demographic model.