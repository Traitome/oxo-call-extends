---
name: moss
category: variant-calling
description: A multi-sample somatic SNV caller
tags: [moss, variant-calling, somatic]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/Moss"
---

## Concepts

- **Tool Overview**: Moss v0.1.1 calls somatic SNVs from multiple samples.
- **Core Function**: Identifies somatic single-nucleotide variants across samples.
- **Multi-sample Analysis**: Analyzes multiple samples simultaneously.
- **Somatic Calling**: Focuses on somatic mutations in cancer samples.
- **Bayesian Model**: Uses Bayesian inference for variant calling.
- **Input/Output**: Accepts BAM files; outputs VCF with somatic variants.

## Pitfalls

- **Cancer Data Specific**: Designed for cancer sequencing data.
- **Memory Requirements**: Memory usage depends on sample count.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on sequencing quality and depth.
- **Normal Sample Required**: Needs matched normal sample for comparison.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Call somatic SNVs
**Args:** `moss -t tumor.bam -n normal.bam -g genome.fasta -o snvs.vcf`
**Explanation:** Calls somatic SNVs from tumor-normal pair.

### With multiple tumors
**Args:** `moss -t tumor1.bam tumor2.bam -n normal.bam -g genome.fasta -o snvs.vcf`
**Explanation:** Analyzes multiple tumor samples.

### With quality filtering
**Args:** `moss -t tumor.bam -n normal.bam -g genome.fasta -q -o snvs.vcf`
**Explanation:** Applies quality filtering before calling.

### Verbose output
**Args:** `moss -t tumor.bam -n normal.bam -g genome.fasta -v -o snvs.vcf`
**Explanation:** Shows detailed calling results.

### Batch processing
**Args:** `moss -t tumors/ -n normal.bam -g genome.fasta -o results/`
**Explanation:** Processes multiple tumor samples.