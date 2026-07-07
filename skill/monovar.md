---
name: monovar
category: variant-calling
description: single cell joint genotyper
tags: [monovar, variant-calling, single-cell]
author: oxo-call-community
source_url: "https://bitbucket.org/hamimzafar/monovar"
---

## Concepts

- **Tool Overview**: Monovar v0.0.1 performs joint genotyping across single cells.
- **Core Function**: Genotypes variants jointly across multiple single cells.
- **Joint Genotyping**: Improves calling accuracy by leveraging information across cells.
- **Single-Cell Data**: Designed for single-cell sequencing experiments.
- **Bayesian Model**: Uses Bayesian inference for variant calling.
- **Input/Output**: Accepts allele counts; outputs joint genotype calls.

## Pitfalls

- **Single-Cell Specific**: Designed for single-cell sequencing data.
- **Memory Requirements**: Memory usage depends on cell count and variant number.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on sequencing depth per cell.
- **Allele Dropout**: May be affected by single-cell allele dropout.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run joint genotyping
**Args:** `monovar -i allele_counts.txt -o genotypes.txt`
**Explanation:** Performs joint genotyping across single cells.

### With prior probabilities
**Args:** `monovar -i allele_counts.txt -p priors.txt -o genotypes.txt`
**Explanation:** Uses custom prior probabilities.

### Verbose output
**Args:** `monovar -i allele_counts.txt -v -o genotypes.txt`
**Explanation:** Shows detailed genotyping results.

### Batch processing
**Args:** `monovar -i data/ -o results/`
**Explanation:** Processes multiple datasets.

### Generate VCF
**Args:** `monovar -i allele_counts.txt -vcf -o variants.vcf`
**Explanation:** Outputs results in VCF format.