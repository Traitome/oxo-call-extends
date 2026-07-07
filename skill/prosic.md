---
name: prosic
category: utility
description: prosic is a Bayesian caller for somatic insertions and deletions.
tags: [prosic, utility, variant-calling, indels]
author: oxo-call-community
source_url: "https://prosic.github.io"
---

## Concepts

- **Tool Overview**: prosic detects somatic indels.
- **Core Function**: Somatic indel calling.
- **Algorithm**: Uses Bayesian methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces variant calls.
- **Use Case**: Cancer genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Detection Sensitivity**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prosic --help`
**Explanation:** Shows available options and usage instructions.

### Call indels
**Args:** `prosic -t tumor.bam -n normal.bam -r reference.fasta -o indels.vcf`
**Explanation:** Calls somatic insertions and deletions.

### With parameters
**Args:** `prosic -t tumor.bam -n normal.bam -r reference.fasta -p params.yaml -o indels.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prosic -v -t tumor.bam -n normal.bam -r reference.fasta -o indels.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prosic -t 4 -t tumor.bam -n normal.bam -r reference.fasta -o indels.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prosic -t tumor.bam -n normal.bam -r reference.fasta -o indels.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `prosic -t tumor.bam -n normal.bam -r reference.fasta -o indels.vcf --report report.html`
**Explanation:** Generates HTML report.