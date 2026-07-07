---
name: minimac4
category: variant-calling
description: Computationally efficient genotype imputation
tags: [minimac4, variant-calling, imputation]
author: oxo-call-community
source_url: "https://github.com/statgen/Minimac4"
---

## Concepts

- **Tool Overview**: Minimac4 v4.1.6 performs computationally efficient genotype imputation.
- **Core Function**: Imputes missing genotypes from reference panels.
- **Genotype Imputation**: Fills in missing genetic variants using reference data.
- **Memory Efficient**: Optimized for lower memory usage compared to previous versions.
- **Input/Output**: Accepts VCF files; outputs imputed genotypes.
- **Phasing Support**: Supports pre-phased and unphased input data.

## Pitfalls

- **Reference Panel**: Requires appropriate reference panel for imputation.
- **Computational Resources**: Large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on reference panel size.
- **Parameter Tuning**: May require parameter adjustment for optimal imputation.
- **Data Quality**: Imputation accuracy depends on input data quality.
- **Population Matching**: Reference panel should match study population.

## Examples

### Run genotype imputation
**Args:** `minimac4 --refHaps reference.haps --refLegend reference.legend --haps input.haps --legend input.legend --prefix output`
**Explanation:** Imputes missing genotypes using reference panel.

### With VCF input
**Args:** `minimac4 --refHaps reference.haps --vcf input.vcf --prefix output`
**Explanation:** Imputes from VCF format input.

### Pre-phased data
**Args:** `minimac4 --refHaps reference.haps --haps input.haps --legend input.legend --prefix output --prePhased`
**Explanation:** Processes pre-phased input data.

### Batch processing
**Args:** `minimac4 --refHaps reference.haps --vcf vcf/ --prefix outputs/`
**Explanation:** Processes multiple VCF files.

### Generate statistics
**Args:** `minimac4 --refHaps reference.haps --haps input.haps --legend input.legend --prefix output --stats`
**Explanation:** Generates imputation quality statistics.