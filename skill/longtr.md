---
name: longtr
category: variant-calling
description: LongTR - Tandem repeat genotyping with long reads
tags: [longtr, variant-calling, tandem-repeats, genotyping, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gymrek-lab/LongTR"
---

## Concepts

- **Tandem Repeat Genotyping**: Genotyping tandem repeat regions
- **Long-read Data**: Using long reads for repeat analysis
- **Repeat Expansion**: Detection of repeat expansions
- **Repeat Length**: Determining repeat unit lengths
- **Genetic Variation**: Analysis of repeat-based genetic variation
- **Complex Loci**: Analysis of complex repeat loci

## Pitfalls

- **Read Quality**: Poor quality reads affect genotyping
- **Repeat Complexity**: Highly complex repeats may be difficult to genotype
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive calls

## Examples

### Genotype repeats
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.vcf`
**Explanation:** Genotypes tandem repeats from long-read data.

### Repeat regions
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.vcf --regions repeats.bed`
**Explanation:** Analyzes specific repeat regions.

### Threads
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum length
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.vcf --min-length 100`
**Explanation:** Filters short repeats.

### Output format
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.json --format json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `longtr --bam input.bam --ref reference.fasta --out repeats.vcf --verbose`
**Explanation:** Provides detailed output.