---
name: raiss
category: variant-calling
description: RAISS performs SNP summary statistics imputation for genetic association studies.
tags: [raiss, variant-calling, imputation, genetics]
author: oxo-call-community
source_url: "http://statistical-genetics.pages.pasteur.fr/raiss/"
---

## Concepts

- **Tool Overview**: raiss imputes SNPs.
- **Core Function**: SNP imputation.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts summary statistics.
- **Output**: Produces imputed data.
- **Use Case**: Genetic association.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Panel**: Must be compatible.
- **Parameters**: Must be configured.
- **Runtime**: Imputation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `raiss --help`
**Explanation:** Shows available options and usage instructions.

### Impute SNPs
**Args:** `raiss impute -i summary_stats.txt -r reference_panel.txt -o imputed.txt`
**Explanation:** Imputes missing SNP statistics.

### With parameters
**Args:** `raiss impute -i summary_stats.txt -p params.yaml -o imputed.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raiss -v impute -i summary_stats.txt -o imputed.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raiss -t 4 impute -i summary_stats.txt -o imputed.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With LD reference
**Args:** `raiss impute -i summary_stats.txt -l ld_panel.txt -o imputed.txt`
**Explanation:** Uses LD reference panel.

### Generate report
**Args:** `raiss impute -i summary_stats.txt -o imputed.txt --report report.html`
**Explanation:** Generates HTML report.