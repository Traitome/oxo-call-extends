---
name: peakhood
category: utility
description: Peakhood extracts site context for CLIP-Seq peak regions.
tags: [peakhood, utility, clip-seq, peak]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/Peakhood"
---

## Concepts

- **Tool Overview**: Peakhood extracts peak context.
- **Core Function**: Analyzes site context around peaks.
- **Algorithm**: Uses context extraction algorithms.
- **Input Format**: Accepts CLIP-seq peak files.
- **Output**: Produces context information.
- **Use Case**: CLIP-seq analysis, binding site context.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large peak sets require memory.
- **Peak Quality**: Results depend on peak quality.
- **Context Definition**: Requires proper context specification.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peakhood --help`
**Explanation:** Shows available options and usage instructions.

### Extract context
**Args:** `peakhood -i peaks.bed -o context.txt`
**Explanation:** Extracts site context for peaks.

### With genome
**Args:** `peakhood -i peaks.bed -g genome.fasta -o context.txt`
**Explanation:** Uses genome for context extraction.

### Verbose mode
**Args:** `peakhood -v -i peaks.bed -o context.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peakhood -t 4 -i peaks.bed -o context.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peakhood -i peaks.bed -o context.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peakhood -i peaks.bed -o context.txt --report report.html`
**Explanation:** Generates HTML report.