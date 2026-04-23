---
name: bgt
category: variant-calling
description: BGT - Flexible genotype query among 30,000+ samples whole-genome
tags: [genotype-query, vcf, large-scale, variant]
author: oxo-call-community
source_url: "https://github.com/lh3/bgt"
---

## Concepts
- **Tool Overview**: BGT is a tool for flexible genotype queries across large-scale whole-genome datasets (30,000+ samples). It provides efficient random access to genotype data in BCF/VCF format.
- **Large-Scale Queries**: Designed for querying subsets of samples or genomic regions from very large variant datasets.
- **Efficient Access**: Uses indexing for fast retrieval without loading entire files into memory.
- **Applications**: Population genetics, association studies, and large cohort analyses.

## Pitfalls
- **Indexing Required**: BCF/VCF files must be indexed (with `bcftools index`) before querying.
- **Memory**: While more efficient than loading entire files, large queries still require substantial memory.
- **Sample Names**: Sample names must match exactly between query and data file.

## Examples
### Query specific region
**Args:** `bgt query -r chr1:1000000-2000000 data.bcf`
**Explanation:** Retrieves genotype data for a specific genomic region.

### Query specific samples
**Args:** `bgt query -s sample1,sample2,sample3 data.bcf`
**Explanation:** Retrieves genotype data for specific samples.

### Query with genotype filter
**Args:** `bgt query -r chr22 -g hom data.bcf`
**Explanation:** Retrieves homozygous genotypes from chromosome 22.
