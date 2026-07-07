---
name: fastlmm
category: population-genomics
description: "Fast GWAS"
tags: [fastlmm, population-genomics, GWAS, genetics, bioinformatics]
author: oxo-call-community
source_url: "http://research.microsoft.com/en-us/um/redmond/projects/mscompbio/fastlmm/"
---

## Concepts

- **Tool Overview**: FastLMM is a fast and efficient tool for performing Genome-Wide Association Studies (GWAS) using linear mixed models.
- **Core Function**: Identifies genetic variants associated with phenotypes using linear mixed model approaches.
- **Input/Output**: Input: Genotype data (PLINK/VCF), phenotype data. Output: Association results, p-values.
- **Algorithm**: Uses linear mixed models with variance component estimation for GWAS.
- **Key Features**: Fast GWAS analysis, linear mixed models, population structure correction, multiple phenotypes, efficient computation.
- **Installation**: `conda install -c bioconda fastlmm`

## Pitfalls

- **Data Quality**: Requires high-quality genotype and phenotype data.
- **Population Structure**: May require careful handling of population structure.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic GWAS
**Args:** `fastlmm -i genotypes.vcf -p phenotypes.txt -o gwas_results.txt`
**Explanation:** Performs GWAS analysis.

### With covariates
**Args:** `fastlmm -i genotypes.vcf -p phenotypes.txt -c covariates.txt -o gwas_results.txt`
**Explanation:** Includes covariates in analysis.

### PLINK format
**Args:** `fastlmm -i genotypes.bed -b -p phenotypes.txt -o gwas_results.txt`
**Explanation:** Processes PLINK formatted data.

### Multiple phenotypes
**Args:** `fastlmm -i genotypes.vcf -p phenotypes.txt -m -o gwas_results.txt`
**Explanation:** Analyzes multiple phenotypes.

### Output Manhattan plot
**Args:** `fastlmm -i genotypes.vcf -p phenotypes.txt -o gwas_results.txt --plot manhattan.png`
**Explanation:** Generates Manhattan plot.