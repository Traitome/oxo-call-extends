---
name: pizzly
category: utility
description: pizzly detects gene fusions using kallisto.
tags: [pizzly, utility, fusion, kallisto]
author: oxo-call-community
source_url: "https://github.com/pmelsted/pizzly"
---

## Concepts

- **Tool Overview**: pizzly detects gene fusions.
- **Core Function**: Fusion transcript detection.
- **Algorithm**: Uses kallisto-based methods.
- **Input Format**: Accepts RNA-seq data files.
- **Output**: Produces fusion detection results.
- **Use Case**: Cancer genomics, fusion detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on data quality.
- **Fusion Detection**: May have false positives/negatives.
- **Runtime**: Detection may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pizzly --help`
**Explanation:** Shows available options and usage instructions.

### Detect fusions
**Args:** `pizzly -i rna_seq_data.fastq -o fusions.txt`
**Explanation:** Detects gene fusions using kallisto.

### With parameters
**Args:** `pizzly -i rna_seq_data.fastq -p params.yaml -o fusions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pizzly -v -i rna_seq_data.fastq -o fusions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pizzly -t 4 -i rna_seq_data.fastq -o fusions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pizzly -i rna_seq_data.fastq -o fusions.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `pizzly -i rna_seq_data.fastq -o fusions.txt --report report.html`
**Explanation:** Generates HTML report.