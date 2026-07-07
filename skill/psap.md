---
name: psap
category: utility
description: psap predicts protein phase separation probability using a RandomForest classifier.
tags: [psap, utility, machine-learning, protein-phase-separation]
author: oxo-call-community
source_url: "https://github.com/vanheeringen-lab/psap"
---

## Concepts

- **Tool Overview**: psap predicts phase separation.
- **Core Function**: Protein phase separation prediction.
- **Algorithm**: Uses RandomForest classification.
- **Input Format**: Accepts protein sequences.
- **Output**: Produces probability scores.
- **Use Case**: Protein biophysics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Model Accuracy**: May have false positives.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psap --help`
**Explanation:** Shows available options and usage instructions.

### Predict PPS
**Args:** `psap predict -i proteins.fasta -o predictions.txt`
**Explanation:** Predicts phase separation probability.

### With parameters
**Args:** `psap predict -i proteins.fasta -p params.yaml -o predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psap -v predict -i proteins.fasta -o predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psap -t 4 predict -i proteins.fasta -o predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psap predict -i proteins.fasta -o predictions.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `psap predict -i proteins.fasta -o predictions.txt --report report.html`
**Explanation:** Generates HTML report.