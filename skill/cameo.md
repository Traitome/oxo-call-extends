---
name: cameo
category: utility
description: Computer aided metabolic engineering and optimization
tags: [cameo, metabolic, engineering, optimization, flux-balance]
author: oxo-call-community
source_url: "http://cameo.bio"
---

## Concepts

- **Tool Overview**: CAMEO is a Python library for metabolic engineering and optimization.
- **Core Function**: Predicts gene knockout strategies and designs metabolic pathways.
- **Algorithm**: Uses flux balance analysis (FBA) and strain design algorithms.
- **Input**: Genome-scale metabolic models in SBML format.
- **Output**: Strain design strategies and flux predictions.
- **Application**: Metabolic engineering and synthetic biology.
- **Installation**: Install via bioconda: `conda install -c bioconda cameo`

## Pitfalls

- **Python Only**: Python library, not a command-line tool.
- **Model Required**: Requires genome-scale metabolic model.
- **Solver Dependency**: Needs optimization solver (CPLEX, Gurobi, or GLPK).

## Examples

### Load metabolic model
**Args:** `python -c "from cameo import load_model; model = load_model('iJO1366.xml'); print(model.objective)"`
**Explanation:** Loads E. coli metabolic model and prints objective function.

### Predict gene knockouts
**Args:** `python -c "from cameo import strain_design; model = load_model('iJO1366.xml'); result = strain_design.opt_gene_knockout(model)"`
**Explanation:** Predicts optimal gene knockout strategy for production.

### Simulate growth
**Args:** `python -c "from cameo import load_model; model = load_model('iJO1366.xml'); solution = model.solve(); print(solution.fluxes)"`
**Explanation:** Simulates growth and computes flux distribution.
