---
name: plink2
category: utility
description: plink2 performs whole genome association analysis.
tags: [plink2, utility, gwas, association]
author: oxo-call-community
source_url: "https://www.cog-genomics.org/plink2"
---

## Concepts

- **Tool Overview**: plink2 analyzes genetic associations.
- **Core Function**: Whole genome association analysis.
- **Algorithm**: Uses statistical genetics methods.
- **Input Format**: Accepts genotype files.
- **Output**: Produces association results.
- **Use Case**: GWAS, population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on genotype quality.
- **Statistical Power**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plink2 --help`
**Explanation:** Shows available options and usage instructions.

### Run association analysis
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --out results`
**Explanation:** Performs GWAS association analysis.

### With parameters
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --params params.yaml --out results`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --verbose --out results`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --threads 4 --out results`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --out results --format vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `plink2 --bfile genotype --pheno phenotype.txt --assoc --out results --report report.html`
**Explanation:** Generates HTML report.