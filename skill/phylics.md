---
name: phylics
category: expression
description: phylics provides single-cell CNV data analysis tools.
tags: [phylics, expression, single-cell, cnv]
author: oxo-call-community
source_url: "https://github.com/bioinformatics-polito/PhyliCS"
---

## Concepts

- **Tool Overview**: phylics analyzes single-cell CNV data.
- **Core Function**: Single-cell CNV analysis toolkit.
- **Algorithm**: Uses CNV analysis methods.
- **Input Format**: Accepts single-cell data files.
- **Output**: Produces CNV analysis results.
- **Use Case**: Single-cell analysis, CNV detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **CNV Detection**: May miss low-frequency CNVs.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylics --help`
**Explanation:** Shows available options and usage instructions.

### Analyze CNV
**Args:** `phylics -i single_cell_data.txt -o cnv_results.txt`
**Explanation:** Analyzes single-cell CNV data.

### With config
**Args:** `phylics -i single_cell_data.txt -c config.yaml -o cnv_results.txt`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `phylics -v -i single_cell_data.txt -o cnv_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylics -t 4 -i single_cell_data.txt -o cnv_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylics -i single_cell_data.txt -o cnv_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylics -i single_cell_data.txt -o cnv_results.txt --report report.html`
**Explanation:** Generates HTML report.