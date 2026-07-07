---
name: suma_package
category: sequence-analysis
description: Fast and exact comparison of sequences for metagenomics analysis.
tags: [suma_package, sequence-comparison, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "http://metabarcoding.org/sumatra"
---

## Concepts

- **Tool Overview**: suma_package (v1.0.00) provides fast and exact comparison of sequences for metagenomics.
- **Core Function**: Compares sequences efficiently with exact matching algorithms.
- **Algorithm**: Uses advanced sequence comparison algorithms for fast matching.
- **Input/Output**: Input: FASTA/FASTQ sequences; Output: Comparison results.
- **Applications**: Metagenomics, sequence analysis, barcode comparison.
- **Installation**: `conda install -c bioconda suma_package` or download from website.

## Pitfalls

- **Input Format**: Requires specific sequence format.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Comparison of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect results.
- **Sequence Quality**: Low-quality sequences affect comparison.
- **Duplicate Sequences**: Duplicates may affect analysis.

## Examples

### Display help
**Args:** `suma_package --help`
**Explanation:** Shows available options and usage information.

### Basic sequence comparison
**Args:** `suma_package -i sequences.fasta -o results.txt`
**Explanation:** Compare sequences with default parameters.

### With custom threshold
**Args:** `suma_package -i sequences.fasta -o results.txt -t 0.95`
**Explanation:** Compare sequences with 95% identity threshold.

### Verbose mode
**Args:** `suma_package -i sequences.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `suma_package -i sequences.fasta -o results.txt --stats`
**Explanation:** Generate statistics about comparison.

### Batch processing
**Args:** `suma_package -i fastas/ -o results/`
**Explanation:** Process multiple FASTA files together.

### Filter by length
**Args:** `suma_package -i sequences.fasta -o results.txt -m 100`
**Explanation:** Minimum sequence length of 100.

### Include alignment
**Args:** `suma_package -i sequences.fasta -o results.txt --align`
**Explanation:** Include alignment information in output.

### Generate report
**Args:** `suma_package -i sequences.fasta -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
