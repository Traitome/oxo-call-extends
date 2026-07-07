---
name: psqtl
category: formatting
description: psqtl predicts QTLs (Quantitative Trait Loci) using per-sample sequencing data.
tags: [psqtl, formatting, QTL-mapping, genetics]
author: oxo-call-community
source_url: "https://github.com/zkstewart/psQTL/wiki"
---

## Concepts

- **Tool Overview**: psqtl identifies QTLs from sequencing data.
- **Core Function**: QTL prediction.
- **Algorithm**: Uses statistical mapping.
- **Input Format**: Accepts genotype/phenotype data.
- **Output**: Produces QTL candidates.
- **Use Case**: Genetic mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Population Structure**: May affect mapping.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psqtl --help`
**Explanation:** Shows available options and usage instructions.

### Predict QTLs
**Args:** `psqtl -i genotypes.vcf -p phenotypes.txt -o qtl_results.txt`
**Explanation:** Predicts QTLs from genotype-phenotype data.

### With parameters
**Args:** `psqtl -i genotypes.vcf -p phenotypes.txt -params params.yaml -o qtl_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psqtl -v -i genotypes.vcf -p phenotypes.txt -o qtl_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psqtl -t 4 -i genotypes.vcf -p phenotypes.txt -o qtl_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psqtl -i genotypes.vcf -p phenotypes.txt -o qtl_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `psqtl -i genotypes.vcf -p phenotypes.txt -o qtl_results.txt --report report.html`
**Explanation:** Generates HTML report.