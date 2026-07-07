---
name: rcorrector
category: expression
description: Rcorrector (RNA-seq error CORRECTOR) is a k-mer-based error correction method for RNA-seq data with non-uniform coverage.
tags: [rcorrector, expression, error-correction, rna-seq]
author: oxo-call-community
source_url: "https://github.com/mourisl/Rcorrector/blob/v1.0.7/README.md"
---

## Concepts

- **Tool Overview**: rcorrector corrects errors.
- **Core Function**: RNA-seq error correction.
- **Algorithm**: Uses k-mer methods.
- **Input Format**: Accepts RNA-seq reads.
- **Output**: Produces corrected reads.
- **Use Case**: Transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Coverage**: Affects correction.
- **Parameters**: Must be configured.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rcorrector --help`
**Explanation:** Shows available options and usage instructions.

### Correct reads
**Args:** `rcorrector correct -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects RNA-seq errors.

### With parameters
**Args:** `rcorrector correct -i reads.fastq -p params.yaml -o corrected.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rcorrector -v correct -i reads.fastq -o corrected.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rcorrector -t 4 correct -i reads.fastq -o corrected.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `rcorrector correct -i reads.fastq -k 23 -o corrected.fastq`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `rcorrector correct -i reads.fastq -o corrected.fastq --report report.html`
**Explanation:** Generates HTML report.