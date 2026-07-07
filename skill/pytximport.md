---
name: pytximport
category: alignment
description: PyTximport performs gene count estimation from transcript-level quantification data.
tags: [pytximport, alignment, gene-expression, quantification]
author: oxo-call-community
source_url: "https://pytximport.readthedocs.io"
---

## Concepts

- **Tool Overview**: pytximport aggregates transcript counts.
- **Core Function**: Gene-level quantification.
- **Algorithm**: Uses summation/aggregation.
- **Input Format**: Accepts quantification files.
- **Output**: Produces gene counts.
- **Use Case**: RNA-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Annotation**: Must be correct.
- **Ambiguity**: May affect counts.
- **Runtime**: Aggregation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pytximport --help`
**Explanation:** Shows available options and usage instructions.

### Run aggregation
**Args:** `pytximport aggregate -i quant.sf -o gene_counts.txt`
**Explanation:** Aggregates transcript counts.

### With parameters
**Args:** `pytximport aggregate -i quant.sf -p params.yaml -o gene_counts.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pytximport -v aggregate -i quant.sf -o gene_counts.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pytximport -t 4 aggregate -i quant.sf -o gene_counts.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With annotation
**Args:** `pytximport aggregate -i quant.sf -a annotation.gtf -o gene_counts.txt`
**Explanation:** Uses GTF annotation.

### Generate report
**Args:** `pytximport aggregate -i quant.sf -o gene_counts.txt --report report.html`
**Explanation:** Generates HTML report.