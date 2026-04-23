---
name: beast
category: utility
description: BEAST - Bayesian Evolutionary Analysis Sampling Trees for molecular sequences
tags: [phylogenetics, bayesian, mcmc, molecular-evolution, divergence-dating]
author: oxo-call-community
source_url: "https://beast.community"
---

## Concepts

- **Tool Overview**: BEAST (Bayesian Evolutionary Analysis Sampling Trees) performs Bayesian analysis of molecular sequences using MCMC, estimating phylogenies, divergence times, and evolutionary parameters.

- **Bayesian Framework**: Uses Bayesian inference to estimate posterior distributions of trees and parameters.

- **MCMC Sampling**: Employs Markov Chain Monte Carlo to sample from posterior distributions.

- **Divergence Dating**: Estimates divergence times using molecular clock models and calibrations.

- **Demographic Models**: Supports various demographic models (coalescent, birth-death, etc.).

- **Model Selection**: Provides tools for model selection and comparison.

## Pitfalls

- **Convergence**: MCMC must converge. Run sufficient iterations and check ESS values.

- **Prior Sensitivity**: Results sensitive to prior choices. Test sensitivity and justify priors.

- **Computational Cost**: MCMC is computationally expensive. Long runs may be needed.

- **Model Specification**: XML configuration is complex. Use BEAUti GUI for setup.

## Examples

### Basic BEAST run
**Args:** `beast input.xml`
**Explanation:** Runs BEAST analysis from XML configuration file.

### Specify number of threads
**Args:** `beast -threads 8 input.xml`
**Explanation:** Uses 8 threads for parallel likelihood calculation.

### Resume from checkpoint
**Args:** `beast -resume checkpoint.file`
**Explanation:** Resumes analysis from saved checkpoint.

### Specify output directory
**Args:** `beast -output_dir results/ input.xml`
**Explanation:** Saves output files to specified directory.

### Overwrite existing files
**Args:** `beast -overwrite input.xml`
**Explanation:** Overwrites existing output files without prompting.

### Set random seed
**Args:** `beast -seed 12345 input.xml`
**Explanation:** Sets random seed for reproducible results.

### Beagle library acceleration
**Args:** `beast -beagle input.xml`
**Explanation:** Uses Beagle library for faster likelihood calculation.
