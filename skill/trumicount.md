---
name: trumicount
category: analysis
description: TruMiCount - Tool for estimating tumor mutational burden from targeted sequencing.
tags: [trumicount, tmb, tumor-mutational-burden, cancer, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/trumicount"
---

## Concepts

- **Tool Overview**: TruMiCount - A tool for estimating tumor mutational burden from targeted sequencing data.
- **Core Function**: Calculates TMB (Tumor Mutational Burden) from variant calls.
- **Input**: VCF files, BED files with target regions.
- **Output**: TMB estimates, confidence intervals, quality metrics.
- **Installation**: `pip install trumicount` or `conda install -c bioconda trumicount`
- **Use Case**: Cancer genomics, immunotherapy response prediction, clinical research.

## Pitfalls

- **Target Coverage**: Requires adequate coverage depth.
- **Variant Quality**: Results depend on variant calling quality.

## Examples

### Calculate TMB
**Args:** `trumicount -i variants.vcf -t targets.bed -o tmb.txt`
**Explanation:** Calculate tumor mutational burden from variants.

### With confidence intervals
**Args:** `trumicount -i vcf/ -t targets.bed -c -o tmb_estimates/`
**Explanation:** Calculate TMB with confidence intervals.
