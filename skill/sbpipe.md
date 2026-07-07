---
name: sbpipe
category: workflow-management
description: SBpipe - pipelines for systems modelling of biological networks
tags: ["sbpipe", "workflow-management", "systems-biology", "COPASI"]
author: oxo-call-community
source_url: "http://sbpipe.readthedocs.io"
---

## Concepts

- **Tool Overview**: SBpipe (v4.21.0) is a collection of pipelines for systems modelling of biological networks, enabling automated model simulation and parameter estimation.
- **Core Function**: Automates repetitive tasks of model simulation, parameter estimation, and robustness analysis for mathematical models.
- **Model Support**: Runs models implemented in COPASI, Python, or any programming language via Python wrapper.
- **Execution Backends**: Supports multicore computers, SGE, LSF clusters, and Snakemake for parallel execution.
- **Input/Output**: Accepts model files and parameter configurations, produces simulation results and analysis reports.
- **Applications**: Systems biology model development, parameter optimization, and robustness analysis.

## Pitfalls

- **Model Dependencies**: Requires COPASI or Python environment for model execution.
- **Complex Setup**: May require significant configuration for cluster execution.
- **Computational Resources**: Parameter estimation can be computationally intensive.
- **Learning Curve**: Steep learning curve for pipeline configuration.
- **Documentation**: Limited examples for advanced use cases.
- **Version Compatibility**: May have compatibility issues with different COPASI versions.

## Examples

### Run basic simulation
**Args:** `sbpipe run -m model.copasi -o results/`
**Explanation:** Runs COPASI model simulation and outputs results.

### Parameter estimation
**Args:** `sbpipe estimate -m model.copasi -d data.csv -o estimates/`
**Explanation:** Performs parameter estimation using experimental data.

### Sensitivity analysis
**Args:** `sbpipe sensitivity -m model.copasi -o sensitivity/`
**Explanation:** Runs sensitivity analysis on model parameters.

### Robustness analysis
**Args:** `sbpipe robustness -m model.copasi -n 1000 -o robustness/`
**Explanation:** `-n 1000` runs 1000 simulations for robustness analysis.

### Parallel execution
**Args:** `sbpipe run -m model.copasi -p 8 -o results/`
**Explanation:** `-p 8` uses 8 parallel processes for simulation.

### Cluster submission
**Args:** `sbpipe submit -m model.copasi -c sge -o results/`
**Explanation:** `-c sge` submits job to SGE cluster.

### Pipeline configuration
**Args:** `sbpipe configure -i config.yaml -m model.copasi -o results/`
**Explanation:** Uses custom configuration file for pipeline settings.