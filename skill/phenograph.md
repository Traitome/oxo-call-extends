---
name: phenograph
category: expression
description: phenograph performs graph-based clustering for single-cell data.
tags: [phenograph, expression, clustering, single-cell]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/PhenoGraph"
---

## Concepts

- **Tool Overview**: phenograph clusters single-cell data.
- **Core Function**: Graph-based clustering algorithm.
- **Algorithm**: Uses community detection methods.
- **Input Format**: Accepts high-dimensional data files.
- **Output**: Produces cluster assignments.
- **Use Case**: Single-cell analysis, data clustering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Parameter Tuning**: Requires proper parameter selection.
- **Runtime**: Clustering may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phenograph --help`
**Explanation:** Shows available options and usage instructions.

### Cluster data
**Args:** `phenograph -i data.txt -o clusters.txt`
**Explanation:** Clusters high-dimensional data.

### With parameters
**Args:** `phenograph -i data.txt -p params.yaml -o clusters.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phenograph -v -i data.txt -o clusters.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phenograph -t 4 -i data.txt -o clusters.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phenograph -i data.txt -o clusters.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phenograph -i data.txt -o clusters.txt --report report.html`
**Explanation:** Generates HTML report.