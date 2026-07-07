---
name: porechop
category: qc
description: porechop removes adapters and demultiplexes Oxford Nanopore reads.
tags: [porechop, qc, nanopore, adapter-trimming]
author: oxo-call-community
source_url: "https://github.com/rrwick/Porechop"
---

## Concepts

- **Tool Overview**: porechop processes nanopore sequencing data.
- **Core Function**: Adapter removal and demultiplexing.
- **Algorithm**: Uses sequence alignment methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces trimmed reads.
- **Use Case**: Nanopore data preprocessing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Adapter Detection**: May miss some adapters.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `porechop --help`
**Explanation:** Shows available options and usage instructions.

### Trim adapters
**Args:** `porechop -i reads.fastq -o trimmed.fastq`
**Explanation:** Removes adapters from nanopore reads.

### With parameters
**Args:** `porechop -i reads.fastq -p params.yaml -o trimmed.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `porechop -v -i reads.fastq -o trimmed.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `porechop -t 4 -i reads.fastq -o trimmed.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `porechop -i reads.fastq -o trimmed.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `porechop -i reads.fastq -o trimmed.fastq --report report.html`
**Explanation:** Generates HTML report.