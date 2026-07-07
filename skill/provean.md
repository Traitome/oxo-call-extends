---
name: provean
category: variant-calling
description: provean predicts the functional impact of amino acid substitutions and indels on protein function.
tags: [provean, variant-calling, protein-variation, functional-prediction]
author: oxo-call-community
source_url: "https://www.jcvi.org/research/provean"
---

## Concepts

- **Tool Overview**: provean analyzes variant effects.
- **Core Function**: Functional impact prediction.
- **Algorithm**: Uses sequence homology methods.
- **Input Format**: Accepts variant data.
- **Output**: Produces impact scores.
- **Use Case**: Variant functional analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Predictive Accuracy**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `provean.sh --help`
**Explanation:** Shows available options and usage instructions.

### Predict impact
**Args:** `provean.sh -f protein.fasta -v variants.txt -o results.txt`
**Explanation:** Predicts variant functional impact.

### With parameters
**Args:** `provean.sh -f protein.fasta -v variants.txt --params params.txt -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `provean.sh -v -f protein.fasta -v variants.txt -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `provean.sh -t 4 -f protein.fasta -v variants.txt -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `provean.sh -f protein.fasta -v variants.txt -o results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `provean.sh -f protein.fasta -v variants.txt -o results.txt --report report.html`
**Explanation:** Generates HTML report.