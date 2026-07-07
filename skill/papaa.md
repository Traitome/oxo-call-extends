---
name: papaa
category: variant-calling
description: PAPAA measures mutation-specific pathway activity in cancer datasets.
tags: [papaa, variant-calling, cancer, pathway-analysis]
author: oxo-call-community
source_url: "https://github.com/nvk747/papaa"
---

## Concepts

- **Tool Overview**: PAPAA analyzes mutation-specific pathway activity.
- **Core Function**: Measures pathway activity from mutation data.
- **Algorithm**: Uses statistical methods to quantify pathway activity.
- **Input Format**: Accepts mutation data and pathway definitions.
- **Output**: Produces pathway activity scores.
- **Use Case**: Cancer genomics, pathway analysis, TCGA data analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on input data quality.
- **Pathway Definitions**: Results depend on pathway databases.
- **Sample Size**: Requires sufficient sample size.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `papaa --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `papaa -i mutations.txt -p pathways.gmt -o results/`
**Explanation:** Analyzes pathway activity.

### With TCGA data
**Args:** `papaa tcga -i tcga_data/ -o results/`
**Explanation:** Analyzes TCGA pancancer dataset.

### Verbose mode
**Args:** `papaa -v -i mutations.txt -p pathways.gmt -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `papaa -t 8 -i mutations.txt -p pathways.gmt -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `papaa -i mutations.txt -p pathways.gmt -o results.json --json`
**Explanation:** Outputs in JSON format.

### Plot results
**Args:** `papaa plot -i results/ -o plot.pdf`
**Explanation:** Generates visualization of results.