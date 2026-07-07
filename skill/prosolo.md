---
name: prosolo
category: variant-calling
description: prosolo is a Bayesian caller for variants in single cell sequencing data.
tags: [prosolo, variant-calling, single-cell, bayesian]
author: oxo-call-community
source_url: "https://github.com/prosolo/prosolo/tree/v0.6.1"
---

## Concepts

- **Tool Overview**: prosolo calls variants in single cells.
- **Core Function**: Single-cell variant calling.
- **Algorithm**: Uses Bayesian methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces variant calls.
- **Use Case**: Single-cell genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Allele Dropout**: May affect calling.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prosolo --help`
**Explanation:** Shows available options and usage instructions.

### Call variants
**Args:** `prosolo -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants in single cell data.

### With parameters
**Args:** `prosolo -i aligned.bam -r reference.fasta -p params.yaml -o variants.vcf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prosolo -v -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prosolo -t 4 -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prosolo -i aligned.bam -r reference.fasta -o variants.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `prosolo -i aligned.bam -r reference.fasta -o variants.vcf --report report.html`
**Explanation:** Generates HTML report.