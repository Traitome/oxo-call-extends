---
name: hapbin
category: bioinformatics
description: hapbin calculates Extended Haplotype Homozygosity (EHH), Integrated Haplotype Score (iHS), and Cross Population EHH (XP-EHH) statistics for detecting selection signatures.
tags: [hapbin, population-genomics, selection-signatures, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/evotools/hapbin"
---

## Concepts

- **Haplotype Statistics**: hapbin calculates EHH, iHS, and XP-EHH statistics.

- **Selection Detection**: Identifies signatures of natural selection in populations.

- **Extended Haplotype Homozygosity**: Measures haplotype homozygosity across extended regions.

- **Population Genetics**: Analyzes genetic variation across populations.

- **Linkage Disequilibrium**: Studies non-random association of alleles.

- **Genome-Wide Analysis**: Performs genome-wide scans for selection.

## Pitfalls

- **Population Structure**: Account for population structure in analysis.

- **Sample Size**: Results may vary with sample size.

- **Marker Density**: Requires sufficient marker density.

- **Missing Data**: Handle missing genotypes appropriately.

- **Multiple Testing**: Correct for multiple hypothesis testing.

## Examples

### Calculate EHH
**Args:** `hapbin --ehh -i input.bed -o ehh_results.txt`
**Explanation:** Calculates Extended Haplotype Homozygosity.

### Calculate iHS
**Args:** `hapbin --ihs -i input.bed -o ihs_results.txt`
**Explanation:** Calculates Integrated Haplotype Score.

### Calculate XP-EHH
**Args:** `hapbin --xpehh -i1 pop1.bed -i2 pop2.bed -o xpehh_results.txt`
**Explanation:** Calculates Cross Population EHH between two populations.

### With genetic map
**Args:** `hapbin --ihs -i input.bed -g genetic_map.txt -o ihs_results.txt`
**Explanation:** Uses genetic map for improved calculations.

### Batch processing
**Args:** `for chr in {1..22}; do hapbin --ihs -i chr${chr}.bed -o chr${chr}_ihs.txt; done`
**Explanation:** Processes multiple chromosome files.

### Generate statistics
**Args:** `hapbin --stats -i input.bed -o stats.txt`
**Explanation:** Generates summary statistics.

### Help command
**Args:** `hapbin --help`
**Explanation:** Shows available options and usage information.