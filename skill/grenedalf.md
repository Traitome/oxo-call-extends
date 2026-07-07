---
name: grenedalf
category: bioinformatics
description: grenedalf computes population genetic statistics from pool-sequenced samples, particularly for Evolve and Resequence experiments.
tags: [grenedalf, population-genetics, pool-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lczech/grenedalf"
---

## Concepts

- **Pool-Seq Analysis**: grenedalf analyzes pooled sequencing data for population genetics studies.

- **Evolve and Resequence**: Designed specifically for Evolve and Resequence (E&R) experiments.

- **Population Statistics**: Computes various population genetic statistics including allele frequencies, Fst, and Tajima's D.

- **SNP Calling**: Calls SNPs from pooled sequencing data.

- **Efficiency**: Optimized for large-scale pool-seq datasets.

- **Visualization**: Generates visualizations of population genetic patterns.

## Pitfalls

- **Pool Composition**: Results depend on the composition of pooled samples. Unequal representation can affect statistics.

- **Read Depth**: Ensure sufficient read depth for reliable allele frequency estimation.

- **Population Structure**: Be aware of population structure when interpreting statistics.

- **Computational Resources**: Processing large datasets may require significant memory.

- **Parameter Tuning**: Adjust parameters based on sequencing depth and population size.

## Examples

### Compute allele frequencies
**Args:** `grenedalf freq -i aligned.bam -o frequencies.txt`
**Explanation:** Computes allele frequencies from aligned pool-seq data.

### Calculate Fst
**Args:** `grenedalf fst -i populations.bamlist -o fst.txt`
**Explanation:** Calculates Fst values between populations.

### Call SNPs
**Args:** `grenedalf snp -i aligned.bam -o snps.vcf`
**Explanation:** Calls SNPs from pooled sequencing data.

### Compute Tajima's D
**Args:** `grenedalf tajima -i aligned.bam -o tajima.txt`
**Explanation:** Computes Tajima's D statistic across the genome.

### Batch processing
**Args:** `grenedalf batch -d samples/ -o results/`
**Explanation:** Processes multiple pool-seq samples in a directory.

### Generate visualization
**Args:** `grenedalf plot -i frequencies.txt -o plot.png`
**Explanation:** Creates a visualization of allele frequency patterns.

### Filter low-quality sites
**Args:** `grenedalf filter -i snps.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters SNPs with quality score below 30.