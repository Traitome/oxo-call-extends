---
name: quake
category: containerization
description: Quake corrects substitution sequencing errors in deep coverage sequencing experiments, specifically for Illumina reads.
tags: [quake, containerization, error-correction, sequencing]
author: oxo-call-community
source_url: "http://www.cbcb.umd.edu/software/quake/"
---

## Concepts

- **Tool Overview**: quake corrects sequencing errors.
- **Core Function**: Error correction.
- **Algorithm**: Uses k-mer frequency.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces corrected reads.
- **Use Case**: Preprocessing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Coverage**: Must be high (>15X).
- **k-mer Size**: Must be set.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quake --help`
**Explanation:** Shows available options and usage instructions.

### Correct errors
**Args:** `quake correct -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects sequencing errors.

### With parameters
**Args:** `quake correct -i reads.fastq -p params.yaml -o corrected.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quake -v correct -i reads.fastq -o corrected.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quake -t 4 correct -i reads.fastq -o corrected.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `quake correct -i reads.fastq -k 21 -o corrected.fastq`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `quake correct -i reads.fastq -o corrected.fastq --report report.html`
**Explanation:** Generates HTML report.