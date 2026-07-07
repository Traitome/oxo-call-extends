---
name: peer
category: expression
description: PEER infers hidden determinants from gene expression using factor analysis.
tags: [peer, expression, factor-analysis, bayesian]
author: oxo-call-community
source_url: "https://github.com/PMBio/peer"
---

## Concepts

- **Tool Overview**: PEER infers hidden factors.
- **Core Function**: Identifies hidden determinants in expression.
- **Algorithm**: Uses Bayesian factor analysis.
- **Input Format**: Accepts expression matrices.
- **Output**: Produces inferred factors.
- **Use Case**: Expression analysis, confounder detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large matrices require memory.
- **Expression Quality**: Results depend on data quality.
- **Factor Number**: Requires proper factor selection.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peer --help`
**Explanation:** Shows available options and usage instructions.

### Infer factors
**Args:** `peer -i expression.tsv -o factors.tsv`
**Explanation:** Infers hidden factors from expression.

### With factor number
**Args:** `peer -i expression.tsv -n 10 -o factors.tsv`
**Explanation:** Infers 10 hidden factors.

### Verbose mode
**Args:** `peer -v -i expression.tsv -o factors.tsv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peer -t 4 -i expression.tsv -o factors.tsv`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peer -i expression.tsv -o factors.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `peer -i expression.tsv -o factors.tsv --report report.html`
**Explanation:** Generates HTML report.