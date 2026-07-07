---
name: peekseq
category: utility
description: peekseq calculates protein-coding potential using k-mer approach.
tags: [peekseq, utility, coding-potential, k-mer]
author: oxo-call-community
source_url: "https://github.com/BirolLab/peekseq"
---

## Concepts

- **Tool Overview**: peekseq predicts coding potential.
- **Core Function**: Calculates protein-coding potential.
- **Algorithm**: Uses k-mer frequency analysis.
- **Input Format**: Accepts sequence files.
- **Output**: Produces coding potential scores.
- **Use Case**: Gene prediction, transcript analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **K-mer Selection**: K-mer size affects accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peekseq --help`
**Explanation:** Shows available options and usage instructions.

### Calculate coding potential
**Args:** `peekseq -i sequences.fasta -o coding_scores.txt`
**Explanation:** Calculates coding potential scores.

### With k-mer size
**Args:** `peekseq -i sequences.fasta -k 6 -o coding_scores.txt`
**Explanation:** Uses 6-mer for analysis.

### Verbose mode
**Args:** `peekseq -v -i sequences.fasta -o coding_scores.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peekseq -t 4 -i sequences.fasta -o coding_scores.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peekseq -i sequences.fasta -o coding_scores.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peekseq -i sequences.fasta -o coding_scores.txt --report report.html`
**Explanation:** Generates HTML report.