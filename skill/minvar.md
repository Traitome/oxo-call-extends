---
name: minvar
category: variant-calling
description: A tool to detect minority variants in HIV-1 and HCV populations
tags: [minvar, variant-calling, viral]
author: oxo-call-community
source_url: "https://git.io/minvar"
---

## Concepts

- **Tool Overview**: MinVar v2.2.2 detects minority variants in viral populations.
- **Core Function**: Identifies low-frequency variants in HIV-1 and HCV.
- **Viral Variant Calling**: Detects minority variants in viral sequences.
- **Population Genetics**: Analyzes viral population diversity.
- **Input/Output**: Accepts sequencing data; outputs variant calls.
- **Virology Research**: Supports viral evolution and drug resistance studies.

## Pitfalls

- **Virus Specific**: Designed for HIV-1 and HCV analysis.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Calling accuracy depends on input data quality.
- **Frequency Threshold**: Choice of threshold affects sensitivity.

## Examples

### Call minority variants
**Args:** `minvar -i reads.fastq -r reference.fasta -o variants.vcf`
**Explanation:** Detects minority variants in viral sequences.

### With frequency threshold
**Args:** `minvar -i reads.fastq -r reference.fasta -o variants.vcf -t 0.01`
**Explanation:** Uses 1% frequency threshold.

### HIV-specific analysis
**Args:** `minvar -i reads.fastq -r hiv_reference.fasta -o variants.vcf -h`
**Explanation:** Optimized for HIV-1 analysis.

### HCV-specific analysis
**Args:** `minvar -i reads.fastq -r hcv_reference.fasta -o variants.vcf -c`
**Explanation:** Optimized for HCV analysis.

### Generate statistics
**Args:** `minvar -i reads.fastq -r reference.fasta -o variants.vcf -s stats.txt`
**Explanation:** Generates variant calling statistics.