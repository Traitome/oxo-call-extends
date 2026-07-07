---
name: ppanini
category: annotation
description: ppanini predicts functional annotations via network integration.
tags: [ppanini, annotation, functional-prediction, network]
author: oxo-call-community
source_url: "http://huttenhower.sph.harvard.edu/ppanini"
---

## Concepts

- **Tool Overview**: ppanini annotates gene functions.
- **Core Function**: Functional prediction.
- **Algorithm**: Uses network integration methods.
- **Input Format**: Accepts genome/network files.
- **Output**: Produces functional annotations.
- **Use Case**: Gene annotation, functional genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large networks require memory.
- **Data Quality**: Results depend on input quality.
- **Prediction Accuracy**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ppanini --help`
**Explanation:** Shows available options and usage instructions.

### Predict annotations
**Args:** `ppanini -i genes.fasta -n network.txt -o annotations.txt`
**Explanation:** Predicts functional annotations.

### With parameters
**Args:** `ppanini -i genes.fasta -n network.txt -p params.yaml -o annotations.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ppanini -v -i genes.fasta -n network.txt -o annotations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ppanini -t 4 -i genes.fasta -n network.txt -o annotations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `ppanini -i genes.fasta -n network.txt -o annotations.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `ppanini -i genes.fasta -n network.txt -o annotations.txt --report report.html`
**Explanation:** Generates HTML report.