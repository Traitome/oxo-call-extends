---
name: structure
category: population-genetics
description: STRUCTURE uses multi-locus genotype data to investigate population structure, infer distinct populations, assign individuals to populations, study hybrid zones, identify migrants and admixed individuals.
tags: [structure, population-genetics, admixture, snps]
author: oxo-call-community
source_url: "https://web.stanford.edu/group/pritchardlab/structure.html"
---

## Concepts

- **Tool Overview**: structure (v2.3.4) is a software package for investigating population structure using multi-locus genotype data.
- **Core Function**: Infers population structure, assigns individuals to populations, and estimates admixture proportions.
- **Algorithm**: Uses Bayesian clustering to identify genetically distinct populations.
- **Input/Output**: Input: Genotype data file; Output: Population assignment probabilities.
- **Applications**: Population genetics, evolutionary biology, conservation genetics.
- **Installation**: `conda install -c bioconda structure` or download from website.

## Pitfalls

- **Computational Time**: Analysis can be computationally intensive.
- **Memory Requirements**: Large datasets require significant memory.
- **Parameter Tuning**: Incorrect parameters affect clustering results.
- **K Selection**: Choosing the correct number of populations is challenging.
- **Convergence**: MCMC chains may not converge properly.
- **Data Quality**: Poor quality genotype data affects results.

## Examples

### Display help
**Args:** `structure --help`
**Explanation:** Shows available options and usage information.

### Basic population structure analysis
**Args:** `structure -i genotypes.str -o results/ -K 3`
**Explanation:** Run STRUCTURE with K=3 populations.

### With admixture model
**Args:** `structure -i genotypes.str -o results/ -K 5 -m admixture`
**Explanation:** Use admixture model for population assignment.

### Verbose mode
**Args:** `structure -i genotypes.str -o results/ -K 3 -v`
**Explanation:** Run with detailed logging for debugging.

### Run multiple replicates
**Args:** `structure -i genotypes.str -o results/ -K 3 -R 10`
**Explanation:** Run 10 replicates for robustness.

### Batch processing
**Args:** `structure -i genotypes.str -o results/ -K 2-10`
**Explanation:** Run analysis for K values from 2 to 10.

### Filter by quality
**Args:** `structure -i genotypes.str -o results/ -K 3 -q 0.9`
**Explanation:** Use minimum confidence threshold of 0.9.

### Include population labels
**Args:** `structure -i genotypes.str -o results/ -K 3 -l populations.txt`
**Explanation:** Use predefined population labels.

### Generate report
**Args:** `structure -i genotypes.str -o results/ -K 3 --report`
**Explanation:** Generate comprehensive HTML report.
