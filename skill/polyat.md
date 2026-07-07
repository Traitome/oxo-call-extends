---
name: polyat
category: variant-calling
description: polyat quantifies poly-A/T homopolymers in sequencing reads.
tags: [polyat, variant-calling, homopolymer, sequencing]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/polyat"
---

## Concepts

- **Tool Overview**: polyat analyzes homopolymer sequences.
- **Core Function**: Poly-A/T homopolymer quantification.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts FASTQ sequencing reads.
- **Output**: Produces homopolymer statistics.
- **Use Case**: Sequencing quality control, variant analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Homopolymer Detection**: May have detection errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `polyat --help`
**Explanation:** Shows available options and usage instructions.

### Quantify homopolymers
**Args:** `polyat -i reads.fastq -o results/`
**Explanation:** Quantifies poly-A/T homopolymers.

### With parameters
**Args:** `polyat -i reads.fastq -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `polyat -v -i reads.fastq -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `polyat -t 4 -i reads.fastq -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `polyat -i reads.fastq -o results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `polyat -i reads.fastq -o results/ --report report.html`
**Explanation:** Generates HTML report.