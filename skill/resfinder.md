---
name: resfinder
category: utility
description: ResFinder identifies acquired antimicrobial resistance genes in bacterial isolates.
tags: [resfinder, utility, antimicrobial-resistance, bacteria]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/resfinder/src/master/README.md"
---

## Concepts

- **Tool Overview**: resfinder finds resistance genes.
- **Core Function**: Antimicrobial resistance gene detection.
- **Algorithm**: Uses BLAST-based methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces resistance gene list.
- **Use Case**: Antibiotic resistance analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Database Updates**: Must be maintained.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `resfinder.py -h`
**Explanation:** Shows available options and usage instructions.

### Identify resistance genes
**Args:** `resfinder.py -i genome.fasta -o results/`
**Explanation:** Identifies antimicrobial resistance genes.

### With parameters
**Args:** `resfinder.py -i genome.fasta -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `resfinder.py -v -i genome.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `resfinder.py -t 4 -i genome.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `resfinder.py -i genome.fasta -d custom_db -o results/`
**Explanation:** Uses custom resistance gene database.

### Generate report
**Args:** `resfinder.py -i genome.fasta -o results/ --report report.html`
**Explanation:** Generates HTML report.