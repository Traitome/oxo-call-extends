---
name: plinder
category: qc
description: plinder is a protein-ligand interaction dataset and evaluation resource.
tags: [plinder, qc, protein-ligand, interaction]
author: oxo-call-community
source_url: "https://www.plinder.sh"
---

## Concepts

- **Tool Overview**: plinder evaluates protein-ligand interactions.
- **Core Function**: Protein-ligand interaction prediction evaluation.
- **Algorithm**: Uses benchmark evaluation methods.
- **Input Format**: Accepts protein-ligand complex files.
- **Output**: Produces evaluation results.
- **Use Case**: Drug discovery, structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Evaluation Accuracy**: May have benchmark errors.
- **Runtime**: Evaluation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plinder --help`
**Explanation:** Shows available options and usage instructions.

### Evaluate predictions
**Args:** `plinder -i predictions.csv -o evaluation.txt`
**Explanation:** Evaluates protein-ligand interaction predictions.

### With parameters
**Args:** `plinder -i predictions.csv -p params.yaml -o evaluation.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plinder -v -i predictions.csv -o evaluation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plinder -t 4 -i predictions.csv -o evaluation.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plinder -i predictions.csv -o evaluation.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `plinder -i predictions.csv -o evaluation.txt --report report.html`
**Explanation:** Generates HTML report.