---
name: titan-gc
category: analysis
description: Titan-GC - Genomic Characterization tool for tumor samples.
tags: [titan-gc, tumor-genomics, copy-number, cancer, structural-variation]
author: oxo-call-community
source_url: "https://github.com/compbio/titan-gc"
---

## Concepts

- **Tool Overview**: Titan-GC - A tool for analyzing copy number alterations and genomic characterization in tumor samples.
- **Core Function**: Identifies copy number variants, loss of heterozygosity (LOH), and structural variations in cancer genomes.
- **Input**: Tumor and normal sequencing data (BAM/FASTQ), VCF files.
- **Output**: Copy number profiles, LOH regions, structural variant calls.
- **Installation**: `pip install titan-gc` or `conda install -c bioconda titan-gc`
- **Use Case**: Cancer genomics, tumor profiling, copy number analysis.

## Pitfalls

- **Matched Normal**: Requires matched normal sample for accurate LOH detection.
- **Purity**: Tumor purity affects copy number estimation.

## Examples

### Analyze tumor genome
**Args:** `titan-gc -t tumor.bam -n normal.bam -o copy_number/`
**Explanation:** Analyze copy number alterations in tumor sample.

### With VCF input
**Args:** `titan-gc -v variants.vcf -o structural_variants/`
**Explanation:** Analyze structural variants from VCF file.
