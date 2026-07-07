---
name: svjedi
category: variant-calling
description: Structural variation genotyper for long-read sequencing data.
tags: [svjedi, structural-variants, long-reads, genotyping]
author: oxo-call-community
source_url: "https://github.com/llecompte/SVJedi"
---

## Concepts

- **Tool Overview**: svjedi (v1.1.6) is a structural variation genotyper for long-read data.
- **Core Function**: Genotypes known structural variants from long sequencing reads.
- **Algorithm**: Uses alignment signatures to determine genotypes of known SVs.
- **Input/Output**: Input: BAM file, SV VCF, reference genome; Output: Genotyped VCF.
- **Applications**: SV genotyping, population genetics, variant validation.
- **Installation**: `conda install -c bioconda svjedi` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Genotyping large SV sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect genotyping accuracy.
- **Input Quality**: Requires high-quality SV calls as input.
- **Alignment Quality**: Requires well-aligned BAM files.
- **SV Complexity**: Complex SVs may be difficult to genotype.

## Examples

### Display help
**Args:** `svjedi --help`
**Explanation:** Shows available options and usage information.

### Basic SV genotyping
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype SVs from long reads.

### With multiple samples
**Args:** `svjedi -i samples.txt -v sv.vcf -r reference.fasta -o genotyped.vcf`
**Explanation:** Genotype multiple samples together.

### Verbose mode
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --stats`
**Explanation:** Generate statistics about genotyping.

### Batch processing
**Args:** `svjedi -i bams/ -v sv.vcf -r reference.fasta -o results/`
**Explanation:** Process multiple BAM files together.

### Filter by quality
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf -q 0.9`
**Explanation:** Filter by confidence score.

### Include all SV types
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --all-types`
**Explanation:** Genotype all types of structural variants.

### Generate report
**Args:** `svjedi -i sample.bam -v sv.vcf -r reference.fasta -o genotyped.vcf --report`
**Explanation:** Generate comprehensive HTML report.
