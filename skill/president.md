---
name: president
category: utility
description: president calculates pairwise nucleotide identity with respect to a reference.
tags: [president, utility, identity, comparison]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/president"
---

## Concepts

- **Tool Overview**: president compares sequences.
- **Core Function**: Nucleotide identity calculation.
- **Algorithm**: Uses alignment-based methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces identity scores.
- **Use Case**: Sequence comparison, phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May affect identity scores.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `president --help`
**Explanation:** Shows available options and usage instructions.

### Calculate identity
**Args:** `president -r reference.fasta -i query.fasta -o identity.txt`
**Explanation:** Calculates pairwise nucleotide identity.

### With parameters
**Args:** `president -r reference.fasta -i query.fasta -p params.yaml -o identity.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `president -v -r reference.fasta -i query.fasta -o identity.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `president -t 4 -r reference.fasta -i query.fasta -o identity.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `president -r reference.fasta -i query.fasta -o identity.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `president -r reference.fasta -i query.fasta -o identity.txt --report report.html`
**Explanation:** Generates HTML report.