---
name: pyclone-vi
category: population-genomics
description: PyClone-VI is a fast variational inference method for inferring clonal population structure from sequencing data.
tags: [pyclone-vi, population-genomics, clonal-analysis, variational-inference]
author: oxo-call-community
source_url: "https://github.com/Roth-Lab/pyclone-vi"
---

## Concepts

- **Tool Overview**: pyclone-vi performs fast clonal inference.
- **Core Function**: Variational inference for clones.
- **Algorithm**: Uses variational Bayes.
- **Input Format**: Accepts variant data.
- **Output**: Produces clonal assignments.
- **Use Case**: Cancer genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Model Convergence**: May require tuning.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyclone-vi --help`
**Explanation:** Shows available options and usage instructions.

### Run inference
**Args:** `pyclone-vi run -i variants.tsv -o results/`
**Explanation:** Runs variational inference for clonal structure.

### With parameters
**Args:** `pyclone-vi run -i variants.tsv -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyclone-vi -v run -i variants.tsv -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyclone-vi -t 4 run -i variants.tsv -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Analyze convergence
**Args:** `pyclone-vi converge -i results/ -o convergence.txt`
**Explanation:** Analyzes convergence diagnostics.

### Generate report
**Args:** `pyclone-vi run -i variants.tsv -o results/ --report report.html`
**Explanation:** Generates HTML report.