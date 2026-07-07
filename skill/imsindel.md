---
name: imsindel
category: variant-calling
description: Accurate intermediate-size indel detection tool combining de novo assembly and gapped alignment
tags: [imsindel, indel-detection, variant-calling, alignment]
author: oxo-call-community
source_url: "https://github.com/NCGG-MGC/IMSindel"
---

## Concepts

- **Tool Overview**: IMSindel (v1.0.2) is a specialized tool for detecting intermediate-size insertions and deletions (indels) from sequencing data.
- **Core Function**: Combines de novo assembly, gapped global-local alignment, and split-read analysis for accurate indel detection.
- **Input/Output**: Accepts BAM files with aligned reads. Outputs VCF files with detected indels and quality scores.
- **Size Range**: Optimized for indels in the range of 10-1000 base pairs, complementing standard variant callers.
- **Accuracy**: Achieves high sensitivity and specificity by integrating multiple detection strategies.

## Pitfalls

- **BAM File Requirements**: Input BAM files must be properly sorted and indexed.
- **Reference Genome**: Must provide matching reference genome in FASTA format.
- **Memory Usage**: Large genomes or deep sequencing data may require significant memory.
- **Indel Size Limits**: Primarily designed for intermediate-size indels; may miss very small or very large variants.
- **Computational Time**: De novo assembly component can be computationally intensive.

## Examples

### Basic indel detection
**Args:** `imsindel --bam input.bam --ref reference.fasta --out output.vcf`
**Explanation:** Detects intermediate-size indels from aligned BAM file.

### With quality filtering
**Args:** `imsindel --bam input.bam --ref ref.fasta --out output.vcf --min-qual 20`
**Explanation:** Filters output to include only indels with quality score ≥ 20.

### Targeted region analysis
**Args:** `imsindel --bam input.bam --ref ref.fasta --out output.vcf --bed target_regions.bed`
**Explanation:** Limits analysis to specific genomic regions defined in BED file.

### Paired-end specific options
**Args:** `imsindel --bam input.bam --ref ref.fasta --out output.vcf --pe-reads`
**Explanation:** Optimizes detection for paired-end sequencing data.

### Increase sensitivity
**Args:** `imsindel --bam input.bam --ref ref.fasta --out output.vcf --sensitive`
**Explanation:** Uses more sensitive (but slower) detection parameters.

### Parallel processing
**Args:** `imsindel --bam input.bam --ref ref.fasta --out output.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel computation.