---
name: demuxlet
category: expression
description: demuxlet - genetic multiplexing of barcoded single cell RNA-seq.
tags: [demuxlet, expression, single-cell, demultiplexing, rna-seq]
author: oxo-call-community
source_url: "https://github.com/statgen/demuxlet"
---

## Concepts

- **Tool Overview**: demuxlet (v1.0+) is a tool for genetically demultiplexing pooled single-cell RNA-seq samples using natural genetic variation. It assigns cells to individual donors without requiring cell hashing.
- **Core Function**: Uses SNP genotypes from donor samples to assign single cells to their respective donors in pooled scRNA-seq experiments.
- **Input/Output**: Input: BAM/CRAM from scRNA-seq, donor genotype VCF/PLINK. Output: Cell-to-donor assignments, confidence scores, summary statistics.
- **Algorithm**: Uses likelihood-based matching of scRNA-seq reads to donor genotypes to assign cells.
- **Key Features**: Genetic demultiplexing, no cell hashing required, high accuracy, supports pooled experiments, confidence scoring.
- **Installation**: `conda install -c bioconda demuxlet`

## Pitfalls

- **Input Requirements**: Requires donor genotype information and scRNA-seq data.
- **SNP Density**: Performance depends on SNP density in sequencing data.
- **Cell Quality**: Low-quality cells may produce ambiguous assignments.
- **Donor Relatedness**: Related donors may reduce assignment accuracy.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Demultiplex pooled scRNA-seq
**Args:** `demuxlet --plink genotypes --vcf pool.vcf --out assignments`
**Explanation:** Demultiplexes pooled scRNA-seq using genetic variation.

### With BAM input
**Args:** `demuxlet --bam cells.bam --vcf genotypes.vcf --out assignments`
**Explanation:** Use aligned scRNA-seq BAM for demultiplexing.

### With confidence threshold
**Args:** `demuxlet --plink genotypes --vcf pool.vcf --out assignments --confidence 0.9`
**Explanation:** Filter assignments with minimum confidence threshold.