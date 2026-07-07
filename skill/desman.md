---
name: desman
category: metagenomics
description: DESMAN - de novo extraction of strains from metagenomes.
tags: [desman, metagenomics, strain, deconvolution, binning]
author: oxo-call-community
source_url: "https://github.com/chrisquince/DESMAN"
---

## Concepts

- **Tool Overview**: desman (v2.1+) is a tool for de novo extraction of individual strain genomes from metagenomic data. It resolves strain-level variation within metagenomic bins.
- **Core Function**: Uses SNP patterns and abundance information to separate closely related strains within metagenomic assemblies, enabling strain-resolved genomic analysis.
- **Input/Output**: Input: BAM files with mapped reads, metagenomic bins (MAGs). Output: Strain-resolved genomes, variant profiles, abundance estimates.
- **Algorithm**: Uses statistical models to cluster reads by strain based on SNP patterns and coverage variations.
- **Key Features**: Strain-level resolution, de novo extraction, SNP-based clustering, abundance estimation, visualization support.
- **Installation**: `conda install -c bioconda desman`

## Pitfalls

- **Input Requirements**: Requires mapped reads and high-quality metagenomic bins.
- **Strain Similarity**: May struggle with very closely related strains.
- **Coverage Depth**: Requires sufficient coverage for strain separation.
- **Computational Resources**: May require significant computational resources.
- **Bin Quality**: Results depend on the quality of input metagenomic bins.

## Examples

### Extract strain genomes from metagenome
**Args:** `desman --bam mapping.bam --bins bins/ --output strains/`
**Explanation:** Extracts strain genomes from metagenomic bins.

### With variant calling
**Args:** `desman --bam mapping.bam --bins bins/ --output strains/ --call-variants`
**Explanation:** Call variants during strain extraction.

### Generate visualization
**Args:** `desman --bam mapping.bam --bins bins/ --output strains/ --plot strains.png`
**Explanation:** Generate visualization of strain relationships.