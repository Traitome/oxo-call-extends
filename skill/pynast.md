---
name: pynast
category: alignment
description: PyNAST performs Nearest Alignment Space Termination for sequence alignment.
tags: [pynast, alignment, sequence-analysis, qiime]
author: oxo-call-community
source_url: "http://qiime.org/pynast"
---

## Concepts

- **Tool Overview**: pynast aligns sequences.
- **Core Function**: Sequence alignment.
- **Algorithm**: Uses NAST algorithm.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces alignments.
- **Use Case**: 16S rRNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Database**: Must be current.
- **Sequence Quality**: Affects alignment.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pynast --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `pynast align -i sequences.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** Aligns sequences using reference.

### With parameters
**Args:** `pynast align -i sequences.fasta -p params.yaml -o aligned.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pynast -v align -i sequences.fasta -o aligned.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pynast -t 4 align -i sequences.fasta -o aligned.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Filter alignments
**Args:** `pynast filter -i aligned.fasta -m 0.8 -o filtered.fasta`
**Explanation:** Filters alignments by quality.

### Generate report
**Args:** `pynast align -i sequences.fasta -o aligned.fasta --report report.html`
**Explanation:** Generates HTML report.