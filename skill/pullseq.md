---
name: pullseq
category: formatting
description: pullseq extracts sequences from FASTA/FASTQ files based on various criteria.
tags: [pullseq, formatting, sequence-extraction, FASTA]
author: oxo-call-community
source_url: "https://github.com/bcthomas/pullseq"
---

## Concepts

- **Tool Overview**: pullseq extracts sequences.
- **Core Function**: Sequence extraction.
- **Algorithm**: Uses pattern matching.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces extracted sequences.
- **Use Case**: Sequence filtering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Pattern Complexity**: May affect performance.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pullseq --help`
**Explanation:** Shows available options and usage instructions.

### Extract by length
**Args:** `pullseq -i input.fasta -m 100 -M 500 -o output.fasta`
**Explanation:** Extracts sequences between 100-500 bp.

### Extract by id
**Args:** `pullseq -i input.fasta -n "gene*" -o output.fasta`
**Explanation:** Extracts sequences matching name pattern.

### Extract by pattern
**Args:** `pullseq -i input.fasta -p "ATG*" -o output.fasta`
**Explanation:** Extracts sequences matching pattern.

### Verbose mode
**Args:** `pullseq -v -i input.fasta -m 100 -o output.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pullseq -t 4 -i input.fasta -m 100 -o output.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `pullseq -i input.fasta -m 100 -o output.fasta --report report.html`
**Explanation:** Generates HTML report.