---
name: pyrodigal-gv
category: utility
description: Pyrodigal-GV extends Pyrodigal for gene prediction in giant viruses and viruses with alternative genetic codes.
tags: [pyrodigal-gv, utility, gene-prediction, viruses]
author: oxo-call-community
source_url: "https://github.com/althonos/pyrodigal-gv"
---

## Concepts

- **Tool Overview**: pyrodigal-gv predicts viral genes.
- **Core Function**: Gene prediction.
- **Algorithm**: Uses ORF finding.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces gene predictions.
- **Use Case**: Viral genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Genetic Code**: Must be specified.
- **Gene Boundaries**: May be ambiguous.
- **Runtime**: Prediction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyrodigal-gv --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `pyrodigal-gv predict -i genome.fasta -o genes.gff`
**Explanation:** Predicts genes in giant virus genome.

### With parameters
**Args:** `pyrodigal-gv predict -i genome.fasta -p params.yaml -o genes.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyrodigal-gv -v predict -i genome.fasta -o genes.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyrodigal-gv -t 4 predict -i genome.fasta -o genes.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Specify genetic code
**Args:** `pyrodigal-gv predict -i genome.fasta -g 11 -o genes.gff`
**Explanation:** Uses specific genetic code.

### Generate report
**Args:** `pyrodigal-gv predict -i genome.fasta -o genes.gff --report report.html`
**Explanation:** Generates HTML report.