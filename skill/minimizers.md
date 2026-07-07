---
name: minimizers
category: programming
description: Minimizers extraction from fasta files.
tags: [minimizers, programming, sequence]
author: oxo-call-community
source_url: "https://github.com/cumbof/minimizers"
---

## Concepts

- **Tool Overview**: minimizers v0.1.2 extracts minimizers from FASTA files.
- **Core Function**: Identifies minimizers in sequence data.
- **Minimizer Selection**: Chooses representative k-mers from sequences.
- **Sequence Indexing**: Supports efficient sequence indexing.
- **Input/Output**: Accepts FASTA files; outputs minimizer positions.
- **k-mer Analysis**: Supports k-mer based sequence analysis.

## Pitfalls

- **FASTA Specific**: Designed for FASTA format input.
- **Computational Resources**: Processing large sequences may require significant resources.
- **Memory Requirements**: Memory usage depends on sequence length.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **k-mer Selection**: Choice of k-mer size affects results.
- **Data Quality**: Results depend on input sequence quality.

## Examples

### Extract minimizers
**Args:** `minimizers -i input.fasta -o minimizers.txt`
**Explanation:** Extracts minimizers from FASTA file.

### With custom k-mer size
**Args:** `minimizers -i input.fasta -o minimizers.txt -k 21`
**Explanation:** Uses k-mer size of 21.

### Batch processing
**Args:** `minimizers -i fasta/ -o minimizers/`
**Explanation:** Processes multiple FASTA files.

### Detailed output
**Args:** `minimizers -i input.fasta -o minimizers.txt -v`
**Explanation:** Generates detailed minimizer report.

### With window size
**Args:** `minimizers -i input.fasta -o minimizers.txt -w 50`
**Explanation:** Uses window size of 50 for minimizer selection.