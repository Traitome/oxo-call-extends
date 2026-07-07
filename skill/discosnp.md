---
name: discosnp
category: variant-calling
description: DiscoSnp - SNP discovery from read sets without reference genome.
tags: [discosnp, variant-calling, snp, reference-free, de-bruijn]
author: oxo-call-community
source_url: "https://github.com/GATB/discoSnp"
---

## Concepts

- **Tool Overview**: DiscoSnp is a reference-free SNP discovery tool using de Bruijn graph approach.
- **Core Function**: Discovers SNPs directly from read sets without requiring a reference genome.
- **Input/Output**: Input: FASTQ read files from multiple samples. Output: SNP predictions in VCF format.
- **Algorithm**: Uses de Bruijn graph construction to identify candidate SNPs from k-mer analysis.
- **Key Features**: Reference-free SNP calling, de Bruijn graph approach, population-level SNP discovery, variant filtering, multiple sample support.
- **Installation**: `conda install -c bioconda discosnp`

## Pitfalls

- **Input Requirements**: Requires multiple read sets for comparative SNP discovery.
- **Read Coverage**: Requires sufficient coverage for reliable SNP calling.
- **K-mer Selection**: Appropriate k-mer size selection is critical.
- **False Positives**: May produce false positive SNP calls in repetitive regions.
- **Memory Usage**: High memory requirements for large datasets.

## Examples

### Discover SNPs between samples
**Args:** `discosnp run --reads sample1.fq sample2.fq --output snps.vcf`
**Explanation:** Discovers SNPs between read sets without reference genome.

### With specific k-mer size
**Args:** `discosnp run --reads sample1.fq sample2.fq --kmer 31 --output snps.vcf`
**Explanation:** Use specific k-mer size for SNP discovery.

### Filter by quality
**Args:** `discosnp run --reads sample1.fq sample2.fq --output snps.vcf --min-quality 20`
**Explanation:** Filter SNPs by minimum quality score.

### Population SNP discovery
**Args:** `discosnp run --reads *.fq --output population_snps.vcf`
**Explanation:** Discover SNPs across multiple samples in population.

### Generate statistics
**Args:** `discosnp run --reads sample1.fq sample2.fq --output snps.vcf --stats stats.tsv`
**Explanation:** Generate SNP calling statistics.