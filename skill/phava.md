---
name: phava
category: qc
description: phava detects invertons from long-read sequencing datasets.
tags: [phava, qc, invertons, long-read]
author: oxo-call-community
source_url: "https://github.com/patrickwest/PhaVa"
---

## Concepts

- **Tool Overview**: phava detects genomic inversions.
- **Core Function**: Identifies invertons in reads.
- **Algorithm**: Uses long-read analysis methods.
- **Input Format**: Accepts long-read sequencing data.
- **Output**: Produces inversion detection results.
- **Use Case**: Inversion detection, long-read QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on read quality.
- **Inversion Detection**: May miss complex inversions.
- **Runtime**: Detection may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phava --help`
**Explanation:** Shows available options and usage instructions.

### Detect invertons
**Args:** `phava -i long_reads.fastq -o inversions.txt`
**Explanation:** Detects invertons from long reads.

### With reference
**Args:** `phava -i long_reads.fastq -r ref.fasta -o inversions.txt`
**Explanation:** Uses specific reference genome.

### Verbose mode
**Args:** `phava -v -i long_reads.fastq -o inversions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phava -t 4 -i long_reads.fastq -o inversions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phava -i long_reads.fastq -o inversions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phava -i long_reads.fastq -o inversions.txt --report report.html`
**Explanation:** Generates HTML report.