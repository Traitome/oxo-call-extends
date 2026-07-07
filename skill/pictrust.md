---
name: pictrust
category: population-genomics
description: pictrust provides trust scores for PICRUSt predictions.
tags: [pictrust, population-genomics, trust-score, prediction]
author: oxo-call-community
source_url: "http://picrust.github.com"
---

## Concepts

- **Tool Overview**: pictrust calculates trust scores.
- **Core Function**: Prediction confidence scoring.
- **Algorithm**: Uses statistical scoring methods.
- **Input Format**: Accepts prediction results.
- **Output**: Produces trust score results.
- **Use Case**: Prediction validation, confidence assessment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Prediction Quality**: Results depend on input quality.
- **Score Calculation**: May have calculation errors.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pictrust --help`
**Explanation:** Shows available options and usage instructions.

### Calculate trust scores
**Args:** `pictrust -i predictions.txt -o trust_scores.txt`
**Explanation:** Calculates trust scores for predictions.

### With parameters
**Args:** `pictrust -i predictions.txt -p params.yaml -o trust_scores.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pictrust -v -i predictions.txt -o trust_scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pictrust -t 4 -i predictions.txt -o trust_scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pictrust -i predictions.txt -o trust_scores.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pictrust -i predictions.txt -o trust_scores.txt --report report.html`
**Explanation:** Generates HTML report.