---
name: pegasuspy
category: expression
description: Pegasus analyzes transcriptomes of millions of single cells.
tags: [pegasuspy, expression, single-cell, transcriptome]
author: oxo-call-community
source_url: "https://github.com/lilab-bcb/pegasus"
---

## Concepts

- **Tool Overview**: Pegasus analyzes single-cell data.
- **Core Function**: Processes transcriptomes at scale.
- **Algorithm**: Uses efficient Python processing.
- **Input Format**: Accepts single-cell expression data.
- **Output**: Produces analysis results.
- **Use Case**: Single-cell analysis, transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Analysis Parameters**: Requires proper parameter setup.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pegasus --help`
**Explanation:** Shows available options and usage instructions.

### Analyze data
**Args:** `pegasus analyze -i data.h5ad -o results/`
**Explanation:** Analyzes single-cell transcriptome.

### With parameters
**Args:** `pegasus analyze -i data.h5ad -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pegasus -v analyze -i data.h5ad -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pegasus analyze -t 8 -i data.h5ad -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pegasus analyze -i data.h5ad -o results/ --format h5ad`
**Explanation:** Outputs in h5ad format.

### Generate report
**Args:** `pegasus analyze -i data.h5ad -o results/ --report report.html`
**Explanation:** Generates HTML report.