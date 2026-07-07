---
name: snpick
category: variant-analysis
description: snpick - Fast and memory-efficient SNP extraction from genomic alignments
tags: [snpick, variant-analysis, snps, alignment, extraction]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/snpick"
---

## Concepts

- **Tool Overview**: snpick (v1.0.1) - A tool for extracting SNPs from alignments
- **Core Function**: Extracts SNP positions from genomic alignments efficiently
- **Input/Output**: Accepts BAM/FASTA alignments; outputs SNP lists
- **Algorithm**: Scans alignments for variant positions with memory efficiency
- **Installation**: `conda install -c bioconda snpick`
- **Key Features**: Fast extraction, memory-efficient, SNP identification

## Pitfalls

- **Input Requirements**: Requires properly formatted alignment files
- **Reference Genome**: Must use compatible reference genome
- **Memory Usage**: Large alignments may still require significant memory
- **Output Format**: Multiple output formats available
- **Filtering**: Requires proper filtering for quality SNPs
- **Coverage**: Low coverage regions may produce unreliable SNPs

## Examples

### Display help
**Args:** `snpick --help`
**Explanation:** Shows available options and usage information.

### Basic SNP extraction
**Args:** `snpick -i alignment.bam -o snps.txt`
**Explanation:** Extract SNPs from BAM alignment.

### From FASTA alignment
**Args:** `snpick -i alignment.fasta -o snps.txt`
**Explanation:** Extract SNPs from FASTA alignment.

### With reference
**Args:** `snpick -i alignment.bam -r reference.fasta -o snps.txt`
**Explanation:** Use reference for SNP extraction.

### Filter by quality
**Args:** `snpick -i alignment.bam -o snps.txt --min-quality 20`
**Explanation:** Filter SNPs by minimum quality.

### Filter by coverage
**Args:** `snpick -i alignment.bam -o snps.txt --min-coverage 10`
**Explanation:** Filter SNPs by minimum coverage.

### Output VCF format
**Args:** `snpick -i alignment.bam -o snps.vcf --vcf`
**Explanation:** Output SNPs in VCF format.

### With statistics
**Args:** `snpick -i alignment.bam -o snps.txt --stats`
**Explanation:** Output SNP statistics.