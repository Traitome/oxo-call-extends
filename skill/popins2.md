---
name: popins2
category: variant-calling
description: popins2 detects non-reference sequence variants using de Bruijn graphs.
tags: [popins2, variant-calling, de-bruijn, population]
author: oxo-call-community
source_url: "https://github.com/kehrlab/PopIns2"
---

## Concepts

- **Tool Overview**: popins2 identifies non-reference variants.
- **Core Function**: Population-scale variant detection.
- **Algorithm**: Uses colored de Bruijn graphs.
- **Input Format**: Accepts FASTA/VCF files.
- **Output**: Produces variant calls.
- **Use Case**: Population genetics, pan-genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large graphs require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Detection Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `popins2 --help`
**Explanation:** Shows available options and usage instructions.

### Detect variants
**Args:** `popins2 detect -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Detects non-reference sequence variants.

### With parameters
**Args:** `popins2 detect -i reads.fastq -r reference.fasta -p params.yaml -o variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `popins2 -v detect -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `popins2 -t 4 detect -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `popins2 detect -i reads.fastq -r reference.fasta -o variants.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `popins2 detect -i reads.fastq -r reference.fasta -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.