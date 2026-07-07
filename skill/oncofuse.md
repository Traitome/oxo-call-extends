---
name: oncofuse
category: utility
description: Oncofuse predicts the oncogenic potential of gene fusions.
tags: [oncofuse, utility, gene-fusion, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/mikessh/oncofuse"
---

## Concepts

- **Tool Overview**: Oncofuse predicts oncogenic potential of gene fusions.
- **Core Function**: Evaluates gene fusion events for cancer relevance.
- **Algorithm**: Uses machine learning and biological features.
- **Input Format**: Accepts gene fusion predictions and patient data.
- **Output**: Produces oncogenic potential scores and classifications.
- **Use Case**: Cancer genomics, fusion gene analysis, and precision medicine.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Training Data**: Model trained on specific cancer types.
- **Input Quality**: Results depend on fusion prediction quality.
- **False Positives**: May predict false oncogenic fusions.
- **Model Limitations**: Limited to known fusion types.
- **Validation**: Results should be experimentally validated.

## Examples

### Display help
**Args:** `oncofuse --help`
**Explanation:** Shows available options and usage instructions.

### Predict oncogenicity
**Args:** `oncofuse -i fusions.txt -o predictions.txt`
**Explanation:** Predicts oncogenic potential of gene fusions.

### With patient data
**Args:** `oncofuse -i fusions.txt -p patient_data.txt -o predictions.txt`
**Explanation:** Incorporates patient data for prediction.

### Output format
**Args:** `oncofuse -i fusions.txt -o results.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `oncofuse -i fusions.txt -v -o predictions.txt`
**Explanation:** Runs with verbose output.

### Confidence threshold
**Args:** `oncofuse -i fusions.txt -t 0.9 -o predictions.txt`
**Explanation:** Sets confidence threshold to 0.9.

### Batch processing
**Args:** `oncofuse -d fusions/ -o results/`
**Explanation:** Processes multiple fusion files.