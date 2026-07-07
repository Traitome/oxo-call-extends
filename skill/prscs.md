---
name: prscs
category: variant-calling
description: prscs infers posterior SNP effect sizes using GWAS summary statistics and LD reference panels.
tags: [prscs, variant-calling, GWAS, polygenic-risk-score]
author: oxo-call-community
source_url: "https://github.com/getian107/PRScs"
---

## Concepts

- **Tool Overview**: prscs calculates polygenic risk scores.
- **Core Function**: SNP effect size estimation.
- **Algorithm**: Uses continuous shrinkage priors.
- **Input Format**: Accepts GWAS summary stats.
- **Output**: Produces effect size estimates.
- **Use Case**: Polygenic risk prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **LD Reference**: Affects accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prscs --help`
**Explanation:** Shows available options and usage instructions.

### Calculate PRS
**Args:** `prscs --ref_dir ref_panel --bim_prefix gwas_data --out prs_results`
**Explanation:** Infers SNP effect sizes.

### With parameters
**Args:** `prscs --ref_dir ref_panel --bim_prefix gwas_data --params params.yaml --out prs_results`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prscs -v --ref_dir ref_panel --bim_prefix gwas_data --out prs_results`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prscs -t 4 --ref_dir ref_panel --bim_prefix gwas_data --out prs_results`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prscs --ref_dir ref_panel --bim_prefix gwas_data --out prs_results --format csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `prscs --ref_dir ref_panel --bim_prefix gwas_data --out prs_results --report report.html`
**Explanation:** Generates HTML report.