---
name: pigpen
category: expression
description: pigpen quantifies RNA localization using OINC-seq data.
tags: [pigpen, expression, rna-localization, oinc-seq]
author: oxo-call-community
source_url: "https://github.com/TaliaferroLab/OINC-seq"
---

## Concepts

- **Tool Overview**: pigpen quantifies RNA localization.
- **Core Function**: OINC-seq data analysis.
- **Algorithm**: Uses RNA localization methods.
- **Input Format**: Accepts OINC-seq data files.
- **Output**: Produces RNA localization results.
- **Use Case**: RNA analysis, localization quantification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Localization Analysis**: May have analysis errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pigpen --help`
**Explanation:** Shows available options and usage instructions.

### Quantify RNA localization
**Args:** `pigpen -i oinc_seq_data.txt -o localization_results.txt`
**Explanation:** Quantifies RNA localization from OINC-seq data.

### With parameters
**Args:** `pigpen -i oinc_seq_data.txt -p params.yaml -o localization_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pigpen -v -i oinc_seq_data.txt -o localization_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pigpen -t 4 -i oinc_seq_data.txt -o localization_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pigpen -i oinc_seq_data.txt -o localization_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pigpen -i oinc_seq_data.txt -o localization_results.txt --report report.html`
**Explanation:** Generates HTML report.