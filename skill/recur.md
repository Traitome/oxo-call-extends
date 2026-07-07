---
name: recur
category: alignment
description: RECUR detects recurrent amino-acid substitutions from multiple-sequence alignments for evolutionary analysis.
tags: [recur, alignment, recurrent-substitutions, evolutionary-analysis]
author: oxo-call-community
source_url: "https://orthofinder.github.io/RECUR"
---

## Concepts

- **Tool Overview**: recur detects substitutions.
- **Core Function**: Recurrent substitution detection.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts MSA files.
- **Output**: Produces substitution patterns.
- **Use Case**: Evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recur --help`
**Explanation:** Shows available options and usage instructions.

### Detect substitutions
**Args:** `recur detect -i alignment.fasta -o substitutions.txt`
**Explanation:** Detects recurrent substitutions.

### With parameters
**Args:** `recur detect -i alignment.fasta -p params.yaml -o substitutions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recur -v detect -i alignment.fasta -o substitutions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recur -t 4 detect -i alignment.fasta -o substitutions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With phylogenetic tree
**Args:** `recur detect -i alignment.fasta -t tree.newick -o substitutions.txt`
**Explanation:** Uses phylogenetic tree.

### Generate report
**Args:** `recur detect -i alignment.fasta -o substitutions.txt --report report.html`
**Explanation:** Generates HTML report.