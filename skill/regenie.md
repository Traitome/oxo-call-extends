---
name: regenie
category: utility
description: Regenie is a C++ program for whole genome regression modelling of large genome-wide association studies (GWAS).
tags: [regenie, utility, gwas, genome-wide-association]
author: oxo-call-community
source_url: "https://rgcgithub.github.io/regenie/options/"
---

## Concepts

- **Tool Overview**: regenie models GWAS.
- **Core Function**: Genome-wide regression.
- **Algorithm**: Uses regression methods.
- **Input Format**: Accepts genotype data.
- **Output**: Produces association results.
- **Use Case**: GWAS analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Genotype Quality**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `regenie --help`
**Explanation:** Shows available options and usage instructions.

### Run GWAS
**Args:** `regenie --step 1 --bed genotypes.bed --pheno phenotypes.txt --out gwas_results`
**Explanation:** Runs genome-wide association study.

### With parameters
**Args:** `regenie --step 1 --bed genotypes.bed --par params.txt --out gwas_results`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `regenie --verbose --step 1 --bed genotypes.bed --out gwas_results`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `regenie --threads 4 --step 1 --bed genotypes.bed --out gwas_results`
**Explanation:** Uses 4 threads for parallel processing.

### Step 2 analysis
**Args:** `regenie --step 2 --bed genotypes.bed --pheno phenotypes.txt --pred step1_pred.list --out gwas_results`
**Explanation:** Runs step 2 of analysis.

### Generate report
**Args:** `regenie --step 1 --bed genotypes.bed --out gwas_results --report report.html`
**Explanation:** Generates HTML report.