---
name: mrpast
category: utility
description: Demographic inference from Ancestral Recombination Graphs.
tags: [mrpast, utility, population-genetics]
author: oxo-call-community
source_url: "https://aprilweilab.github.io/"
---

## Concepts

- **Tool Overview**: mrpast v0.2 performs demographic inference from ARGs.
- **Core Function**: Reconstructs population demographic history.
- **ARG Analysis**: Analyzes Ancestral Recombination Graphs.
- **Demographic Inference**: Infers population size changes over time.
- **Coalescent Theory**: Based on coalescent simulation methods.
- **Input/Output**: Accepts ARG files; outputs demographic models.

## Pitfalls

- **ARG Dependence**: Requires input Ancestral Recombination Graphs.
- **Memory Requirements**: Memory usage depends on ARG complexity.
- **Parameter Tuning**: May require parameter adjustment for inference.
- **Data Quality**: Results depend on ARG quality.
- **Computational Resources**: Complex ARGs may require significant resources.
- **Model Selection**: Choosing appropriate demographic model is critical.

## Examples

### Infer demography from ARG
**Args:** `mrpast -i arg.graph -o demographic_model.txt`
**Explanation:** Performs demographic inference from ARG.

### With multiple ARGs
**Args:** `mrpast -i args/ -o demographic_model.txt`
**Explanation:** Uses multiple ARG files for inference.

### Specify model type
**Args:** `mrpast -i arg.graph -m bottleneck -o model.txt`
**Explanation:** Tests bottleneck demographic model.

### Generate plot
**Args:** `mrpast -i arg.graph -p plot.png -o model.txt`
**Explanation:** Generates demographic history plot.

### Bootstrap analysis
**Args:** `mrpast -i arg.graph -b 100 -o model.txt`
**Explanation:** Performs 100 bootstrap replicates.