---
name: plek
category: utility
description: plek predicts long non-coding RNAs and mRNAs.
tags: [plek, utility, lncRNA, prediction]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/plek"
---

## Concepts

- **Tool Overview**: plek predicts RNA types.
- **Core Function**: Long non-coding RNA prediction.
- **Algorithm**: Uses k-mer based machine learning.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces RNA classification results.
- **Use Case**: RNA-seq analysis, transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Prediction Accuracy**: May have classification errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plek --help`
**Explanation:** Shows available options and usage instructions.

### Predict RNA type
**Args:** `plek -i sequences.fasta -o predictions.txt`
**Explanation:** Predicts lncRNAs and mRNAs.

### With parameters
**Args:** `plek -i sequences.fasta -p params.yaml -o predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plek -v -i sequences.fasta -o predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plek -t 4 -i sequences.fasta -o predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plek -i sequences.fasta -o predictions.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `plek -i sequences.fasta -o predictions.txt --report report.html`
**Explanation:** Generates HTML report.