---
name: phykit
category: population-genomics
description: phykit provides phylogenomic data processing and analysis tools.
tags: [phykit, population-genomics, phylogenomics, toolkit]
author: oxo-call-community
source_url: "https://github.com/jlsteenwyk/phykit"
---

## Concepts

- **Tool Overview**: phykit processes phylogenomic data.
- **Core Function**: Phylogenomic analysis toolkit.
- **Algorithm**: Uses phylogenomic analysis methods.
- **Input Format**: Accepts phylogenomic data files.
- **Output**: Produces phylogenomic analysis results.
- **Use Case**: Phylogenomics, data analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Analysis Method**: Requires proper method selection.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phykit --help`
**Explanation:** Shows available options and usage instructions.

### Process phylogenomic data
**Args:** `phykit -i phylogenomic_data.txt -o analysis_results.txt`
**Explanation:** Processes phylogenomic data.

### With parameters
**Args:** `phykit -i phylogenomic_data.txt -p params.yaml -o analysis_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phykit -v -i phylogenomic_data.txt -o analysis_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phykit -t 4 -i phylogenomic_data.txt -o analysis_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phykit -i phylogenomic_data.txt -o analysis_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phykit -i phylogenomic_data.txt -o analysis_results.txt --report report.html`
**Explanation:** Generates HTML report.