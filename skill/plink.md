---
name: plink
category: utility
description: plink performs whole genome association analysis.
tags: [plink, utility, gwas, association]
author: oxo-call-community
source_url: "https://www.cog-genomics.org/plink/"
---

## Concepts

- **Tool Overview**: plink analyzes genetic associations.
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
**Args:** `plink --help`
**Explanation:** Shows available options and usage instructions.

### Run association analysis
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --out results`
**Explanation:** Performs GWAS association analysis.

### With parameters
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --params params.yaml --out results`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --verbose --out results`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --threads 4 --out results`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --out results --format vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `plink --bfile genotype --pheno phenotype.txt --assoc --out results --report report.html`
**Explanation:** Generates HTML report.