---
name: piaso
category: expression
description: piaso provides integrative analysis of single-cell omics data.
tags: [piaso, expression, single-cell, omics]
author: oxo-call-community
source_url: "https://piaso.org"
---

## Concepts

- **Tool Overview**: piaso analyzes single-cell omics data.
- **Core Function**: Integrative single-cell analysis.
- **Algorithm**: Uses integration methods.
- **Input Format**: Accepts single-cell RNA-seq/ATAC-seq files.
- **Output**: Produces integration analysis results.
- **Use Case**: Single-cell analysis, omics integration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Batch Integration**: May have integration errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piaso --help`
**Explanation:** Shows available options and usage instructions.

### Analyze single-cell data
**Args:** `piaso -i single_cell_data.txt -o analysis_results.txt`
**Explanation:** Analyzes single-cell omics data.

### With parameters
**Args:** `piaso -i single_cell_data.txt -p params.yaml -o analysis_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piaso -v -i single_cell_data.txt -o analysis_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piaso -t 4 -i single_cell_data.txt -o analysis_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piaso -i single_cell_data.txt -o analysis_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `piaso -i single_cell_data.txt -o analysis_results.txt --report report.html`
**Explanation:** Generates HTML report.