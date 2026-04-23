---
name: bayestyper
category: variant-calling
description: BayesTyper - Variant graph genotyping based on exact k-mer alignment
tags: [genotyping, variant-graph, k-mer, structural-variants]
author: oxo-call-community
source_url: "https://github.com/bioinformatics-centre/BayesTyper"
---

## Concepts

- **Tool Overview**: BayesTyper genotypes variants using k-mer based alignment to a variant graph, enabling accurate genotyping of complex variants including structural variants.

- **K-Mer Based**: Uses exact k-mer matching for robust genotyping, avoiding alignment biases.

- **Variant Graph**: Represents variants as a graph structure, capturing complex variation.

- **Structural Variants**: Particularly effective for genotyping structural variants and complex regions.

- **Joint Calling**: Supports joint genotyping across multiple samples.

## Pitfalls

- **K-Mer Database**: Requires k-mer counting step which can be memory-intensive.

- **Reference Bias**: Less susceptible to reference bias than alignment-based methods, but still present.

- **Novel Variants**: Cannot genotype variants not in input VCF. Input variant set must be comprehensive.

- **K-Mer Size**: K-mer size affects sensitivity and specificity. Adjust for application.

## Examples

### Basic genotyping
**Args:** `bayesTyper kmc -i reads.fastq.gz -o kmc_db && bayesTyper genotype -v variants.vcf -k kmc_db -o genotypes.vcf`
**Explanation:** Counts k-mers from reads, then genotypes variants using k-mer counts.

### Joint genotyping
**Args:** `bayesTyper genotype -v variants.vcf -k sample1_kmc.db -k sample2_kmc.db -o joint_genotypes.vcf`
**Explanation:** Jointly genotypes multiple samples for improved accuracy.

### Specify k-mer size
**Args:** `bayesTyper kmc -i reads.fastq.gz -k 31 -o kmc_db`
**Explanation:** Uses 31-mers instead of default size for k-mer counting.

### Filter output
**Args:** `bayesTyper genotype -v variants.vcf -k kmc_db -o genotypes.vcf --min-qual 20`
**Explanation:** Filters output to include only genotypes with quality ≥20.
