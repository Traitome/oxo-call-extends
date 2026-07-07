---
name: ptrimmer
category: utility
description: ptrimmer trims primer sequences from multiplex amplicon sequencing data.
tags: [ptrimmer, utility, primer-trimming, amplicon-sequencing]
author: oxo-call-community
source_url: "https://github.com/DMU-lilab/pTrimmer"
---

## Concepts

- **Tool Overview**: ptrimmer removes primer sequences.
- **Core Function**: Primer trimming.
- **Algorithm**: Uses sequence matching.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces trimmed reads.
- **Use Case**: Amplicon sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Primer Design**: Affects trimming accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ptrimmer --help`
**Explanation:** Shows available options and usage instructions.

### Trim primers
**Args:** `ptrimmer -i input.fastq -p primers.fasta -o trimmed.fastq`
**Explanation:** Trims primer sequences from reads.

### With parameters
**Args:** `ptrimmer -i input.fastq -p primers.fasta -params params.yaml -o trimmed.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ptrimmer -v -i input.fastq -p primers.fasta -o trimmed.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ptrimmer -t 4 -i input.fastq -p primers.fasta -o trimmed.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Quality trimming
**Args:** `ptrimmer -i input.fastq -p primers.fasta -q 30 -o trimmed.fastq`
**Explanation:** Trims low-quality bases as well.

### Generate report
**Args:** `ptrimmer -i input.fastq -p primers.fasta -o trimmed.fastq --report report.html`
**Explanation:** Generates HTML report.