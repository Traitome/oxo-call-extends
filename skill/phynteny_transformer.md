---
name: phynteny_transformer
category: metagenomics
description: phynteny_transformer predicts bacteriophage genes using transformer models.
tags: [phynteny_transformer, metagenomics, bacteriophage, transformer]
author: oxo-call-community
source_url: "https://github.com/susiegriggo/Phynteny_transformer"
---

## Concepts

- **Tool Overview**: phynteny_transformer predicts bacteriophage genes.
- **Core Function**: Transformer-based gene prediction.
- **Algorithm**: Uses deep learning methods.
- **Input Format**: Accepts bacteriophage sequence files.
- **Output**: Produces gene prediction results.
- **Use Case**: Metagenomics, bacteriophage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Transformer Model**: May have prediction errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phynteny_transformer --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `phynteny_transformer -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Predicts bacteriophage genes with transformer.

### With parameters
**Args:** `phynteny_transformer -i bacteriophage_sequences.fasta -p params.yaml -o gene_predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phynteny_transformer -v -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phynteny_transformer -t 4 -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phynteny_transformer -i bacteriophage_sequences.fasta -o gene_predictions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phynteny_transformer -i bacteriophage_sequences.fasta -o gene_predictions.txt --report report.html`
**Explanation:** Generates HTML report.