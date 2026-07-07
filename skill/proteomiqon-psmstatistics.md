---
name: proteomiqon-psmstatistics
category: expression
description: proteomiqon-psmstatistics integrates search engine scores using semi-supervised machine learning for consensus scoring.
tags: [proteomiqon-psmstatistics, expression, proteomics, machine-learning]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/PSMStatistics.html"
---

## Concepts

- **Tool Overview**: proteomiqon-psmstatistics analyzes PSM data.
- **Core Function**: Consensus score calculation.
- **Algorithm**: Uses semi-supervised ML.
- **Input Format**: Accepts PSM results.
- **Output**: Produces quality scores.
- **Use Case**: PSM quality assessment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Model Training**: May require tuning.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-psmstatistics --help`
**Explanation:** Shows available options and usage instructions.

### Calculate statistics
**Args:** `proteomiqon-psmstatistics -i psm_results.txt -o statistics.txt`
**Explanation:** Computes consensus scores.

### With parameters
**Args:** `proteomiqon-psmstatistics -i psm_results.txt --params params.yaml -o statistics.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-psmstatistics -v -i psm_results.txt -o statistics.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-psmstatistics -t 4 -i psm_results.txt -o statistics.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proteomiqon-psmstatistics -i psm_results.txt -o statistics.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `proteomiqon-psmstatistics -i psm_results.txt -o statistics.txt --report report.html`
**Explanation:** Generates HTML report.