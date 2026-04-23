---
name: baypass
category: population-genomics
description: BayPass - Genome-wide scan for adaptive differentiation and association analysis
tags: [adaptive-differentiation, association-analysis, population-genomics, bayesian]
author: oxo-call-community
source_url: "https://forge.inrae.fr/mathieu.gautier/baypass_public"
---

## Concepts

- **Tool Overview**: BayPass performs genome-wide scans for adaptive differentiation and association analysis with population-specific covariables using Bayesian methods.

- **Adaptive Differentiation**: Identifies loci under selection by distinguishing adaptive from neutral differentiation.

- **Association Analysis**: Tests associations between allele frequencies and environmental covariables.

- **Population Structure**: Accounts for population structure in statistical models, reducing false positives.

- **Covariable Analysis**: Supports continuous and categorical covariables for environmental association.

## Pitfalls

- **Convergence**: MCMC chains must converge. Run sufficient iterations and check diagnostics.

- **Prior Specification**: Results sensitive to prior choices. Test sensitivity to priors.

- **Population Number**: Requires sufficient populations for reliable estimation (≥4 recommended).

- **Missing Data**: High missing data rates can affect results. Filter appropriately.

## Examples

### Basic differentiation scan
**Args:** `baypass -gfile genotype_matrix.txt -outprefix results -nval 25000 -npilot 5000`
**Explanation:** Scans for adaptive differentiation with 25000 MCMC iterations.

### Association with covariables
**Args:** `baypass -gfile genotype_matrix.txt -efile covariables.txt -outprefix results -nval 25000`
**Explanation:** Tests associations between allele frequencies and environmental covariables.

### Core model only
**Args:** `baypass -gfile genotype_matrix.txt -outprefix results -coremodel -nval 25000`
**Explanation:** Runs only the core model without association testing.

### Specify number of threads
**Args:** `baypass -gfile genotype_matrix.txt -outprefix results -nval 25000 -threads 8`
**Explanation:** Uses 8 threads for parallel computation.

### Custom prior parameters
**Args:** `baypass -gfile genotype_matrix.txt -outprefix results -nval 25000 -betaprior pi_beta=0.5 mu_beta=0 sigma_beta=1.5`
**Explanation:** Uses custom prior parameters for beta distribution.
