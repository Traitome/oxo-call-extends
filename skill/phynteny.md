---
name: phynteny
category: metagenomics
description: phynteny predicts bacteriophage genes using synteny.
tags: [phynteny, metagenomics, bacteriophage, synteny]
author: oxo-call-community
source_url: "https://github.com/susiegriggo/Phynteny"
---

## Concepts

- **Tool Overview**: phynteny predicts bacteriophage genes.
- **Core Function**: Synteny-based gene prediction.
- **Algorithm**: Uses synteny analysis methods.
- **Input Format**: Accepts bacteriophage sequence files.
- **Output**: Produces gene prediction results.
- **Use Case**: Metagenomics, bacteriophage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Synteny Analysis**: May have prediction errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phynteny --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `phynteny -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Predicts bacteriophage genes.

### With parameters
**Args:** `phynteny -i bacteriophage_sequences.fasta -p params.yaml -o gene_predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phynteny -v -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phynteny -t 4 -i bacteriophage_sequences.fasta -o gene_predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phynteny -i bacteriophage_sequences.fasta -o gene_predictions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phynteny -i bacteriophage_sequences.fasta -o gene_predictions.txt --report report.html`
**Explanation:** Generates HTML report.