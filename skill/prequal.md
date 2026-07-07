---
name: prequal
category: alignment
description: prequal is a pre-alignment quality filter for comparative sequence analyses.
tags: [prequal, alignment, quality-filter, sequences]
author: oxo-call-community
source_url: "https://github.com/simonwhelan/prequal"
---

## Concepts

- **Tool Overview**: prequal filters sequences before alignment.
- **Core Function**: Pre-alignment quality filtering.
- **Algorithm**: Uses quality-based methods.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces filtered sequences.
- **Use Case**: Comparative genomics, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Filtering Stringency**: May affect downstream analysis.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prequal --help`
**Explanation:** Shows available options and usage instructions.

### Filter sequences
**Args:** `prequal -i input.fasta -o filtered.fasta`
**Explanation:** Filters sequences before alignment.

### With parameters
**Args:** `prequal -i input.fasta -p params.yaml -o filtered.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prequal -v -i input.fasta -o filtered.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prequal -t 4 -i input.fasta -o filtered.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prequal -i input.fasta -o filtered.fastq --fastq`
**Explanation:** Outputs in FASTQ format.

### Generate report
**Args:** `prequal -i input.fasta -o filtered.fasta --report report.html`
**Explanation:** Generates HTML report.