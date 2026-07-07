---
name: prinseq-plus-plus
category: qc
description: prinseq-plus-plus is a multi-threaded C++ sequence cleaning tool.
tags: [prinseq-plus-plus, qc, sequence-cleaning, parallel]
author: oxo-call-community
source_url: "https://github.com/Adrian-Cantu/PRINSEQ-plus-plus"
---

## Concepts

- **Tool Overview**: prinseq-plus-plus cleans sequences.
- **Core Function**: Parallel sequence processing.
- **Algorithm**: Uses multi-threaded methods.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces cleaned sequences.
- **Use Case**: High-throughput sequencing data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Thread Management**: May have overhead issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prinseq++ --help`
**Explanation:** Shows available options and usage instructions.

### Clean sequences
**Args:** `prinseq++ -i reads.fastq -o cleaned.fastq`
**Explanation:** Filters and trims sequence data.

### With parameters
**Args:** `prinseq++ -i reads.fastq -p params.txt -o cleaned.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prinseq++ -v -i reads.fastq -o cleaned.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prinseq++ -t 4 -i reads.fastq -o cleaned.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prinseq++ -i reads.fastq -o cleaned.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `prinseq++ -i reads.fastq -o cleaned.fastq --report report.html`
**Explanation:** Generates HTML report.