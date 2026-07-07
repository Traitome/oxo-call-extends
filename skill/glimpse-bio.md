---
name: glimpse-bio
category: phasing-imputation
description: GLIMPSE - Phasing and imputation method for large-scale low-coverage sequencing studies.
tags: [glimpse-bio, phasing-imputation, GWAS, low-coverage]
author: oxo-call-community
source_url: "https://odelaneau.github.io/GLIMPSE/"
---

## Concepts
- **Phasing**: Phases haplotypes from low-coverage data.
- **Imputation**: Imputes missing genotypes.
- **Low-Coverage**: Works with low-coverage sequencing.
- **Population Studies**: Designed for population studies.
- **Efficient Algorithm**: Efficient for large datasets.

## Pitfalls
- **Reference Panel**: Requires good reference panel.
- **Sample Size**: Larger samples improve accuracy.
- **Coverage**: Very low coverage may affect accuracy.
- **Computational Resources**: Requires resources for large datasets.
- **Result Validation**: Results should be validated.

## Examples
### Phase data
**Args:** `GLIMPSE_phase --input input.bcf --reference reference.vcf.gz --output phased.vcf`
**Explanation:** Phases input data.

### Impute chunks
**Args:** `GLIMPSE_chunk --input input.vcf --reference reference.vcf.gz --output chunk.vcf`
**Explanation:** Imputes genomic chunks.

### Ligate chunks
**Args:** `GLIMPSE_ligate --input chunks/ --output phased.vcf`
**Explanation:** Combines imputed chunks.

### Generate report
**Args:** `GLIMPSE_phase --input input.bcf --reference reference.vcf.gz --report -o phased.vcf`
**Explanation:** Generates phasing report.

### Batch processing
**Args:** `GLIMPSE_phase --input samples.txt --reference reference.vcf.gz --output ./phased/`
**Explanation:** Processes multiple samples.