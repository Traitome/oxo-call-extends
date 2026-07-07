---
name: resistify
category: annotation
description: Resistify annotates resistance genes in bacterial genomes.
tags: [resistify, annotation, resistance-genes, bacteria]
author: oxo-call-community
source_url: "https://github.com/SwiftSeal/resistify/blob/v2.1.0/README.md"
---

## Concepts

- **Tool Overview**: resistify annotates resistance.
- **Core Function**: Resistance gene annotation.
- **Algorithm**: Uses sequence comparison methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces annotations.
- **Use Case**: Antibiotic resistance analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Database Quality**: Affects annotation.
- **Parameters**: Must be configured.
- **Runtime**: Annotation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `resistify --help`
**Explanation:** Shows available options and usage instructions.

### Annotate resistance genes
**Args:** `resistify annotate -i genome.fasta -o annotation.gff`
**Explanation:** Annotates resistance genes in genome.

### With parameters
**Args:** `resistify annotate -i genome.fasta -p params.yaml -o annotation.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `resistify -v annotate -i genome.fasta -o annotation.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `resistify -t 4 annotate -i genome.fasta -o annotation.gff`
**Explanation:** Uses 4 threads for parallel processing.

### With database
**Args:** `resistify annotate -i genome.fasta -d db_path -o annotation.gff`
**Explanation:** Uses custom database.

### Generate report
**Args:** `resistify annotate -i genome.fasta -o annotation.gff --report report.html`
**Explanation:** Generates HTML report.