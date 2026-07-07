---
name: longshot
category: variant-calling
description: Longshot - Diploid SNV caller for error-prone reads
tags: [longshot, variant-calling, SNVs, error-prone, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pjedge/longshot"
---

## Concepts

- **SNV Calling**: Single-nucleotide variant detection
- **Diploid Calling**: Diploid genotype calling
- **Error-Prone Reads**: Handling high-error-rate sequencing data
- **Long-read Data**: Analysis of long-read sequencing data
- **Bayesian Calling**: Bayesian variant calling approach
- **Haplotype Phasing**: Integrated haplotype phasing

## Pitfalls

- **Read Quality**: Poor quality reads affect variant calling
- **Mapping Quality**: Requires accurate read mapping
- **Error Rate**: High error rates may affect accuracy
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **False Positives**: May produce false positive calls

## Examples

### Call variants
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf`
**Explanation:** Calls SNVs from long-read data.

### Phasing
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf --phase`
**Explanation:** Performs haplotype phasing.

### Threads
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf --min-qual 30`
**Explanation:** Filters by minimum quality score.

### Error rate
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf --error-rate 0.1`
**Explanation:** Sets expected error rate to 10%.

### Verbose output
**Args:** `longshot --bam input.bam --ref reference.fasta --out variants.vcf --verbose`
**Explanation:** Provides detailed output.