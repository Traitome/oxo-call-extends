---
name: pyani-plus
category: utility
description: pyani-plus performs whole-genome classification of microbes using Average Nucleotide Identity and related methods.
tags: [pyani-plus, utility, microbial-classification, ANI]
author: oxo-call-community
source_url: "https://pyani-plus.github.io/pyani-plus-docs"
---

## Concepts

- **Tool Overview**: pyani-plus classifies microbes.
- **Core Function**: Microbial classification.
- **Algorithm**: Uses ANI-based methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces classification results.
- **Use Case**: Taxonomic identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Reference Database**: Affects classification.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyani-plus --help`
**Explanation:** Shows available options and usage instructions.

### Classify genome
**Args:** `pyani-plus classify -i genome.fasta -o classification.txt`
**Explanation:** Classifies microbial genome.

### With parameters
**Args:** `pyani-plus classify -i genome.fasta -p params.yaml -o classification.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyani-plus -v classify -i genome.fasta -o classification.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyani-plus -t 4 classify -i genome.fasta -o classification.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Update database
**Args:** `pyani-plus update-db -o database/`
**Explanation:** Updates reference database.

### Generate report
**Args:** `pyani-plus classify -i genome.fasta -o classification.txt --report report.html`
**Explanation:** Generates HTML report.