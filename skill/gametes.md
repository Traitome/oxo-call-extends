---
name: gametes
category: variant-calling
description: Tool for the generation of complex single SNP models.
tags: [gametes, SNP, genetic model, simulation]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/gametes/"
---

## Concepts
- **SNP Modeling**: Generates complex single SNP models.
- **Genetic Simulation**: Simulates genetic data.
- **Case-Control Studies**: Designs case-control study parameters.
- **Power Analysis**: Performs power calculations.
- **Sample Size**: Calculates required sample sizes.

## Pitfalls
- **Model Complexity**: Complex models require careful setup.
- **Statistical Expertise**: Requires understanding of statistical genetics.
- **Simulation Time**: Complex simulations can be time-consuming.
- **Convergence Issues**: May have convergence problems.
- **Parameter Selection**: Requires careful parameter tuning.

## Examples
### Generate SNP model
**Args:** `gametes -m model.txt -o simulated.csv`
**Explanation:** Generates SNP data from model.

### With case-control design
**Args:** `gametes -m model.txt --cases 1000 --controls 1000 -o simulated.csv`
**Explanation:** Simulates case-control study.

### Power calculation
**Args:** `gametes -m model.txt --power -o power.txt`
**Explanation:** Calculates statistical power.

### Sample size calculation
**Args:** `gametes -m model.txt --sample-size -o samples.txt`
**Explanation:** Calculates required sample size.

### Multiple markers
**Args:** `gametes -m model.txt --markers 10 -o simulated.csv`
**Explanation:** Simulates data with 10 markers.