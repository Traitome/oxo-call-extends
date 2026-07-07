---
name: snmf
category: population-genomics
description: sNMF - Fast program for estimating individual admixture coefficients using sparse NMF
tags: [snmf, population-genomics, admixture, genetics, ancestry]
author: oxo-call-community
source_url: "http://membres-timc.imag.fr/Olivier.Francois/snmf/index.htm"
---

## Concepts

- **Tool Overview**: snmf (v1.2) - Estimates individual admixture coefficients using sparse NMF
- **Core Function**: Performs population structure analysis and admixture estimation
- **Input/Output**: Accepts genotype data; outputs admixture coefficients
- **Algorithm**: Uses sparse non-negative matrix factorization for ancestry inference
- **Installation**: `conda install -c bioconda snmf`
- **Key Features**: Fast computation, sparse NMF, population genetics

## Pitfalls

- **Input Format**: Requires specific genotype format (LFMM or VCF)
- **K Value Selection**: Choosing optimal number of populations (K) is critical
- **Computational Resources**: Large datasets require significant memory
- **Convergence**: May require multiple runs to check convergence
- **Missing Data**: Missing genotypes can affect results
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `snmf --help`
**Explanation:** Shows available options and usage information.

### Basic admixture analysis
**Args:** `snmf input.geno -K 3 -o results/`
**Explanation:** Run admixture analysis with K=3 populations.

### With cross-entropy
**Args:** `snmf input.geno -K 2:6 -c -o results/`
**Explanation:** Run with K from 2 to 6 with cross-entropy evaluation.

### With repetitions
**Args:** `snmf input.geno -K 4 -r 10 -o results/`
**Explanation:** Run 10 repetitions for stability.

### With percentage
**Args:** `snmf input.geno -K 3 -p 10 -o results/`
**Explanation:** Use 10% of data for cross-validation.

### Project individuals
**Args:** `snmf input.geno -K 3 -o results/ --project`
**Explanation:** Project individuals onto ancestral populations.

### With tolerance
**Args:** `snmf input.geno -K 3 -e 1e-5 -o results/`
**Explanation:** Set convergence tolerance threshold.

### Output format
**Args:** `snmf input.geno -K 3 -o results/ --output-format Q`
**Explanation:** Specify output format for admixture coefficients.