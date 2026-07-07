---
name: porfast
category: formatting
description: porfast extracts ORFs from paired-end Illumina reads.
tags: [porfast, formatting, orf, illumina]
author: oxo-call-community
source_url: "https://github.com/telatin/porfast"
---

## Concepts

- **Tool Overview**: porfast finds ORFs in reads.
- **Core Function**: ORF extraction.
- **Algorithm**: Uses pattern matching methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces ORF sequences.
- **Use Case**: Metagenomics, gene prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Frame Detection**: May have frame shifts.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `porfast --help`
**Explanation:** Shows available options and usage instructions.

### Extract ORFs
**Args:** `porfast -i reads_1.fastq -j reads_2.fastq -o orfs.fasta`
**Explanation:** Extracts ORFs from paired-end reads.

### With parameters
**Args:** `porfast -i reads_1.fastq -j reads_2.fastq -p params.yaml -o orfs.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `porfast -v -i reads_1.fastq -j reads_2.fastq -o orfs.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `porfast -t 4 -i reads_1.fastq -j reads_2.fastq -o orfs.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `porfast -i reads_1.fastq -j reads_2.fastq -o orfs.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `porfast -i reads_1.fastq -j reads_2.fastq -o orfs.fasta --report report.html`
**Explanation:** Generates HTML report.