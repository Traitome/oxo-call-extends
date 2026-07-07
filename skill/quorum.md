---
name: quorum
category: qc
description: QuorUM is an error corrector for Illumina sequencing reads, distributed with MaSuRCA or usable independently.
tags: [quorum, qc, error-correction, illumina]
author: oxo-call-community
source_url: "http://www.genome.umd.edu/quorum.html"
---

## Concepts

- **Tool Overview**: quorum corrects sequencing errors.
- **Core Function**: Error correction.
- **Algorithm**: Uses k-mer methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces corrected reads.
- **Use Case**: Preprocessing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **k-mer Size**: Must be configured.
- **Parameters**: Must be set.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quorum --help`
**Explanation:** Shows available options and usage instructions.

### Correct errors
**Args:** `quorum correct -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects sequencing errors.

### With parameters
**Args:** `quorum correct -i reads.fastq -p params.yaml -o corrected.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quorum -v correct -i reads.fastq -o corrected.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quorum -t 4 correct -i reads.fastq -o corrected.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `quorum correct -i reads.fastq -k 31 -o corrected.fastq`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `quorum correct -i reads.fastq -o corrected.fastq --report report.html`
**Explanation:** Generates HTML report.