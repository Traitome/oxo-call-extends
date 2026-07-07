---
name: tgt
category: analysis
description: TGT - Targeted Genotyping Tool for high-confidence variant calling.
tags: [tgt, genotyping, variant-calling, targeted-sequencing, snp, indels]
author: oxo-call-community
source_url: "https://github.com/compbio/tgt"
---

## Concepts

- **Tool Overview**: TGT (Targeted Genotyping Tool) - A tool for high-accuracy genotyping and variant calling from targeted sequencing data.
- **Core Function**: Performs targeted variant calling with high accuracy by leveraging known variant sites and quality filters.
- **Input**: Targeted sequencing reads (FASTQ/BAM), target region BED, known variants (optional).
- **Output**: VCF file with called variants, genotype calls, quality scores.
- **Installation**: `pip install tgt` or `conda install -c bioconda tgt`
- **Use Case**: Clinical targeted sequencing, validation of known variants, population genetics.

## Pitfalls

- **Target Region**: Accurate target region definition is critical.
- **Allele Balance**: Heterozygous variants may be imbalanced in targeted sequencing.

## Examples

### Genotype targets
**Args:** `tgt -i reads.bam -b targets.bed -o genotypes.vcf`
**Explanation:** Call genotypes at targeted regions from sequencing data.

### With known variants
**Args:** `tgt -i sample.bam -b targets.bed -v known_variants.vcf -o results.vcf`
**Explanation:** Use known variants as reference for more accurate genotyping.
