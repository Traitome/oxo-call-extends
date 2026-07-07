---
name: omamer
category: alignment
description: OMAmer assigns proteins to orthologous sub-families using tree-driven alignment-free methods.
tags: [omamer, alignment, orthology, protein-analysis]
author: oxo-call-community
source_url: "https://github.com/DessimozLab/omamer"
---

## Concepts

- **Tool Overview**: OMAmer assigns proteins to orthologous sub-families.
- **Core Function**: Classifies proteins into evolutionary sub-families.
- **Algorithm**: Uses tree-driven and alignment-free methods.
- **Input Format**: Accepts FASTA protein sequences.
- **Output**: Produces orthology assignments and scores.
- **Use Case**: Comparative genomics, protein classification, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Requirements**: Requires OMA database.
- **Sequence Quality**: Results depend on input sequence quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `omamer --help`
**Explanation:** Shows available options and usage instructions.

### Assign proteins
**Args:** `omamer assign -i proteins.fasta -o assignments.txt`
**Explanation:** Assigns proteins to orthologous sub-families.

### With database
**Args:** `omamer assign -i proteins.fasta -d oma_db -o assignments.txt`
**Explanation:** Uses custom OMA database.

### Output format
**Args:** `omamer assign -i proteins.fasta -o results.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `omamer assign -i proteins.fasta -v -o assignments.txt`
**Explanation:** Runs with verbose output.

### Create database
**Args:** `omamer build -i sequences.fasta -o oma_db`
**Explanation:** Creates custom OMA database.

### Threads
**Args:** `omamer assign -i proteins.fasta -t 8 -o assignments.txt`
**Explanation:** Uses 8 threads for parallel processing.