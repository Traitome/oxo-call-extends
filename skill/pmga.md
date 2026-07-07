---
name: pmga
category: annotation
description: pmga annotates genomes using PubMLST scheme.
tags: [pmga, annotation, pubmlst, genome]
author: oxo-call-community
source_url: "https://github.com/CDCgov/BMGAP"
---

## Concepts

- **Tool Overview**: pmga annotates bacterial genomes.
- **Core Function**: PubMLST genome annotation.
- **Algorithm**: Uses sequence matching methods.
- **Input Format**: Accepts FASTA genome files.
- **Output**: Produces MLST typing results.
- **Use Case**: Bacterial typing, epidemiological analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on sequence quality.
- **Typing Accuracy**: May have classification errors.
- **Runtime**: Annotation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pmga --help`
**Explanation:** Shows available options and usage instructions.

### Annotate genome
**Args:** `pmga -i genome.fasta -o annotation.txt`
**Explanation:** Annotates genome using PubMLST scheme.

### With parameters
**Args:** `pmga -i genome.fasta -p params.yaml -o annotation.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pmga -v -i genome.fasta -o annotation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmga -t 4 -i genome.fasta -o annotation.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmga -i genome.fasta -o annotation.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pmga -i genome.fasta -o annotation.txt --report report.html`
**Explanation:** Generates HTML report.