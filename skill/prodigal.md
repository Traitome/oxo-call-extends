---
name: prodigal
category: utility
description: prodigal is a microbial gene finding program for prokaryotic genomes.
tags: [prodigal, utility, gene-prediction, prokaryotes]
author: oxo-call-community
source_url: "https://github.com/hyattpd/Prodigal/wiki"
---

## Concepts

- **Tool Overview**: prodigal finds prokaryotic genes.
- **Core Function**: Gene prediction in bacteria/archaea.
- **Algorithm**: Uses dynamic programming methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces gene predictions.
- **Use Case**: Prokaryotic genome annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Gene Prediction**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prodigal --help`
**Explanation:** Shows available options and usage instructions.

### Predict genes
**Args:** `prodigal -i genome.fasta -o genes.gff`
**Explanation:** Predicts genes in prokaryotic genome.

### With parameters
**Args:** `prodigal -i genome.fasta -p params.txt -o genes.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prodigal -v -i genome.fasta -o genes.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prodigal -t 4 -i genome.fasta -o genes.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prodigal -i genome.fasta -o genes.embl --embl`
**Explanation:** Outputs in EMBL format.

### Generate report
**Args:** `prodigal -i genome.fasta -o genes.gff --report report.html`
**Explanation:** Generates HTML report.