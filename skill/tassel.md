---
name: tassel
category: population-genomics
description: Evaluates trait associations, evolutionary patterns, and linkage disequilibrium.
tags: [tassel, gwas, population-genomics, ld, plant-breeding]
author: oxo-call-community
source_url: "https://www.maizegenetics.net/tassel"
---

## Concepts

- **Tool Overview**: tassel (v5.2.89) is a comprehensive genetics analysis package.
- **Core Function**: GWAS, evolutionary analysis, and linkage disequilibrium.
- **Algorithm**: Statistical methods for genetic association studies.
- **Input/Output**: Input: Genotype data (VCF/HapMap); Output: Association results.
- **Applications**: Plant genetics, breeding, evolutionary biology.
- **Installation**: Download from website or conda install.

## Pitfalls

- **Memory Usage**: Large datasets require significant memory.
- **Genotype Quality**: Poor quality genotypes affect results.
- **Population Structure**: Requires correction for population structure.
- **Multiple Testing**: Requires correction for multiple comparisons.
- **LD Decay**: Long-range LD may affect mapping resolution.
- **Computational Time**: Large datasets process slowly.

## Examples

### Display help
**Args:** `run_tassel --help`
**Explanation:** Shows available options and usage information.

### Basic GWAS
**Args:** `run_tassel -plink -input genotypes.hmp.txt -tphenotype traits.txt -out results/`
**Explanation:** Perform genome-wide association study.

### Calculate LD
**Args:** `run_tassel -ld -input genotypes.vcf -output results/ld.txt`
**Explanation:** Calculate linkage disequilibrium.

### Diversity analysis
**Args:** `run_tassel -diversity -input genotypes.vcf -output results/div.txt`
**Explanation:** Analyze genetic diversity.

###kinship calculation
**Args:** `run_tassel -kinship -input genotypes.vcf -output results/kindist.txt`
**Explanation:** Calculate kinship matrix.

### PCA analysis
**Args:** `run_tassel -PCA -input genotypes.vcf -output results/pca.txt`
**Explanation:** Perform principal component analysis.

### Generate haplotype network
**Args:** `run_tassel -haplotypeNetwork -input genotypes.vcf -output results/network.txt`
**Explanation:** Generate haplotype network.

### Filter genotypes
**Args:** `run_tassel -filterGenotypes -input genotypes.vcf -output filtered.vcf -minFreq 0.05`
**Explanation:** Filter rare variants.
