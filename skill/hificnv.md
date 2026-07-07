---
name: hificnv
category: bioinformatics
description: HiFiCNV calls copy number variants and provides depth visualization for PacBio HiFi reads.
tags: [hificnv, CNV-calling, PacBio, HiFi, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/HiFiCNV"
---

## Concepts

- **Copy Number Variation**: HiFiCNV identifies copy number variants.

- **PacBio HiFi**: Optimized for PacBio HiFi sequencing data.

- **Depth Analysis**: Analyzes sequencing depth.

- **Visualization**: Provides visualization of CNV results.

- **Variant Calling**: Calls structural variants.

- **Genomic Analysis**: Analyzes genomic copy number.

## Pitfalls

- **Data Quality**: Results depend on sequencing data quality.

- **Reference Genome**: Requires appropriate reference genome.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Call CNVs
**Args:** `hificnv --input reads.bam --output cnv.vcf`
**Explanation:** Calls copy number variants from HiFi reads.

### With visualization
**Args:** `hificnv --input reads.bam --output cnv.vcf --plot`
**Explanation:** Generates CNV calls and visualization.

### Batch processing
**Args:** `for f in *.bam; do hificnv --input $f --output ${f%.bam}_cnv.vcf; done`
**Explanation:** Processes multiple BAM files.

### Generate report
**Args:** `hificnv --input reads.bam --output cnv.vcf --report`
**Explanation:** Generates comprehensive CNV report.

### Help command
**Args:** `hificnv --help`
**Explanation:** Shows available options and usage information.