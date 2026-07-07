---
name: lofreq
category: variant-calling
description: LoFreq - Fast and sensitive variant caller for SNVs and indels from NGS data
tags: [lofreq, variant-calling, SNVs, indels, NGS, bioinformatics]
author: oxo-call-community
source_url: "https://csb5.github.io/lofreq"
---

## Concepts

- **Variant Calling**: Detection of genetic variants from sequencing data
- **SNVs**: Single-nucleotide variant detection
- **Indels**: Insertion and deletion detection
- **Low-Frequency Variants**: Detection of low-frequency variants
- **NGS Data**: Next-generation sequencing data analysis
- **Sensitive Detection**: Sensitive variant detection algorithm

## Pitfalls

- **Read Quality**: Poor quality reads affect variant calling
- **Mapping Quality**: Requires accurate read mapping
- **Coverage Depth**: Requires sufficient coverage depth
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive calls
- **Computational Time**: May be slow for large datasets

## Examples

### Call variants
**Args:** `lofreq call-parallel --pp-threads 4 -f reference.fa -o variants.vcf input.bam`
**Explanation:** Calls low-frequency variants from BAM file using 4 threads.

### Single-threaded mode
**Args:** `lofreq call -f reference.fa -o variants.vcf input.bam`
**Explanation:** Calls variants in single-threaded mode.

### Quality filtering
**Args:** `lofreq call -f reference.fa -o variants.vcf -Q 30 input.bam`
**Explanation:** Filters by minimum base quality of 30.

### Minimum frequency
**Args:** `lofreq call -f reference.fa -o variants.vcf --min-freq 0.01 input.bam`
**Explanation:** Sets minimum variant frequency to 1%.

### Indel calling
**Args:** `lofreq call -f reference.fa -o variants.vcf --call-indels input.bam`
**Explanation:** Enables indel calling.

### Variant filtering
**Args:** `lofreq filter -i variants.vcf -o filtered.vcf --min-cov 10`
**Explanation:** Filters variants by minimum coverage.