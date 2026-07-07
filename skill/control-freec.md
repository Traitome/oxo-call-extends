---
name: control-freec
category: variant-calling
description: Copy number and genotype analysis from WGS and WES data
tags: [control-freec, cnv, copy-number, wgs, wes, genotyping]
author: oxo-call-community
source_url: "https://github.com/BoevaLab/FREEC"
---

## Concepts

- **Tool Overview**: Control-FREEC (FREquency Estimator for C) is a tool for detecting copy number variations and genotypes from whole genome and whole exome sequencing data.
- **Core Function**: Analyzes read depth to identify CNVs, loss of heterozygosity (LOH), and somatic alterations in cancer and germline samples.
- **Algorithm**: Uses read depth ratios, GC-content normalization, and B-allele frequency for CNV and LOH detection.
- **Input**: Aligned sequencing reads in BAM format, reference genome.
- **Output**: Copy number profiles, genotype calls, and CNV regions.
- **Application**: Cancer genomics, CNV detection, and somatic mutation analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda control-freec`

## Pitfalls

- **Coverage Requirements**: Requires sufficient coverage for reliable CNV calling.
- **GC Bias**: GC-content normalization critical for accurate results.
- **Ploidy Assumptions**: Default diploid assumption may not fit all samples.
- **Tumor Purity**: Low tumor purity reduces sensitivity for somatic CNVs.
- **Exome Data**: Exome analysis requires careful interval definition.

## Examples

### Analyze copy number variations
**Args:** `freec -conf config_file.txt`
**Explanation:** Runs FREEC analysis with configuration file.

### Tumor-normal paired analysis
**Args:** `freec -conf config.txt -t tumor.bam -n normal.bam`
**Explanation:** Analyzes tumor-normal pair for somatic CNVs.

### With GC-content correction
**Args:** `freec -conf config.txt -g gc_profile.txt`
**Explanation:** Applies GC-content normalization.

### Display help
**Args:** `freec --help`
**Explanation:** Shows all available options and usage information.