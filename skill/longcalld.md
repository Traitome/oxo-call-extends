---
name: longcalld
category: variant-calling
description: longcallD - Local-haplotagging-based small and structural variant calling
tags: [longcalld, variant-calling, haplotagging, structural-variants, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/yangao07/longcallD"
---

## Concepts

- **Variant Calling**: Detection of genetic variants
- **Haplotagging**: Local haplotype-based variant analysis
- **Structural Variants**: Detection of structural variations
- **Small Variants**: Detection of small genetic variants
- **Long Reads**: Analysis of long-read sequencing data
- **Haplotype Phasing**: Determining haplotype phase

## Pitfalls

- **Read Quality**: Poor quality reads affect variant calling
- **Mapping Quality**: Requires accurate read mapping
- **Coverage Depth**: Requires sufficient coverage depth
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive calls

## Examples

### Call variants
**Args:** `longcalld --bam input.bam --ref reference.fasta --output variants.vcf`
**Explanation:** Calls variants from BAM file.

### Small variants
**Args:** `longcalld --bam input.bam --ref reference.fasta --output variants.vcf --small`
**Explanation:** Focuses on small variant calling.

### Structural variants
**Args:** `longcalld --bam input.bam --ref reference.fasta --output sv.vcf --structural`
**Explanation:** Focuses on structural variant calling.

### Threads
**Args:** `longcalld --bam input.bam --ref reference.fasta --output variants.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `longcalld --bam input.bam --ref reference.fasta --output variants.vcf --min-qual 30`
**Explanation:** Filters by minimum quality score.

### Verbose output
**Args:** `longcalld --bam input.bam --ref reference.fasta --output variants.vcf --verbose`
**Explanation:** Provides detailed output.