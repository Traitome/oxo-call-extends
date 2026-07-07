---
name: somaticseq
category: variant-calling
description: SomaticSeq - Ensemble approach for accurate somatic mutation detection
tags: [somaticseq, variant-calling, somatic, mutations, ensemble]
author: oxo-call-community
source_url: "https://bioinform.github.io/somaticseq"
---

## Concepts

- **Tool Overview**: somaticseq (v3.11.1) - An ensemble somatic variant caller
- **Core Function**: Combines multiple variant callers for accurate somatic detection
- **Input/Output**: Accepts BAM files; outputs VCF with somatic mutations
- **Algorithm**: Machine learning ensemble approach for variant calling
- **Installation**: `conda install -c bioconda somaticseq`
- **Key Features**: Ensemble calling, somatic variants, machine learning

## Pitfalls

- **Input Requirements**: Requires tumor and normal BAM files
- **Reference Genome**: Requires reference genome for alignment
- **Multiple Callers**: Requires outputs from multiple variant callers
- **Memory Usage**: Large BAM files require significant memory
- **Training Data**: Machine learning model requires proper training
- **Output Format**: Output format depends on configuration

## Examples

### Display help
**Args:** `somaticseq --help`
**Explanation:** Shows available options and usage information.

### Basic somatic calling
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf`
**Explanation:** Call somatic variants from tumor-normal pair.

### With ensemble mode
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --ensemble`
**Explanation:** Use ensemble approach for calling.

### With machine learning
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --ml`
**Explanation:** Use machine learning model.

### With multiple callers
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --callers mutect2 vardict`
**Explanation:** Combine multiple variant callers.

### Filter variants
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --filter`
**Explanation:** Apply variant filtering.

### Output statistics
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --stats`
**Explanation:** Output calling statistics.

### Generate report
**Args:** `somaticseq -t tumor.bam -n normal.bam -r reference.fasta -o output.vcf --report`
**Explanation:** Generate somatic calling report.