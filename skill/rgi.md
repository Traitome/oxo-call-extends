---
name: rgi
category: annotation
description: RGI annotates antibiotic resistance genes using the CARD database.
tags: [rgi, annotation, antibiotic-resistance, card-database]
author: oxo-call-community
source_url: "https://card.mcmaster.ca"
---

## Concepts

- **Tool Overview**: rgi annotates resistance genes.
- **Core Function**: Antibiotic resistance gene detection.
- **Algorithm**: Uses BLAST-based methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces resistance gene annotations.
- **Use Case**: Antibiotic resistance analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Database Updates**: Must be maintained.
- **Parameters**: Must be configured.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rgi --help`
**Explanation:** Shows available options and usage instructions.

### Annotate genome
**Args:** `rgi main -i genome.fasta -o results/`
**Explanation:** Annotates antibiotic resistance genes.

### With parameters
**Args:** `rgi main -i genome.fasta -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rgi -v main -i genome.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rgi -t 4 main -i genome.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `rgi main -i genome.fasta -d custom_db -o results/`
**Explanation:** Uses custom CARD database.

### Generate report
**Args:** `rgi main -i genome.fasta -o results/ --report report.html`
**Explanation:** Generates HTML report.