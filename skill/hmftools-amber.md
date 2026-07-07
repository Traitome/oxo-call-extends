---
name: hmftools-amber
category: variant-calling
description: Generates a tumor BAF (B-allele frequency) file for use in PURPLE purity/ploidy estimation.
tags: [hmftools-amber, BAF, PURPLE, tumor, copy number]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/amber/README.md"
---

## Concepts

- **B-Allele Frequency (BAF)**: AMBER (v4.2) calculates B-allele frequencies from tumor sequencing data.
- **PURPLE Integration**: Outputs BAF files specifically formatted for PURPLE purity/ploidy estimation.
- **HMF Tools Suite**: Part of the Hartwig Medical Foundation tools suite for cancer genome analysis.
- **Germline SNVs**: Uses germline single-nucleotide variants to calculate BAF values.
- **Copy Number Analysis**: Critical input for accurate copy number profile estimation in tumor samples.

## Pitfalls

- **PURPLE Dependency**: Designed specifically for use with PURPLE; limited standalone utility.
- **Input Requirements**: Requires properly formatted germline VCF and tumor BAM files.
- **Sample Purity**: Results may be unreliable for samples with very low tumor purity.
- **Reference Genome**: Must use consistent reference genome (GRCh38 recommended).
- **Memory Usage**: Processing large genomes may require significant memory resources.

## Examples

### Generate BAF file for PURPLE
**Args:** `amber -t tumor.bam -n normal.vcf -r reference.fasta -o ./output/amber/`
**Explanation:** Generates B-allele frequency data from tumor BAM and germline VCF for PURPLE analysis.

### Run with increased threads
**Args:** `amber -t tumor.bam -n normal.vcf -r reference.fasta -o ./output/amber/ -threads 16`
**Explanation:** Processes BAF calculation with 16 threads for improved performance.

### Specify output prefix
**Args:** `amber -t tumor.bam -n normal.vcf -r reference.fasta -o ./output/amber/ -prefix patient1`
**Explanation:** Generates BAF files with a custom prefix for sample identification.

### Filter by quality
**Args:** `amber -t tumor.bam -n normal.vcf -r reference.fasta -o ./output/amber/ -minQual 30`
**Explanation:** Filters variants by minimum quality score before BAF calculation.

### Run as part of HMF pipeline
**Args:** `nextflow run hmftools/amber --tumor tumor.bam --normal normal.vcf --reference reference.fasta --outdir ./output`
**Explanation:** Executes AMBER as part of the broader HMF analysis pipeline.