---
name: nanocaller
category: variant-calling
description: NanoCaller - Accurate variant detection for long-read sequencing in difficult-to-map regions
tags: [nanocaller, variant-calling, nanopore, snp, indel, long-reads]
author: oxo-call-community
source_url: "https://github.com/WGLab/NanoCaller"
---

## Concepts

- **Tool Overview**: NanoCaller v3.6.2 is a variant caller specifically designed for long-read sequencing data (Nanopore/PacBio). It specializes in detecting SNPs and indels in difficult-to-map regions of the genome.
- **Core Function**: Accurately calls genetic variants from long-read alignments, with particular strength in repetitive regions, segmental duplications, and other genomic regions that are challenging for short-read callers.
- **Algorithm**: Uses a machine learning approach to distinguish true variants from sequencing errors. Incorporates read-level features like mapping quality, base quality, and strand bias for improved accuracy.
- **Input Format**: Requires sorted and indexed BAM files from long-read aligners (minimap2, NGMLR, etc.) and a reference genome in FASTA format.
- **Output**: Produces VCF files containing SNP and indel calls with quality scores, allele frequencies, and supporting read information.
- **Use Case**: Clinical variant detection from long-read data, population genetics studies, and analysis of complex genomic regions.

## Pitfalls

- **Alignment Quality**: Variant calling accuracy depends heavily on alignment quality. Use appropriate long-read aligners with proper parameters.
- **Basecalling Errors**: Higher error rates in raw Nanopore data require careful filtering. Consider using high-accuracy basecallers like Guppy's high-accuracy mode.
- **Read Coverage**: Low coverage regions produce unreliable calls. Aim for at least 20x coverage for confident variant detection.
- **Structural Variants**: While focused on SNPs and indels, larger structural variants may require additional tools for detection.
- **False Positives**: Stringent filtering is recommended for clinical applications. Use multiple quality filters to reduce false positives.
- **Reference Bias**: Variant calls may be biased towards the reference allele. Consider using phased data when available.

## Examples

### Basic variant calling
**Args:** `-b aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Standard NanoCaller workflow. Calls SNPs and indels from long-read alignments.

### Include low-complexity regions
**Args:** `-b reads.bam -r ref.fa -o variants.vcf --include_low_complexity`
**Explanation:** Forces variant calling in low-complexity regions that are normally skipped.

### Use phased data
**Args:** `-b phased.bam -r reference.fa -o phased_variants.vcf --phase`
**Explanation:** Uses phased reads to improve variant calling accuracy and phase output.

### Adjust minimum quality score
**Args:** `-b aligned.bam -r ref.fasta -o filtered.vcf -q 30`
**Explanation:** Only reports variants with quality score >= 30.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
