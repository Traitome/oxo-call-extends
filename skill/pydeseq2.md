---
name: pydeseq2
category: expression
description: pyDESeq2 is a Python implementation of DESeq2 for differential expression analysis of RNA-seq data.
tags: [pydeseq2, expression, rna-seq, differential-expression]
author: oxo-call-community
source_url: "https://pydeseq2.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: pydeseq2 analyzes differential expression.
- **Core Function**: RNA-seq differential expression.
- **Algorithm**: Uses DESeq2 statistical model.
- **Input Format**: Accepts count matrices.
- **Output**: Produces differential expression results.
- **Use Case**: Gene expression analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Sample Size**: Affects statistical power.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pydeseq2 --help`
**Explanation:** Shows available options and usage instructions.

### Run differential expression
**Args:** `pydeseq2 run -i counts.tsv -c design.csv -o results/`
**Explanation:** Performs differential expression analysis.

### With parameters
**Args:** `pydeseq2 run -i counts.tsv -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pydeseq2 -v run -i counts.tsv -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pydeseq2 -t 4 run -i counts.tsv -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Plot results
**Args:** `pydeseq2 plot -i results/ -o volcano.png`
**Explanation:** Generates volcano plot.

### Generate report
**Args:** `pydeseq2 run -i counts.tsv -o results/ --report report.html`
**Explanation:** Generates HTML report.