---
name: bolt
category: variant-calling
description: Variant caller for short-read sequencing data
tags: [bolt, variant-calling, snp, indel]
author: oxo-call-community
source_url: "https://github.com/sakkayaphab/bolt"
---

## Concepts

- **Tool Overview**: Bolt is a variant caller designed for short-read sequencing data.
- **Core Function**: Detects SNPs and small indels from aligned BAM files.
- **Input**: Sorted and indexed BAM file with aligned reads.
- **Output**: VCF format variant calls.
- **Installation**: Install via bioconda: `conda install -c bioconda bolt`

## Pitfalls

- **BAM Requirements**: Input BAM must be sorted and indexed.
- **Reference Required**: Reference FASTA must match the alignment reference.
- **Quality Filtering**: Apply appropriate quality filters for downstream analysis.
- **Coverage**: Low coverage regions may have reduced sensitivity.

## Examples

### Call variants
**Args:** `bolt call -b aligned.bam -r reference.fa -o variants.vcf`
**Explanation:** Calls variants from aligned BAM file against reference genome.

### Call with minimum quality
**Args:** `bolt call -b aligned.bam -r reference.fa -q 20 -o variants.vcf`
**Explanation:** Filters variants with minimum quality score of 20.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.

### Check version
**Args:** `--version`
**Explanation:** Displays installed version for reproducibility.
