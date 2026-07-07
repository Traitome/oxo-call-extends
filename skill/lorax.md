---
name: lorax
category: variant-calling
description: Lorax - Long-read analysis toolbox for cancer genomics
tags: [lorax, variant-calling, cancer-genomics, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tobiasrausch/lorax"
---

## Concepts

- **Cancer Genomics**: Analysis of cancer genomic data
- **Long-read Analysis**: Analysis of long-read sequencing data
- **Structural Variants**: Detection of structural variations
- **Copy Number Variation**: Analysis of copy number changes
- **Somatic Mutations**: Detection of somatic mutations
- **Integrative Analysis**: Multi-omics data integration

## Pitfalls

- **Read Quality**: Poor quality reads affect analysis
- **Mapping Quality**: Requires accurate read mapping
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive calls

## Examples

### Run analysis
**Args:** `lorax --bam input.bam --ref reference.fasta --output results/`
**Explanation:** Runs cancer genomics analysis on long reads.

### Detect SVs
**Args:** `lorax --bam input.bam --ref reference.fasta --output sv.vcf --sv`
**Explanation:** Detects structural variants.

### Copy number analysis
**Args:** `lorax --bam input.bam --ref reference.fasta --output cnv.txt --cnv`
**Explanation:** Performs copy number variation analysis.

### Threads
**Args:** `lorax --bam input.bam --ref reference.fasta --output results/ --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `lorax --bam input.bam --ref reference.fasta --output results/ --min-qual 30`
**Explanation:** Filters by minimum quality score.

### Verbose output
**Args:** `lorax --bam input.bam --ref reference.fasta --output results/ --verbose`
**Explanation:** Provides detailed output.