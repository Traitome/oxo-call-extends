---
name: psauron
category: annotation
description: psauron uses machine learning to assess protein-coding gene annotation quality.
tags: [psauron, annotation, machine-learning, gene-annotation]
author: oxo-call-community
source_url: "https://github.com/salzberg-lab/PSAURON"
---

## Concepts

- **Tool Overview**: psauron evaluates gene annotations.
- **Core Function**: Annotation assessment.
- **Algorithm**: Uses ML classification.
- **Input Format**: Accepts genome/annotation files.
- **Output**: Produces quality scores.
- **Use Case**: Genome annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Model Performance**: May have biases.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psauron --help`
**Explanation:** Shows available options and usage instructions.

### Assess annotation
**Args:** `psauron -i genome.fasta -a annotation.gff -o scores.txt`
**Explanation:** Evaluates gene annotation quality.

### With parameters
**Args:** `psauron -i genome.fasta -a annotation.gff --params params.yaml -o scores.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psauron -v -i genome.fasta -a annotation.gff -o scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psauron -t 4 -i genome.fasta -a annotation.gff -o scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psauron -i genome.fasta -a annotation.gff -o scores.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `psauron -i genome.fasta -a annotation.gff -o scores.txt --report report.html`
**Explanation:** Generates HTML report.