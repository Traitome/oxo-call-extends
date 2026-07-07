---
name: probord
category: utility
description: probord precisely delimits provirus borders in host genomes.
tags: [probord, utility, provirus, viral-integration]
author: oxo-call-community
source_url: "https://github.com/mujiezhang/ProBord"
---

## Concepts

- **Tool Overview**: probord identifies provirus boundaries.
- **Core Function**: Provirus border delimitation.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts genome sequence files.
- **Output**: Produces border coordinates.
- **Use Case**: Viral integration analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Boundary Accuracy**: May have precision issues.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probord --help`
**Explanation:** Shows available options and usage instructions.

### Find borders
**Args:** `probord -i genome.fasta -o borders.txt`
**Explanation:** Identifies provirus borders in host genome.

### With parameters
**Args:** `probord -i genome.fasta -p params.yaml -o borders.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probord -v -i genome.fasta -o borders.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probord -t 4 -i genome.fasta -o borders.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probord -i genome.fasta -o borders.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `probord -i genome.fasta -o borders.txt --report report.html`
**Explanation:** Generates HTML report.