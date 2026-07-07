---
name: prinseq
category: qc
description: prinseq filters, reformats, and trims genomic and metagenomic sequence data.
tags: [prinseq, qc, sequence-cleaning, filtering]
author: oxo-call-community
source_url: "http://prinseq.sourceforge.net/"
---

## Concepts

- **Tool Overview**: prinseq processes sequence data.
- **Core Function**: Quality control and cleaning.
- **Algorithm**: Uses quality-based filtering methods.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces cleaned sequences.
- **Use Case**: Preprocessing, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Filtering Stringency**: May affect downstream analysis.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prinseq-lite.pl --help`
**Explanation:** Shows available options and usage instructions.

### Clean sequences
**Args:** `prinseq-lite.pl -i reads.fastq -o cleaned.fastq`
**Explanation:** Filters and trims sequence data.

### With parameters
**Args:** `prinseq-lite.pl -i reads.fastq -p params.txt -o cleaned.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prinseq-lite.pl -v -i reads.fastq -o cleaned.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prinseq-lite.pl -t 4 -i reads.fastq -o cleaned.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prinseq-lite.pl -i reads.fastq -o cleaned.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `prinseq-lite.pl -i reads.fastq -o cleaned.fastq --report report.html`
**Explanation:** Generates HTML report.