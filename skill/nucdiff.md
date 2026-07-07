---
name: nucdiff
category: utility
description: NucDiff locates and categorizes differences between two closely related nucleotide sequences.
tags: [nucdiff, utility, sequence-comparison, variant-detection]
author: oxo-call-community
source_url: "https://github.com/uio-cels/NucDiff"
---

## Concepts

- **Tool Overview**: NucDiff compares and identifies differences between nucleotide sequences.
- **Core Function**: Detects and categorizes sequence variations.
- **Algorithm**: Uses alignment-based comparison for variant detection.
- **Input Format**: Accepts FASTA sequences or aligned files.
- **Output**: Produces variant calls and difference reports.
- **Use Case**: Sequence comparison, variant analysis, and genome comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Sequence Similarity**: Works best for closely related sequences.
- **Memory Usage**: Large sequences require memory.
- **Computational Cost**: Comparison can be computationally intensive.
- **Alignment Quality**: Results depend on input alignment quality.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nucdiff --help`
**Explanation:** Shows available options and usage instructions.

### Compare sequences
**Args:** `nucdiff -r reference.fasta -q query.fasta -o differences.txt`
**Explanation:** Compares query to reference sequence.

### Output VCF
**Args:** `nucdiff -r reference.fasta -q query.fasta -o variants.vcf --vcf`
**Explanation:** Outputs variants in VCF format.

### Detailed report
**Args:** `nucdiff -r reference.fasta -q query.fasta -o report.txt --detailed`
**Explanation:** Generates detailed difference report.

### Ignore gaps
**Args:** `nucdiff -r reference.fasta -q query.fasta -o differences.txt --ignore-gaps`
**Explanation:** Ignores gap positions in comparison.

### Threads
**Args:** `nucdiff -r reference.fasta -q query.fasta -t 8 -o differences.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nucdiff -r reference.fasta -q query.fasta -v -o differences.txt`
**Explanation:** Runs with verbose output.