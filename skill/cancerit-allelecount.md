---
name: cancerit-allelecount
category: variant-calling
description: Support code for NGS copy number algorithms - allele counting
tags: [allelecount, cnv, copy-number, allele, cancer]
author: oxo-call-community
source_url: "https://github.com/cancerit/alleleCount"
---

## Concepts

- **Tool Overview**: alleleCount counts alleles at specified positions from BAM files for CNV analysis.
- **Core Function**: Counts A/C/G/T bases at genomic positions for B-allele frequency calculation.
- **Input**: Sorted BAM file and list of SNP positions.
- **Output**: Allele counts at each position.
- **Application**: B-allele frequency calculation for copy number analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cancerit-allelecount`

## Pitfalls

- **BAM Required**: Requires sorted and indexed BAM file.
- **Position Format**: SNP positions must be in correct format.
- **Base Quality**: Adjust minimum base quality threshold.
- **Mapping Quality**: Set appropriate mapping quality filter.

## Examples

### Count alleles at SNP positions
**Args:** `alleleCounter -b aligned.bam -l snp_positions.tsv -o allele_counts.tsv`
**Explanation:** Counts alleles at specified SNP positions from BAM file.

### Set quality thresholds
**Args:** `alleleCounter -b aligned.bam -l snps.tsv -q 20 -m 30 -o counts.tsv`
**Explanation:** Uses base quality ≥20 and mapping quality ≥30 filters.

### Count at specific locus
**Args:** `alleleCounter -b aligned.bam -r chr1:1000000 -o locus_counts.tsv`
**Explanation:** Counts alleles at a specific genomic locus.

### Display help
**Args:** `alleleCounter --help`
**Explanation:** Shows all available options and usage information.
