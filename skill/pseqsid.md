---
name: pseqsid
category: alignment
description: pseqsid calculates pairwise sequence identity and similarity scores from multiple sequence alignments.
tags: [pseqsid, alignment, sequence-identity, similarity]
author: oxo-call-community
source_url: "https://github.com/amaurypm/pseqsid"
---

## Concepts

- **Tool Overview**: pseqsid measures sequence similarity.
- **Core Function**: Identity calculation.
- **Algorithm**: Uses alignment comparison.
- **Input Format**: Accepts FASTA alignments.
- **Output**: Produces similarity scores.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Data Quality**: Results depend on input quality.
- **Alignment Quality**: Affects scores.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pseqsid --help`
**Explanation:** Shows available options and usage instructions.

### Calculate identity
**Args:** `pseqsid -i alignment.fasta -o scores.txt`
**Explanation:** Computes sequence identity scores.

### With parameters
**Args:** `pseqsid -i alignment.fasta --params params.txt -o scores.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pseqsid -v -i alignment.fasta -o scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pseqsid -t 4 -i alignment.fasta -o scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pseqsid -i alignment.fasta -o scores.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pseqsid -i alignment.fasta -o scores.txt --report report.html`
**Explanation:** Generates HTML report.