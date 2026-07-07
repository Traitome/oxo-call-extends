---
name: deploid
category: variant-calling
description: DEploid - deconvolution of mixed genomes with unknown proportions.
tags: [deploid, variant-calling, deconvolution, mixed-infection, malaria]
author: oxo-call-community
source_url: "http://deploid.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: deploid (v0.5+) is a tool for deconvoluting mixed genome samples with unknown proportions, commonly used for analyzing malaria parasite infections with multiple strains.
- **Core Function**: Infers individual strain haplotypes and their relative proportions from mixed sequencing data using Bayesian statistical modeling.
- **Input/Output**: Input: VCF files with SNP calls, reference genome. Output: Strain haplotypes, relative proportions, confidence estimates.
- **Algorithm**: Uses Bayesian hierarchical modeling to simultaneously infer haplotypes and their frequencies from mixed population data.
- **Key Features**: Mixed infection analysis, strain deconvolution, unknown proportion estimation, Bayesian framework, malaria-focused.
- **Installation**: `conda install -c bioconda deploid`

## Pitfalls

- **Input Requirements**: Requires VCF with sufficient SNP coverage across strains.
- **Strain Complexity**: Performance may degrade with very high strain diversity.
- **Reference Genome**: Must use appropriate reference for the organism.
- **Computational Resources**: May require significant computational time for complex samples.
- **Prior Knowledge**: Benefits from prior information about expected strain diversity.

## Examples

### Deconvolute mixed genome sample
**Args:** `deploid --vcf sample.vcf --ref ref.fa --output results/`
**Explanation:** Deconvolutes mixed genome sample into component strains.

### With strain number constraint
**Args:** `deploid --vcf sample.vcf --ref ref.fa --output results/ --strains 3`
**Explanation:** Specify expected number of strains (e.g., 3).

### With prior proportion information
**Args:** `deploid --vcf sample.vcf --ref ref.fa --output results/ --prior prior.txt`
**Explanation:** Provide prior information about strain proportions.