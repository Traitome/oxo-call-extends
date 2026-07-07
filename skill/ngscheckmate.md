---
name: ngscheckmate
category: utility
description: NGSCheckMate identifies NGS data files from the same individual using SNP profiles.
tags: [ngscheckmate, utility, sample-identity, snp]
author: oxo-call-community
source_url: "https://github.com/parklab/NGSCheckMate"
---

## Concepts

- **Tool Overview**: NGSCheckMate verifies sample identity across sequencing runs.
- **Core Function**: Compares SNP profiles to identify duplicate or mislabeled samples.
- **Algorithm**: Uses SNP-based fingerprinting to compare samples.
- **Input Format**: Accepts BAM, VCF, or FASTQ files.
- **Output**: Produces identity verification reports.
- **Use Case**: Sample tracking, quality control, and data management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Genome**: Requires matching reference genome.
- **SNP Density**: Results depend on SNP coverage.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Comparison can be computationally intensive.
- **False Positives**: May produce false matches with related samples.

## Examples

### Display help
**Args:** `ngscheckmate --help`
**Explanation:** Shows available options and usage instructions.

### Check sample identity
**Args:** `ngscheckmate -i bam_list.txt -o results/`
**Explanation:** Compares BAM files for sample identity.

### Using VCF input
**Args:** `ngscheckmate -v vcf_list.txt -o results/`
**Explanation:** Uses VCF files for comparison.

### FASTQ input
**Args:** `ngscheckmate -f fastq_list.txt -r reference.fasta -o results/`
**Explanation:** Processes FASTQ files directly.

### Output report
**Args:** `ngscheckmate -i bam_list.txt -o results/ --report`
**Explanation:** Generates detailed report.

### Threads
**Args:** `ngscheckmate -i bam_list.txt -o results/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Threshold setting
**Args:** `ngscheckmate -i bam_list.txt -o results/ -c 0.95`
**Explanation:** Sets confidence threshold to 0.95.