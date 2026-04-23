---
name: bsaseq
category: population-genomics
description: Bulk Segregant Analysis for QTL mapping from pooled whole-genome sequencing
tags: [bsaseq, bsa, qtl, pooled-seq, bulk-segregant]
author: oxo-call-community
source_url: "https://github.com/rcac-bioinformatics/bsaseq"
---

## Concepts

- **Tool Overview**: BSAseq performs Bulk Segregant Analysis for QTL mapping using pooled sequencing.
- **Core Function**: Identifies genomic regions associated with traits using bulked segregant pools.
- **Input**: Pooled sequencing data from contrasting phenotype bulks.
- **Output**: QTL intervals and SNP index plots.
- **Application**: Rapid QTL mapping in plant and animal genetics.
- **Installation**: Install via bioconda: `conda install -c bioconda bsaseq`

## Pitfalls

- **Pool Design**: Requires proper bulk design with contrasting phenotypes.
- **Coverage**: Sufficient coverage in both pools is critical.
- **Reference Genome**: Requires reference genome for SNP calling.
- **SNP Filtering**: Filter SNPs by quality and depth before analysis.

## Examples

### Run BSA analysis
**Args:** `bsaseq -b1 bulk1.vcf -b2 bulk2.vcf -r reference.fa -o bsa_results/`
**Explanation:** Performs BSA analysis comparing two phenotype bulks.

### Set window size
**Args:** `bsaseq -b1 bulk1.vcf -b2 bulk2.vcf -w 1000000 -o results/`
**Explanation:** Uses 1Mb sliding window for SNP index calculation.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
