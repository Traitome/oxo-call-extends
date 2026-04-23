---
name: beast2
category: utility
description: BEAST 2 - Bayesian phylogenetic analysis of molecular sequences with modular architecture
tags: [phylogenetics, bayesian, mcmc, modular, evolutionary-analysis]
author: oxo-call-community
source_url: "http://www.beast2.org"
---

## Concepts

- **Tool Overview**: BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis, featuring a modular architecture that allows extension through packages.

- **Modular Design**: Extensible through packages, enabling custom models and analyses.

- **MCMC Framework**: Uses MCMC to estimate posterior distributions of trees and parameters.

- **Divergence Dating**: Estimates divergence times with various clock models and calibrations.

- **Package Manager**: Includes package manager for installing extensions and additional models.

- **BEAUti Interface**: Provides graphical interface (BEAUti) for creating XML configuration files.

## Pitfalls

- **Package Dependencies**: Some analyses require additional packages. Install via package manager.

- **Convergence Assessment**: Must assess MCMC convergence using Tracer or similar tools.

- **Memory Usage**: Large datasets require sufficient heap memory. Adjust Java settings.

- **Version Compatibility**: Packages may require specific BEAST 2 versions. Check compatibility.

## Examples

### Basic BEAST 2 run
**Args:** `beast input.xml`
**Explanation:** Runs BEAST 2 analysis from XML configuration file.

### Install package
**Args:** `packagemanager -add BEASTLab`
**Explanation:** Installs BEASTLab package for additional functionality.

### List installed packages
**Args:** `packagemanager -list`
**Explanation:** Lists all installed BEAST 2 packages.

### Specify threads
**Args:** `beast -threads 8 input.xml`
**Explanation:** Uses 8 threads for parallel computation.

### Use Beagle library
**Args:** `beast -beagle_SSE input.xml`
**Explanation:** Uses Beagle library with SSE optimization for faster computation.

### Resume analysis
**Args:** `beast -resume state.file`
**Explanation:** Resumes analysis from saved state file.

### Set Java heap size
**Args:** `java -Xmx8g -jar beast.jar input.xml`
**Explanation:** Allocates 8GB memory for BEAST 2 analysis.
