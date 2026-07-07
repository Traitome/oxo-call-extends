---
name: quickdeconvolution
category: utility
description: QuickDeconvolution deconvolves linked-reads sequencing data for improved analysis.
tags: [quickdeconvolution, utility, linked-reads, sequencing]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/QuickDeconvolution"
---

## Concepts

- **Tool Overview**: quickdeconvolution deconvolves data.
- **Core Function**: Linked-read analysis.
- **Algorithm**: Uses computational methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces deconvolved data.
- **Use Case**: Sequencing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects results.
- **Parameters**: Must be configured.
- **Runtime**: Deconvolution may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quickdeconvolution --help`
**Explanation:** Shows available options and usage instructions.

### Run deconvolution
**Args:** `quickdeconvolution run -i reads.fastq -o deconvolved.fastq`
**Explanation:** Deconvolves linked-reads.

### With parameters
**Args:** `quickdeconvolution run -i reads.fastq -p params.yaml -o deconvolved.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quickdeconvolution -v run -i reads.fastq -o deconvolved.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quickdeconvolution -t 4 run -i reads.fastq -o deconvolved.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With barcode file
**Args:** `quickdeconvolution run -i reads.fastq -b barcodes.txt -o deconvolved.fastq`
**Explanation:** Uses barcode information.

### Generate report
**Args:** `quickdeconvolution run -i reads.fastq -o deconvolved.fastq --report report.html`
**Explanation:** Generates HTML report.