---
name: samrefiner
category: variant_calling
description: Extract variant information from SAM/BAM files
tags: ["samrefiner", "variant calling", "SAM", "BAM", "SNV"]
author: oxo-call-community
source_url: "https://github.com/degregory/SAM_Refiner"
---

## Concepts

- **Tool Overview**: SAM Refiner (v1.4.2.1) is a program for gathering variant information from SAM/BAM formatted files, enabling extraction of SNVs, indels, and other variant types.
- **Core Function**: Analyzes aligned reads to identify potential variants, providing detailed information about variant positions, allele frequencies, and supporting evidence.
- **Algorithm**: Parses CIGAR strings and MD tags to identify mismatches and indels, calculates allele frequencies, and generates variant calls.
- **Input Format**: SAM/BAM alignment files, optional reference genome.
- **Output Format**: Variant calls in VCF format, variant statistics, coverage reports.
- **Use Case**: Variant calling, quality control, population genetics, personalized medicine.

## Pitfalls

- **Alignment quality**: Results depend on alignment accuracy.
- **Coverage depth**: Low coverage may miss true variants.
- **Mapping quality**: Poorly mapped reads may introduce false positives.
- **Indel detection**: Complex indels may not be correctly identified.
- **Memory usage**: Large BAM files require significant memory.
- **Reference genome**: Required for accurate variant calling.

## Examples

### Basic variant calling
**Args:** `samrefiner -i input.bam -o variants.vcf`
**Explanation:** `-i` input BAM; `-o` output VCF.

### With reference genome
**Args:** `samrefiner -i input.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-r` reference genome for variant context.

### Quality filtering
**Args:** `samrefiner -i input.bam -o variants.vcf -q 30`
**Explanation:** `-q` minimum mapping quality threshold.

### Coverage filtering
**Args:** `samrefiner -i input.bam -o variants.vcf -c 10`
**Explanation:** `-c` minimum coverage threshold.

### Output statistics
**Args:** `samrefiner -i input.bam -o variants.vcf -s stats.txt`
**Explanation:** `-s` outputs variant statistics.

### Include indels
**Args:** `samrefiner -i input.bam -o variants.vcf --indels`
**Explanation:** `--indels` enables indel detection.

### Verbose mode
**Args:** `samrefiner -i input.bam -o variants.vcf -v`
**Explanation:** `-v` verbose output with detailed information.