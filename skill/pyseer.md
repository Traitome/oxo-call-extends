---
name: pyseer
category: programming
description: PySEER is a Python implementation of Sequence Element Enrichment Analysis (SEER) for GWAS.
tags: [pyseer, programming, gwas, enrichment]
author: oxo-call-community
source_url: "https://pyseer.readthedocs.io/en/master"
---

## Concepts

- **Tool Overview**: pyseer performs GWAS enrichment.
- **Core Function**: Association mapping.
- **Algorithm**: Uses linear mixed models.
- **Input Format**: Accepts genotype/phenotype data.
- **Output**: Produces association results.
- **Use Case**: GWAS analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Population Structure**: Must be accounted for.
- **Multiple Testing**: Must be corrected.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyseer --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pyseer --phenotypes pheno.txt --genotypes geno.vcf -o results.txt`
**Explanation:** Performs GWAS analysis.

### With parameters
**Args:** `pyseer --phenotypes pheno.txt -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyseer -v --phenotypes pheno.txt -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyseer -t 4 --phenotypes pheno.txt -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Kinship matrix
**Args:** `pyseer --phenotypes pheno.txt --kinship kinship.txt -o results.txt`
**Explanation:** Uses custom kinship matrix.

### Generate report
**Args:** `pyseer --phenotypes pheno.txt -o results.txt --report report.html`
**Explanation:** Generates HTML report.