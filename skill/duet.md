---
name: duet
category: variant-calling
description: "SNP-Assisted Structural Variant Calling and Phasing Using Oxford Nanopore Sequencing"
tags: [duet, variant-calling, structural-variants, SNP, phasing, nanopore]
author: oxo-call-community
source_url: "https://github.com/yekaizhou/duet"
---

## Concepts

- **Tool Overview**: Duet is a tool for SNP-assisted structural variant calling and phasing using Oxford Nanopore sequencing data.
- **Core Function**: Combines SNP information with long-read data to detect and phase structural variants.
- **Input/Output**: Input: BAM alignment file, reference genome (FASTA), VCF with SNPs. Output: Phased structural variants (VCF).
- **Algorithm**: Uses SNP haplotype information to guide structural variant detection and phasing.
- **Key Features**: SNP-assisted SV calling, haplotype phasing, long-read support, high accuracy.
- **Installation**: `conda install -c bioconda duet`

## Pitfalls

- **SNP Density**: Requires sufficient SNP density for accurate phasing.
- **Read Length**: Very short reads may not span structural variants.
- **Coverage Depth**: Low coverage reduces SV detection sensitivity.
- **Alignment Quality**: Poor alignments can produce false positive SV calls.
- **Complex Variants**: Complex rearrangements may be challenging to resolve.

## Examples

### Basic SV calling and phasing
**Args:** `--bam aligned.bam --ref ref.fa --snps snps.vcf --output sv.vcf`
**Explanation:** Calls and phases structural variants using SNP information.

### With custom parameters
**Args:** `--bam aligned.bam --ref ref.fa --snps snps.vcf --output sv.vcf --min-sv-size 50`
**Explanation:** Sets minimum SV size threshold to 50bp.

### High sensitivity mode
**Args:** `--bam aligned.bam --ref ref.fa --snps snps.vcf --output sv.vcf --sensitive`
**Explanation:** Uses high sensitivity settings for SV detection.

### Parallel processing
**Args:** `--bam aligned.bam --ref ref.fa --snps snps.vcf --output sv.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Generate report
**Args:** `--bam aligned.bam --ref ref.fa --snps snps.vcf --output sv.vcf --report report.txt`
**Explanation:** Generates detailed report of SV calling and phasing results.