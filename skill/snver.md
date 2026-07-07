---
name: snver
category: variant-analysis
description: SNVer - Statistical tool for calling variants in pooled and individual NGS data
tags: [snver, variant-analysis, pooled-seq, statistics, ngs]
author: oxo-call-community
source_url: "http://snver.sourceforge.net/"
---

## Concepts

- **Tool Overview**: snver (v0.5.3) - A statistical variant caller for pooled and individual data
- **Core Function**: Calls common and rare variants with statistical significance
- **Input/Output**: Accepts BAM files; outputs VCF with variant calls and p-values
- **Algorithm**: Uses statistical model for variant significance testing
- **Installation**: `conda install -c bioconda snver`
- **Key Features**: Pooled sequencing, statistical testing, rare variant detection

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM files
- **Reference Genome**: Must use compatible reference genome
- **Pool Size**: Pool size affects statistical power
- **Coverage**: Low coverage reduces variant detection accuracy
- **Multiple Testing**: Requires correction for multiple testing
- **Computation Time**: Large datasets can be slow to process

## Examples

### Display help
**Args:** `snver --help`
**Explanation:** Shows available options and usage information.

### Individual variant calling
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from individual sample.

### Pooled variant calling
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --pool-size 10`
**Explanation:** Call variants from pooled sample.

### With p-value threshold
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --p-value 0.01`
**Explanation:** Set p-value threshold for significance.

### With coverage filter
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --min-coverage 10`
**Explanation:** Set minimum coverage threshold.

### Rare variant detection
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --rare`
**Explanation:** Enable rare variant detection mode.

### Common variant detection
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --common`
**Explanation:** Enable common variant detection mode.

### Generate report
**Args:** `snver -i aligned.bam -r reference.fasta -o variants.vcf --report`
**Explanation:** Generate variant calling report.