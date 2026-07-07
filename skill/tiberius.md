---
name: tiberius
category: utility
description: Tiberius - Haplotype-based genetic analysis toolkit.
tags: [tiberius, haplotype, genetic-analysis, phasing, snp, population]
author: oxo-call-community
source_url: "https://github.com/secureamber/tiberius"
---

## Concepts

- **Tool Overview**: Tiberius - A toolkit for haplotype-based genetic analysis including phasing, imputation, and haplotype clustering.
- **Core Function**: Performs haplotype phasing, haplotype-aware association testing, and genetic analysis.
- **Input**: Genotype data (VCF, PED), phenotype information.
- **Output**: Phased haplotypes, association results, haplotype clusters.
- **Installation**: `pip install tiberius` or `conda install -c bioconda tiberius`
- **Use Case**: Population genetics, haplotype analysis, genetic association studies.

## Pitfalls

- **Phase Quality**: Phasing accuracy depends on sample size and linkage disequilibrium patterns.
- **Computation**: Haplotype analysis can be computationally intensive for large datasets.

## Examples

### Phase haplotypes
**Args:** `tiberius phase -i genotypes.vcf -o phased_haplotypes/`
**Explanation:** Phase genotypes into haplotypes.

### Association testing
**Args:** `tiberius assoc -h haplotypes -p phenotype.txt -o results/`
**Explanation:** Perform haplotype-based association testing.
