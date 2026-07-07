---
name: pyrodigal-rv
category: utility
description: Pyrodigal-RV extends Pyrodigal for gene prediction in RNA viruses.
tags: [pyrodigal-rv, utility, gene-prediction, rna-viruses]
author: oxo-call-community
source_url: "https://github.com/LanderDC/pyrodigal-rv"
---

## Concepts

- **Tool Overview**: pyrodigal-rv predicts RNA virus genes.
- **Core Function**: Gene prediction.
- **Algorithm**: Uses ORF finding.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces gene predictions.
- **Use Case**: RNA virus analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Strand Specificity**: Must be considered.
- **Gene Boundaries**: May be ambiguous.
- **Runtime**: Prediction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyrodigal-rv --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `pyrodigal-rv predict -i genome.fasta -o genes.gff`
**Explanation:** Predicts genes in RNA virus genome.

### With parameters
**Args:** `pyrodigal-rv predict -i genome.fasta -p params.yaml -o genes.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyrodigal-rv -v predict -i genome.fasta -o genes.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyrodigal-rv -t 4 predict -i genome.fasta -o genes.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Specify strand
**Args:** `pyrodigal-rv predict -i genome.fasta -s + -o genes.gff`
**Explanation:** Predicts on positive strand only.

### Generate report
**Args:** `pyrodigal-rv predict -i genome.fasta -o genes.gff --report report.html`
**Explanation:** Generates HTML report.