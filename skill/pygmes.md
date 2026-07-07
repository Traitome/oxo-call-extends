---
name: pygmes
category: utility
description: pygmes runs GeneMark-ES gene prediction using pretrained models.
tags: [pygmes, utility, gene-prediction, genemark]
author: oxo-call-community
source_url: "https://github.com/openpaul/pygmes"
---

## Concepts

- **Tool Overview**: pygmes predicts genes.
- **Core Function**: Gene prediction.
- **Algorithm**: Uses GeneMark-ES.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces gene predictions.
- **Use Case**: Genome annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Model Selection**: Affects predictions.
- **Training Data**: Model quality matters.
- **Runtime**: Prediction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pygmes --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `pygmes predict -i genome.fasta -o predictions.gff`
**Explanation:** Predicts genes using GeneMark-ES.

### With parameters
**Args:** `pygmes predict -i genome.fasta -p params.yaml -o predictions.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pygmes -v predict -i genome.fasta -o predictions.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pygmes -t 4 predict -i genome.fasta -o predictions.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Specify model
**Args:** `pygmes predict -i genome.fasta -m model.hmm -o predictions.gff`
**Explanation:** Uses custom model.

### Generate report
**Args:** `pygmes predict -i genome.fasta -o predictions.gff --report report.html`
**Explanation:** Generates HTML report.