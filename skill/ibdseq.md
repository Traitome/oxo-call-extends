---
name: ibdseq
category: population-genomics
description: IBDseq detects segments of Identity-by-Descent (IBD) and Homozygosity-by-Descent (HBD) in unphased genetic sequence data.
tags: [ibdseq, population-genomics, IBD, HBD, genetic-analysis]
author: oxo-call-community
source_url: "http://faculty.washington.edu/browning/ibdseq.html"
---

## Concepts

- **Tool Overview**: IBDseq (vr1206) is a software program for detecting IBD and HBD segments in unphased genotype data, part of the Browning lab suite of genetic analysis tools.
- **Identity-by-Descent (IBD)**: Segments of DNA inherited identically from a common ancestor, indicating recent shared ancestry.
- **Homozygosity-by-Descent (HBD)**: Runs of homozygosity resulting from inheritance of the same ancestral segment from both parents (autozygosity).
- **Unphased Data Support**: Can analyze unphased genotype data without requiring prior phasing, making it widely applicable.
- **Population Scale**: Designed for large-scale population studies and biobank data analysis.
- **Installation**: `conda install -c bioconda ibdseq`

## Pitfalls

- **Genotyping Error Sensitivity**: High error rates can lead to false IBD/HBD calls.
- **Missing Data**: Requires relatively complete genotype data; excessive missingness reduces detection power.
- **Marker Density**: Performance improves with higher marker density (e.g., whole-genome sequencing vs SNP arrays).
- **Population Specificity**: Parameters may need adjustment for different populations with varying linkage disequilibrium patterns.
- **Computational Time**: Memory and time requirements increase quadratically with sample size.
- **Segment Length Cutoff**: Default thresholds may not be optimal for all datasets; parameter tuning recommended.

## Examples

### Detect IBD segments in VCF file
**Args:** `ibdseq --vcf input.vcf --out ibdseq_results`
**Explanation:** Detects IBD segments from VCF format genotype data.

### Include HBD detection
**Args:** `ibdseq --vcf input.vcf --hbd --out ibdseq_results`
**Explanation:** Enables detection of Homozygosity-by-Descent segments in addition to IBD.

### Set minimum segment length
**Args:** `ibdseq --vcf input.vcf --min-cm 1.0 --out ibdseq_results`
**Explanation:** Filters IBD segments to only include those longer than 1.0 centimorgan.

### Use multiple threads
**Args:** `ibdseq --vcf input.vcf --threads 16 --out ibdseq_results`
**Explanation:** Utilizes 16 threads for parallel processing to accelerate analysis.

### Generate segment statistics
**Args:** `ibdseq --vcf input.vcf --stats --out ibdseq_results`
**Explanation:** Produces summary statistics including segment counts and mean lengths.