---
name: pheniqs
category: qc
description: pheniqs classifies barcodes in high-throughput sequencing data.
tags: [pheniqs, qc, barcode, classifier]
author: oxo-call-community
source_url: "http://biosails.github.io/pheniqs"
---

## Concepts

- **Tool Overview**: pheniqs classifies sequencing barcodes.
- **Core Function**: Probabilistic barcode classifier.
- **Algorithm**: Uses noise-aware classification.
- **Input Format**: Accepts FASTQ/BAM/SAM files.
- **Output**: Produces classified sequencing data.
- **Use Case**: Barcode classification, sequencing QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Barcode Quality**: Results depend on barcode quality.
- **Configuration**: Requires proper config setup.
- **Runtime**: Classification may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pheniqs --help`
**Explanation:** Shows available options and usage instructions.

### Classify barcodes
**Args:** `pheniqs -i reads.fastq -c config.yaml -o classified/`
**Explanation:** Classifies barcodes in reads.

### With parameters
**Args:** `pheniqs -i reads.fastq -p params.yaml -o classified/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pheniqs -v -i reads.fastq -c config.yaml -o classified/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pheniqs -t 8 -i reads.fastq -c config.yaml -o classified/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pheniqs -i reads.fastq -c config.yaml -o classified/ --format bam`
**Explanation:** Outputs in BAM format.

### Generate report
**Args:** `pheniqs -i reads.fastq -c config.yaml -o classified/ --report report.html`
**Explanation:** Generates HTML report.