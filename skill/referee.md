---
name: referee
category: qc
description: Referee provides quality scoring for reference genomes for genome quality assessment.
tags: [referee, qc, genome-quality, reference-genomes]
author: oxo-call-community
source_url: "https://github.com/gwct/referee"
---

## Concepts

- **Tool Overview**: referee scores genomes.
- **Core Function**: Genome quality scoring.
- **Algorithm**: Uses scoring methods.
- **Input Format**: Accepts genome assemblies.
- **Output**: Produces quality scores.
- **Use Case**: Genome QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Assembly Quality**: Affects scoring.
- **Parameters**: Must be configured.
- **Runtime**: Scoring may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `referee --help`
**Explanation:** Shows available options and usage instructions.

### Score genome
**Args:** `referee score -i genome.fasta -o quality_scores.txt`
**Explanation:** Scores genome quality.

### With parameters
**Args:** `referee score -i genome.fasta -p params.yaml -o quality_scores.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `referee -v score -i genome.fasta -o quality_scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `referee -t 4 score -i genome.fasta -o quality_scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `referee score -i genome.fasta -r reference.fasta -o quality_scores.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `referee score -i genome.fasta -o quality_scores.txt --report report.html`
**Explanation:** Generates HTML report.