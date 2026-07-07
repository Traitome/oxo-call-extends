---
name: ima3
category: population-genomics
description: IMa3 can be used to solve a fundamental problem in evolutionary genetics, which is to jointly consider phylogenetic history and population genetic history, including gene exchange.
tags: [ima3, population-genomics, isolation-migration, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/jodyhey/IMa3"
---

## Concepts

- **Tool Overview**: ima3 (v1.13) - A program for inferring population divergence times and migration rates under the Isolation-with-Migration (IM) model
- **Core Function**: Uses Markov Chain Monte Carlo (MCMC) to estimate demographic parameters including population sizes, divergence times, and migration rates
- **Input/Output**: Accepts multi-locus sequence data, outputs parameter estimates and posterior distributions
- **Installation**: `conda install -c bioconda ima3` or compile from source
- **Key Features**: Supports multiple populations, handles gene flow, estimates rooted phylogenetic trees

## Pitfalls

- **Computational Intensity**: MCMC runs can be computationally demanding for complex models
- **Input Format**: Strict input file format requirements; incorrect formatting causes errors
- **Burn-in Period**: Requires sufficient burn-in for convergence
- **Parameter Priors**: Prior specification significantly affects results
- **Model Complexity**: Overly complex models may lead to convergence issues

## Examples

### Run basic IMa3 analysis
**Args:** `ima3 -i input.u -o output.out -b 100000 -L 5000 -d 200`
**Explanation:** Runs MCMC with 100,000 burn-in steps and 5,000 sampling steps.

### Specify prior parameters
**Args:** `ima3 -i input.u -o output.out -q 10 -m 1 -t 1.5`
**Explanation:** Sets priors for population size (q=10), migration rate (m=1), and splitting time (t=1.5).

### Use Metropolis coupling
**Args:** `ima3 -i input.u -o output.out -hn 24 -ha 0.97`
**Explanation:** Enables Metropolis coupling with 24 chains and heating factor 0.97.

### Resume from previous run
**Args:** `ima3 -i input.u -o output.out -f previous_run.out.mcf`
**Explanation:** Resumes MCMC from a previously saved Markov chain file.

### Specify mutation model
**Args:** `ima3 -i input.u -o output.out -c 1`
**Explanation:** Sets mutation model (1=HKY, 2=IS, etc.).

### Run with MPI parallelization
**Args:** `mpirun -np 4 ima3 -i input.u -o output.out -b 100000 -L 5000`
**Explanation:** Runs IMa3 in parallel using MPI with 4 processors.